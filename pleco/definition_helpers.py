from pleco.bookmarks_helpers import *
from pleco.keyword_replacements import KEYWORD_REPLACEMENTS
from constants import *

#cross references within the pleco dictionary are being translated to a messy string,
#which can be recognized by the pattern: 'See ' [cross reference] ' '
    # e.g. ' See 59536867斷球duan4qiu2斷球 '
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


keyword_replacements : dict
def reformat_keywords(segments, word_types, keyword_replacements=KEYWORD_REPLACEMENTS):
    new_segments = []

    for index, segment in enumerate(segments):
        if word_types[index] == 'keyword':
            new_segments.append(keyword_replacements[segment])
        else:
            new_segments.append(segment)

    segments = new_segments
    return segments

# we don't want to have <br> after keywords in our anki notes,
# so we need to join keywords with the english word that follows them
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


def strip_segments_of_numbers(segments, word_types):
    new_segments, new_word_types = [], []

    for index, segment in enumerate(segments):
        if word_types[index] == 'number':
            pass
        else:
            new_segments.append(segment)
            new_word_types.append(word_types[index])

    return new_segments, new_word_types


def do_minor_reformatting(segments, word_types):
    new_segments = []

    for segment in segments:
        segment = prettify_or_case(segment)
        segment = strip_double_spaces(segment)
        new_segments.append(segment)
    return new_segments

def strip_double_spaces(input_string):
    return input_string.replace('  ', ' ')


# some example sentences will contain two translations with the binder ". or"
# we want to reformat this case
def prettify_or_case(input_string):
    # Check if the input string contains ". or"
    if ". or" in input_string:
        # Replace ". or" with ".<br><i>or </i>"
        input_string = input_string.replace(". or", ".<br><i>or </i>")
    return input_string

definition : str
example_sentences : str

def group_example_sentences(segments, word_types):

    definition, example_sentences = [], []

    for index, segment in enumerate(segments):
        if word_types[index] == 'example':
            example_sentences.append(segment)
        else:
            definition.append(segment)

    return definition, example_sentences

def build_hidden_example_sentence(chinese: str, pinyin: str, english: str) -> str:
    example_sentence = '<details><summary><big>' \
                       + chinese \
                       + '</big></summary>' + '<small>' \
                       + pinyin \
                       + '<br>' + '</small>'\
                       + english \
                       + '<br></details><br>'
    return example_sentence

# here we also deal with the case of lists that hold strings or lists of lists of strings
# this case might arise if REFORMAT_EXAMPLE_WORDS is set to False
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
