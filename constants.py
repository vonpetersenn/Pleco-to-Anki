from typing import Dict

FILE_NAME = 'plecodata.txt'
OUTPUT_FILE_NAME = 'output.csv'

#tone marks instead of numbers
REFORMAT_PINYIN = True

#replace keywords with html tags for improved readability (e.g. "verb" -> "<i style="color: grey;">v.</i>"), see below
REFORMAT_KEYWORDS = True

#add some html tags to the example sentences for improved readability
#also hide pinyin and translation behind the Chinese characters
REFORMAT_EXAMPLE_SENTENCES = True

#one field for definition, a second field for example sentences. Alternatively, set to False for having definition first
    #followed by the corresponding example sentences
GROUP_EXAMPLE_SENTENCES = True

#cross references within the Pleco dictionary are usually not useful and some of the only information/text
    #that we delete before exporting to Anki. However, if you want to keep them, set this to False
SUPRESS_CROSS_REFERENCES = True

SPOONFED_EXAMPLES = True
NUMBER_OF_SPOONS = 3
TRAD_OR_SIMP = 'simp' # 'trad' or 'simp'; example sentences will be in traditional or simplified characters

#right now, the headers are hard-coded in the Bookmarks class
ANKI_HEADERS = ['Hanzi', 'Pinyin', 'English', 'Example']
if SPOONFED_EXAMPLES:
    ANKI_HEADERS.append('Spoonfed')

