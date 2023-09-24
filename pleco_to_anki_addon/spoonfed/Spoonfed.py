import random

from .spoonfed_simp import SPOONFED_SIMP #path for Addon
#from spoonfed_simp import SPOONFED_SIMP #path for testing
spoonfed_simp = SPOONFED_SIMP
from .spoonfed_trad import SPOONFED_TRAD
#from spoonfed_trad import SPOONFED_TRAD
spoonfed_trad = SPOONFED_TRAD

class Spoonfed:
    def __init__(self, word, configs):

        self.configs = configs

        if type(word) != str:
            raise TypeError('Argument of spoonfed object must be a string not a ' + str(type(hanzi)))

        self.word = word

        if self.configs.trad_or_simp == 'trad':
            self.dataset = spoonfed_trad
        elif self.configs.trad_or_simp == 'simp':
            self.dataset = spoonfed_simp
        else:
            raise ValueError('TRAD_OR_SIMP must be either "trad" or "simp"')

        self.spoons = get_spoons(self.dataset, self.word)[0:self.configs.number_of_spoons]

        self.example_sentences = []
        for spoon in self.spoons:
            self.example_sentences.append(pretty_example_sentence(spoon))

    def __str__(self):
        string = ''
        return '<br><br>'.join(self.example_sentences)

def pretty_example_sentence(spoon : list) -> str:
    hanzi = spoon[0]
    pinyin = spoon[1]
    english = spoon[2]
    soundfile = spoon[3]

    string = ''
    string += '<details><summary><big>'
    string += hanzi
    string += '</big></summary>' + '<small>'
    string += pinyin
    string += '<br></small>'
    string += english
    string += '<br></details>'
    string += soundfile

    return string

def get_spoons(dataset, word):

    indices = word_in_sentence(dataset, word)
    indices = random.sample(indices, len(indices))

    spoons = []
    for index in indices:
        spoons.append(spoon(dataset, index))

    return spoons

def spoon(dataset : list, index : int) -> list:
    hanzi = dataset[0][index]
    pinyin = dataset[1][index]
    english = dataset[2][index]
    soundfile = dataset[3][index]
    return [hanzi, pinyin, english, soundfile]

def word_in_sentence(dataset : list, word : str) -> list:
    indices = []
    sentences = dataset[0]
    for index, sentence in enumerate(sentences):
        if word in sentence:
            indices.append(index)
    return indices