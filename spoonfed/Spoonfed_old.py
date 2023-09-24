from constants import NUMBER_OF_SPOONS, TRAD_OR_SIMP

from spoonfed.spoonfed_helpers import *



spoonfed_chinese_pickle_directory_simp = 'spoonfed\spoonfed_chinese_simp.pickle'
spoonfed_chinese_pickle_directory_trad = 'spoonfed\spoonfed_chinese_trad.pickle'

# simp: simplified characters
# trad: traditional characters

class Spoonfed:
    def __init__(self, hanzi):

        if type(hanzi) != str:
            raise TypeError('Argument of spoonfed object must be a string not a ' + str(type(hanzi)))

        self.number_of_spoons = NUMBER_OF_SPOONS

        self.spoonfed_df_simp = pd.read_pickle(spoonfed_chinese_pickle_directory_simp)
        self.spoonfed_df_trad = pd.read_pickle(spoonfed_chinese_pickle_directory_trad)

        self.hanzi = hanzi

        if TRAD_OR_SIMP == 'trad':
            self.hanzi_trad = hanzi
            self.hanzi_simp = trad_to_simp(hanzi)
        elif TRAD_OR_SIMP == 'simp':
            self.hanzi_trad = simp_to_trad(hanzi)
            self.hanzi_simp = hanzi
        else:
            raise ValueError('TRAD_OR_SIMP must be either "trad" or "simp"')

    def get_spoonfed_sentences(self):
        if TRAD_OR_SIMP == 'trad':
            string = get_spoonfed_sentences(self.spoonfed_df_trad, self.hanzi_trad, self.number_of_spoons)
        elif TRAD_OR_SIMP == 'simp':
            string = get_spoonfed_sentences(self.spoonfed_df_simp, self.hanzi_simp, self.number_of_spoons)
        else:
            raise ValueError('TRAD_OR_SIMP must be either "trad" or "simp"')
        return string

########################################################################################################################

