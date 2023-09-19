import pandas as pd
from spoonfed.spoonfed_helpers import *
from tqdm import tqdm

spoonfed_chinese_pickle_directory = 'spoonfed\spoonfed_chinese_trad.pickle'

spoonfed_df = pd.read_pickle(spoonfed_chinese_pickle_directory)

tqdm.pandas()
spoonfed_df_simp = spoonfed_df.copy()
spoonfed_df_simp['hanzi'] = spoonfed_df_simp['hanzi'].progress_apply(trad_to_simp)


file_path = 'spoonfed/spoonfed_chinese_simp.pickle'
spoonfed_df_simp.to_pickle(file_path)

print(f'DataFrame saved to {file_path}')

print(spoonfed_df_simp.head())