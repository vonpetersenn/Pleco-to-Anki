from pleco.Bookmarks import Bookmarks
from constants import *
from pleco.Definition import Definition
from pleco.definition_helpers import *
from spoonfed.spoonfed_helpers import *

import time


def main():

    bookmarks = Bookmarks(FILE_NAME)

    if REFORMAT_PINYIN:
        bookmarks.reformat_pinyin()

    bookmarks.build_english_and_definition_fields()

    if SPOONFED_EXAMPLES:
        print('Adding Spoonfed examples...')
        start_time = time.time()
        bookmarks.add_spoonfed_sentences()
        end_time = time.time()
        print('Runtime of Spoonfed lookups: ' + str(round(end_time - start_time, 1)) + 's')

    bookmarks.export_to_csv()

    #information = bookmarks.raw_data['Information'][21]
    #print(Definition(information).segments)
    #print(Definition(information).raw_information)
    #print(split_text(information))
    #print(join_keyword_with_english_segments(split_text(information), ['english']))
   # print(do_minor_reformatting(split_text(information), ['english']))
   # print(group_example_sentences(split_text(information), ['english']))


    #print(bookmarks.anki_notes)

   # defintion = "noun 1 bubble 冒泡兒 màopàor bubble; bubble up 肥皂泡兒 féizàopàor soap bubbles 2 sth. shaped like a bubble 手上起了泡 shǒushang qǐ le pào get (or raise) blisters on one’s palm  verb 1 steep; soak 泡腳 pàojiǎo soak one’s feet in water 把種子放在溫水裡泡一下 bǎ zhǒngzi fàng zài wēnshuǐ lǐ pào yīxià steep the seeds in lukewarm water 2 pour boiling water into (tea, instant soup, etc.) 泡方便麵 pào fāngbiànmiàn make instant noodles 3 dawdle; dally; hang about 別泡時間了, 快把工作做完！ Bié pào shíjiān le, kuài bǎ gōngzuò zuò wán! Stop dawdling and finish your work! 4 colloquial (of a male) play the field; fool around with a female 想泡我妹妹, 做夢！ xiǎng pào wǒ mèimei, zuòmèng! How dare you dream of fooling around with my sister!"
    #found_example_sentences = Definition(defintion).get_example_sentences()
   # print(found_example_sentences)

    print(trad_to_simp('這個是繁體字'))
    print(simp_to_trad('这个是简体字'))

if __name__ == "__main__":
    main()