
import pandas as pd
import time as time
import tqdm

spoonfed_chinese_pickle_directory_trad = 'spoonfed_chinese_trad.pickle'

spoonfed_df_trad = pd.read_pickle(spoonfed_chinese_pickle_directory_trad)

list_hanzi = spoonfed_df_trad['hanzi'].tolist()
print(list_hanzi[0:10])
list_pinyin = spoonfed_df_trad['pinyin'].tolist()
list_english = spoonfed_df_trad['english'].tolist()
list_soundfile = spoonfed_df_trad['soundfile'].tolist()

start = time.time()

for i in tqdm.tqdm(range(100)): #say big pleco file has 100 bookmarks
    word = '麻煩'
    counter = 0
    indices = []
    for index, sentence in enumerate(list_hanzi):
        if word in sentence:
            indices.append(index)
    print(indices)

end = time.time()

print('Runtime of Spoonfed lookups: checked ' + str(round(end - start, 1)) + 's')

