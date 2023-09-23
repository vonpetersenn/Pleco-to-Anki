from pleco.Bookmarks_old import Bookmarks
from pleco.definition_helpers_old import *

import time

# TODO: Add dependencies to requirements.txt
# TODO: Add tests
# TODO: wrap project in Anki add-on
# TODO: Fork pinyin function and store in separate library folder

file_name = 'anki_addon/pleco/plecodata.txt'

from pleco.bookmark_helpers import *

def main():

    bookmarks = Bookmarks()
    if bookmarks.reformat_pinyin:
        bookmarks.reformat_pinyin()

def main_old():

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

if __name__ == "__main__":
    main()