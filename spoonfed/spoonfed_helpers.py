import opencc
import pandas as pd
import numpy as np

def get_spoonfed_sentences(spoonfed_df, hanzi : str, number_of_spoons : int) -> str:

    indices : list = indices_of_spoons(spoonfed_df, hanzi, number_of_spoons)

    if len(indices) == 0:
        return ''

    selected_data = pd.Series(indices)
    sentences = selected_data.apply(lambda x: build_pretty_string(spoonfed_df, x))

    sentences_string = '<br><br>'.join(sentences)

    return sentences_string

def indices_of_spoons(spoonfed_df, word, number_of_spoons):
    #logical pd series
    contains_substring = spoonfed_df['hanzi'].str.contains(word, regex=False)

    if contains_substring.sum() == 0:
        return []

    # Get the indices of examples that contain the substring
    indices = np.arange(len(spoonfed_df))[contains_substring]

    indices = np.random.permutation(indices)

    indices = indices[:number_of_spoons]

    return indices

def build_pretty_string(spoonfed_df, index):
    string = '<details><summary><big>' \
             + spoonfed_df.iloc[index]['hanzi'] \
             + '</big></summary>' + '<small>' \
             + spoonfed_df.iloc[index]['pinyin'] \
             + '<br>' + '</small>' \
             + spoonfed_df.iloc[index]['english'] \
             + '<br></details>' \
             + spoonfed_df.iloc[index]['soundfile']
    return string

def trad_to_simp(hanzi):
    try:
        # Create an OpenCC converter instance for traditional to simplified conversion
        converter = opencc.OpenCC("t2s")
        simplified_text = converter.convert(hanzi)
        return simplified_text
    except Exception as e:
        return f"Error: {str(e)}"

def simp_to_trad(hanzi):
    try:
        # Create an OpenCC converter instance for simplified to traditional conversion
        converter = opencc.OpenCC("s2t")
        traditional_text = converter.convert(hanzi)
        return traditional_text
    except Exception as e:
        return f"Error: {str(e)}"