import pandas as pd
from tones.numerical_pinyin_converter import convert_from_numerical_pinyin
from constants import *
from pleco.Definition import Definition
from spoonfed.Spoonfed import Spoonfed
from pleco.bookmarks_helpers import load_pleco_file, preprocess

from tqdm import tqdm
tqdm.pandas()


class Bookmarks:
    def __init__(self, file_name):

        # Initialize the raw_data DataFrame by reading from the specified file
        self.raw_data = self.load_pleco_file(file_name)

        # The file will contain some information that does not refer to bookmarks
        self.raw_data = self.raw_data.apply(lambda x: preprocess(x), axis=1)

        self.anki_notes = self.initialize_anki_notes()

    def __len__(self):
        return len(self.anki_notes)

    def export_to_csv(self):
        self.anki_notes.to_csv(OUTPUT_FILE_NAME, index=False, sep='|')
        print('Exported successfully to ' + OUTPUT_FILE_NAME)

    def reformat_pinyin(self):
        self.anki_notes['Pinyin'] = self.anki_notes['Pinyin'].apply(convert_from_numerical_pinyin)
        print('Reformatting Pinyin to use tone marks i.e. "ni3 hao3" -> "nǐ hǎo"...')

    def build_english_and_definition_fields(self):
        self.anki_notes['English'] = self.get_english()
        self.anki_notes['Example'] = self.get_example()
        if REFORMAT_EXAMPLE_SENTENCES:
            print('Hiding pinyin and translation of example sentences behind the Chinese characters...')

    def add_spoonfed_sentences(self):
        self.anki_notes['Spoonfed'] = self.raw_data['Hanzi'].copy()
        self.anki_notes['Spoonfed'] = self.anki_notes['Spoonfed'].progress_apply(lambda x: Spoonfed(x).get_spoonfed_sentences())

    ############################

    def load_pleco_file(self, file_name):
        raw_data = load_pleco_file(file_name)
        return raw_data

    def initialize_anki_notes(self):
        anki_notes = pd.DataFrame(columns = ANKI_HEADERS)
        anki_notes['Hanzi'] = self.raw_data['Hanzi']
        anki_notes['Pinyin'] = self.raw_data['Pinyin']

        return anki_notes

    def get_english(self):
        self.anki_notes['English'] = self.raw_data['Information']
        self.anki_notes['English'] = self.anki_notes['English'].apply(lambda x: Definition(x).get_definition())
        return self.anki_notes['English']

    def get_example(self):
        self.anki_notes['Example'] = self.raw_data['Information']
        self.anki_notes['Example'] = self.anki_notes['Example'].apply(lambda x: Definition(x).get_example_sentences())
        return self.anki_notes['Example']