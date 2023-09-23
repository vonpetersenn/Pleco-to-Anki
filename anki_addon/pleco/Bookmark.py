from .Definition import Definition
from ..tones.numerical_pinyin_converter import convert_from_numerical_pinyin

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

        self.def_exmpl = Definition(self.information, self.configs)

        self.definiton = self.def_exmpl.get_definition()
        self.examples = self.def_exmpl.get_example_sentences()

        self.spoonfed = ''

