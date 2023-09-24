import unicodedata
from .keyword_replacements import KEYWORD_REPLACEMENTS
keyword_replacements = KEYWORD_REPLACEMENTS
from .pinyin_exceptions import PINYIN_EXCEPTIONAL_CASES
pinyin_exceptional_cases = PINYIN_EXCEPTIONAL_CASES

class Definition:

    def __init__(self, information, configs):

        self.configs = configs
        self.information = information

        if self.configs.supress_cross_references:
            self.information = supress_cross_references(self.information)

        self.segments = []
        self.word_types = []

        self.definition = ''
        self.example_sentences = ''

        self.segments, self.word_types = split_into_segments(self.information)
        self.segments, self.word_types = find_example_sentences(self.segments, self.word_types)

        # add html tags to hide pinyin and translations behind the chinese characters
        if self.configs.reformat_example_sentences:
            self.segments = reformat_example_sentences(self.segments, self.word_types)
        else:
            self.segments = build_basic_example_sentences(self.segments, self.word_types)

        # more pretty formatting of "verb", "noun", etc.
        if self.configs.reformat_keywords:
            self.segments = reformat_keywords(self.segments, self.word_types, keyword_replacements)

        self.segments, self.word_types = strip_segments_of_numbers(self.segments, self.word_types)

        # we don't want to have <br> after keywords in our anki notes, so we need to join keywords with the english word that follows them
        self.segments, self.word_types = join_keyword_with_english_segments(self.segments, self.word_types)

        self.segments = do_minor_reformatting(self.segments)


        # group example sentences and definitions as they serve different purposes in our anki notes
        self.definition, self.example_sentences = [], []
        if self.configs.group_example_sentences:
            self.definition, self.example_sentences = group_example_sentences(self.segments, self.word_types)
        else:
            if len(self.segments) > 1:
                self.definition, self.example_sentences = [self.segments[0]], self.segments[1:]
            else:
                self.definition, self.example_sentences = self.segments, []

    def get_definition(self):
        return build_string_from_list(self.definition)

    def get_example_sentences(self):
        return build_string_from_list(self.example_sentences)


# cross references result in long ugly strings. this function removes the crossreferences from the raw information string
def supress_cross_references(long_string):

    # Split the string into parts using 'See ' as a delimiter
    parts = long_string.split(' See ')

    if len(parts) == 1:
        return long_string

    new_string = parts[0]

    for string in parts[1:]:
        sub_parts = string.split(' ')
        if len(sub_parts) > 1:
            sub_parts = sub_parts[1:]
            new_string += ' ' + ' '.join(sub_parts)

    return new_string

def build_string_from_list(list_of_strings):

    if len(list_of_strings) == 1 and type(list_of_strings[0]) == str:
        return list_of_strings[0]

    a = ''
    for list in list_of_strings:
        b = ''
        for string in list:
            b += string
            b += ''
        a += b + '<br>'
    return a

def group_example_sentences(segments, word_types):

    definition, example_sentences = [], []

    for index, segment in enumerate(segments):
        if word_types[index] == 'example':
            example_sentences.append(segment)
        else:
            definition.append(segment)

    return definition, example_sentences

def do_minor_reformatting(segments):
    new_segments = []

    for segment in segments:
        segment = prettify_or_case(segment)
        segment = strip_double_spaces(segment)
        new_segments.append(segment)
    return new_segments

def strip_double_spaces(input_string):
    return input_string.replace('  ', ' ')

def join_keyword_with_english_segments(segments, word_types):
    if len(segments) < 2:
        return segments, word_types

    new_segments = []
    new_word_types = []

    for segment, word_type in zip(segments, word_types):
        if word_type == 'keyword':
            # Check if there's a following 'english' segment
            next_index = segments.index(segment) + 1
            if next_index < len(segments) and word_types[next_index] == 'english':
                new_segment = f"{segment} {segments[next_index]}"
                new_segments.append(new_segment)
                new_word_types.append('english')
                # Skip the next segment
                segments[next_index] = ''
                word_types[next_index] = ''
            else:
                new_segments.append(segment)
                new_word_types.append(word_type)
        elif word_type != '':
            new_segments.append(segment)
            new_word_types.append(word_type)

    return new_segments, new_word_types

def strip_segments_of_numbers(segments, word_types):
    new_segments, new_word_types = [], []

    for index, segment in enumerate(segments):
        if word_types[index] == 'number':
            pass
        else:
            new_segments.append(segment)
            new_word_types.append(word_types[index])

    return new_segments, new_word_types

