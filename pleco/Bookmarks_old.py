from pleco.bookmark_helpers import *
from anki_addon.tones.numerical_pinyin_converter import convert_from_numerical_pinyin


class Bookmarks:

    def __init__(self):

        self.file_name = "../anki_addon/exampledata.txt"

        self.raw_data = load_pleco_data(self.file_name)

        self.raw_data = load_pleco_data(self.file_name)

        self.reformat_pinyin = True


    def __str__(self):
        return str(self.raw_data)

    def reformat_pinyin(self):

        for key, value in self.raw_data.items():
            key, value = key, self.helper(value)

        return self.raw_data

    def helper(dict):
        dict = {
            'Hanzi' : dict['Hanzi'],
            'Pinyin' : convert_from_numerical_pinyin(dict['Pinyin']),
            'Information' : dict['Information']
        }
        return dict