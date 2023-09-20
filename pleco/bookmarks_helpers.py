from constants import *
import pandas as pd
import unicodedata
from tones.numerical_pinyin_converter import convert_from_numerical_pinyin
from pleco.pinyin_exceptions import PINYIN_EXCEPTIONAL_CASES
from pleco.keyword_replacements import KEYWORD_REPLACEMENTS

def load_pleco_file(file_name=FILE_NAME):
    column_names = ['Hanzi', 'Pinyin', 'Information']
    df = pd.read_csv(file_name, sep='\t', names=column_names)
    print('Importing Pleco Bookmarks from ' + file_name + '...')
    return df


# Define the preprocess function
def preprocess(slice):
    hanzi = slice['Hanzi']
    pinyin = slice['Pinyin']
    information = slice['Information']


    if type(hanzi) == str and len(hanzi.split('//')) > 1:
        print('Information on folders in the Pleco bookmarks will be ignored. Skipping row ' + hanzi + '...')
        new_slice = pd.Series(['', '', ''], index=['Hanzi', 'Pinyin', 'Information'])
        return new_slice

    if type(hanzi) == str and len(hanzi.split('[')) > 1:
        raise Warning('"[" found. It seems, that the "Character set" '
                      'option in the Pleco export settings is set to "Both" which is not supported. '
                      'Please chose "Simplified" or "Traditional".')

    if type(hanzi) != str or type(pinyin) != str:
        print('Found bookmark that does not contain a Chinese character or does not contain pinyin. Skipping...')
        try:
            print('Hanzi: ' + hanzi)
        except:
            pass
        new_slice = pd.Series(['', '', ''], index=['Hanzi', 'Pinyin', 'Information'])
        return new_slice

    if not is_pinyin(convert_from_numerical_pinyin(pinyin)):
        print(
            'Found bookmark that does not contain valid pinyin. Check bookmark file at word ' + hanzi + ' for errors.')
        new_slice = pd.Series(['', '', ''], index=['Hanzi', 'Pinyin', 'Information'])
        return new_slice

    new_slice = pd.Series([hanzi, pinyin, information], index=['Hanzi', 'Pinyin', 'Information'])
    return new_slice


###############


def is_keyword(word : str) -> bool:
    if word in KEYWORD_REPLACEMENTS.keys():
        return True
    else:
        return False

def is_chinese(text : str) -> bool:
    for char in text:
        if 'CJK' in unicodedata.name(char, ''):
            return True
    return False

def is_pinyin(text : str) -> bool:
    normalized_text = unicodedata.normalize('NFD', text)
    for char in normalized_text:
        if unicodedata.combining(char):
            return True
        elif text in PINYIN_EXCEPTIONAL_CASES:
            return True
    return False

def is_number(text: str) -> bool:
    try:
        float(text)  # Try to convert the string to a float
        return True
    except ValueError:
        return False