def reformat_keywords(segments, word_types, keyword_replacements=keyword_replacements):
    new_segments = []

    for index, segment in enumerate(segments):
        if word_types[index] == 'keyword':
            new_segments.append(keyword_replacements[segment])
        else:
            new_segments.append(segment)

    segments = new_segments
    return segments

def build_basic_example_sentences(segments, word_types):
    new_segments = []
    for index, segment in enumerate(segments):
        if word_types[index] == 'example':
            string = segment[0] + '<br>' + segment[1] + '<br>' + segment[2] + '<br>'
            new_segments.append(string)
        else:
            new_segments.append(segment)
    return new_segments

def reformat_example_sentences(segments, word_types):
    new_segments = []
    for index, segment in enumerate(segments):
        if word_types[index] == 'example':
            string = build_hidden_example_sentence(segment[0], segment[1], segment[2])
            string = prettify_or_case(string)
            new_segments.append(string)
        else:
            new_segments.append(segment)
    return new_segments

def build_hidden_example_sentence(chinese: str, pinyin: str, english: str) -> str:
    example_sentence = '<details><summary><big>' \
                       + chinese \
                       + '</big></summary>' + '<small>' \
                       + pinyin \
                       + '<br>' + '</small>'\
                       + english \
                       + '<br></details><br>'
    return example_sentence

def prettify_or_case(input_string):
    # Check if the input string contains ". or"
    if ". or" in input_string:
        # Replace ". or" with ".<br><i>or </i>"
        input_string = input_string.replace(". or", ".<br><i>or </i>")
    return input_string

def find_example_sentences(segments, word_types):

    found_example_sentence = identify_example_sentences(segments, word_types)#logical list
    new_segments, new_word_types = [], []

    index = 0

    while index < len(segments) - 2:
        if found_example_sentence[index]:
            new_segments.append([segments[index], segments[index + 1], segments[index + 2]])
            new_word_types.append('example')

            # Set the word types to empty strings for the matched elements
            word_types[index + 1] = ''
            word_types[index + 2] = ''

            # Move the index forward by 3 to skip the matched elements
            index += 3

        elif word_types[index] != '':
            new_segments.append(segments[index])
            new_word_types.append(word_types[index])

            index += 1

    while index < len(segments):
        if word_types[index] != '':
            new_segments.append(segments[index])
            new_word_types.append(word_types[index])

        index += 1
    return new_segments, new_word_types

def identify_example_sentences(segments, word_types):
    # an example sentence is a tripel [chinese, pinyin, english]
    found_example_sentence = []

    if len(segments) < 3:
        for i in segments:
            found_example_sentence.append(False)
        return found_example_sentence

    for index in range(len(segments) - 2):
        if word_types[index] == 'chinese' and word_types[index + 1] == 'pinyin' and word_types[index + 2] == 'english':
            found_example_sentence.append(True)
        else:
            found_example_sentence.append(False)

    return found_example_sentence

def split_into_segments(information):
    segments = split_text(information)
    word_types = classify_segment(segments)

    return segments, word_types

def classify_segment(list):
    classifier = []
    segment : str
    for index, segment in enumerate(list):
        if is_chinese(segment):
            classifier.append('chinese')
        elif is_pinyin(segment):
            classifier.append('pinyin')
        elif is_keyword(segment):
            classifier.append('keyword')
        elif is_number(segment):
            classifier.append('number')
        else:
            classifier.append('english')
    return classifier

def split_text(text):
    words = text.split(' ')

    classifier = []
    for word in words:
        if is_chinese(word):
            classifier.append('chinese')
        elif is_pinyin(word):
            classifier.append('pinyin')
        elif is_keyword(word):
            classifier.append('keyword')
        elif is_number(word):
            classifier.append('number')
        else:
            classifier.append('english')

    segments = []
    current_segment = []
    for index, word in enumerate(words):
        if index == 0:
            current_segment.append(word)
        elif classifier[index] == 'number' or classifier[index] != classifier[index - 1]:
            segments.append(' '.join(current_segment))
            current_segment = [word]
        else: #classifier[index] == classifier[index - 1]:
            current_segment.append(word)

    segments.append(' '.join(current_segment))

    return segments

def is_keyword(word : str) -> bool:
    if word in keyword_replacements.keys():
        return True
    else:
        return False

def is_chinese(text : str) -> bool:
    for char in text:
        if 'CJK' in unicodedata.name(char, ''):
            return True
    return False

def is_pinyin(text : str) -> bool:
    normalized_text = unicodedata.normalize('NFD', text)
    for char in normalized_text:
        if unicodedata.combining(char):
            return True
        elif text in pinyin_exceptional_cases:
            return True
    return False

def is_number(text: str) -> bool:
    try:
        float(text)  # Try to convert the string to a float
        return True
    except ValueError:
        return False