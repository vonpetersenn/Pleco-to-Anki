from pleco.definition_helpers import *
from pleco.keyword_replacements import KEYWORD_REPLACEMENTS
from constants import *


# the 'definition' or just 'dictionary entry' contained in the pleco bookmarks are the most complex piece of information
#   as they contain a lot of information in a linear string,
# we need to reformat them to be of value to us when importing them into anki

class Definition:

    def __init__(self, string):

        if pd.isna(string):
            print('Warning: Bookmark with empty definition found.')
            string = ''

        if not isinstance(string, str):
            raise TypeError(f"Definition must be initialized with a string, not {type(string)}.")

        self.raw_information = string

        if SUPRESS_CROSS_REFERENCES:
            self.information = supress_cross_references(self.raw_information)

        # the gros of the work on the definition string is done by working on lists of sub strings "segments" together
        # with a list of "word_types" that classify each segment as either a translation, example sentence, or keyword

        self.segments, self.word_types = [], []
        self.split_into_segments()

        self.find_example_sentences()

        #add html tags to hide pinyin and translations behind the chinese characters
        if REFORMAT_EXAMPLE_SENTENCES:
            self.reformat_example_sentences()

        #more pretty formatting of "verb", "noun", etc.
        if REFORMAT_KEYWORDS:
            self.reformat_keywords()

        self.strip_segments_of_numbers()

        #we don't want to have <br> after keywords in our anki notes,
        #so we need to join keywords with the english word that follows them
        self.join_keyword_with_english_segments()

        #no double spaces and stuff like that, add <br> tags etc.
        self.do_minor_reformatting()

        #group example sentences and definitions as they serve different purposes in our anki notes
        self.definition, self.example_sentences = [], []
        if GROUP_EXAMPLE_SENTENCES:
            self.group_example_sentences()
        else:
            self.definition, self.example_sentences = self.segments[0], self.segments[1:]

    def get_definition(self):
        return build_string_from_list(self.definition)

    def get_example_sentences(self):
        return build_string_from_list(self.example_sentences)

################################################################
################################################################

    # in the definition string, we have short translations, example sentences containing Chinese, Pinyin, and English,
    # and Keywords like ('noun', 'verb', etc.)
    # we first need to split the string into its components Translation, Example, and Keywords where Example has the
    # sub components Chinese, Pinyin, and English.

################################################################
################################################################

    def reformat_keywords(self):
        self.segments = reformat_keywords(self.segments, self.word_types, KEYWORD_REPLACEMENTS)

    def split_into_segments(self):
        self.segments = split_text(self.information)
        self.word_types = classify_segment(self.segments)

        return self.segments, self.word_types

    def join_keyword_with_english_segments(self):
        self.segments, self.word_types = join_keyword_with_english_segments(self.segments, self.word_types)

    def find_example_sentences(self):
        self.segments, self.word_types = find_example_sentences(self.segments, self.word_types)

    def group_example_sentences(self):
        self.definition, self.example_sentences = group_example_sentences(self.segments, self.word_types)

    def reformat_example_sentences(self):
        self.segments = reformat_example_sentences(self.segments, self.word_types)

    def strip_segments_of_numbers(self):
        self.segments, self.word_types = strip_segments_of_numbers(self.segments, self.word_types)

    def do_minor_reformatting(self):
        self.segments = do_minor_reformatting(self.segments, self.word_types)

