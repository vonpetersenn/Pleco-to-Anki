from .Definition import Definition
from ..tones.numerical_pinyin_converter import convert_from_numerical_pinyin
from ..spoonfed.Spoonfed import Spoonfed

class Bookmark:

    def __init__(self, bookmarks_slice, configs):

        self.configs = configs

        self.hanzi = bookmarks_slice['Hanzi']

        self.pinyin_ugly = bookmarks_slice['Pinyin']
        self.pinyin_pretty = convert_from_numerical_pinyin(self.pinyin_ugly)
        if self.configs.reformat_pinyin:
            self.pinyin = self.pinyin_pretty
        else:
            self.pinyin = self.pinyin_ugly


        self.information = bookmarks_slice['Information']

        self.defi = Definition(self.information, self.configs)

        self.definition = self.defi.get_definition()
        self.examples = self.defi.get_example_sentences()

        self.spoonfed = ''
        if self.configs.spoonfed_examples:
            self.spoonfed = str(Spoonfed(self.hanzi, self.configs))

