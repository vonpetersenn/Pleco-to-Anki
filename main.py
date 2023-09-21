from pleco.Bookmarks import Bookmarks
from pleco.definition_helpers import *

import time

# TODO: Add dependencies to requirements.txt
# TODO: Add tests
# TODO: wrap project in Anki add-on
# TODO: Fork pinyin function and store in separate library folder

def main():

    bookmarks = Bookmarks(FILE_NAME)

    if REFORMAT_PINYIN:
        bookmarks.reformat_pinyin()

    bookmarks.build_english_and_definition_fields()

    if SPOONFED_EXAMPLES:
        print('Adding Spoonfed examples...')
        start_time = time.time()
        bookmarks.add_spoonfed_sentences()
        end_time = time.time()
        print('Runtime of Spoonfed lookups: ' + str(round(end_time - start_time, 1)) + 's')

    bookmarks.export_to_csv()

from tests.test_Definition import test_Definition_definition
from tests.test_Definition import test_Definition_example_sentences
from tests.test_Definition import load_example_file

def debugging():
    #print(test_Definition_example_sentences(load_example_file('tests/test_Definition_input_1.txt')))
    #print(load_example_file('tests/test_Definition_output_example_sentences_1.txt'))
    print(test_Definition_definition('tests/test_Definition_input_1.txt'))
if __name__ == "__main__":
    #main()
    debugging()