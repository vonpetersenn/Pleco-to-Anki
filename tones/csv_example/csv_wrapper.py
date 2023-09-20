# Add parent directory with numerical_pinyin_converter.py to path
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from numerical_pinyin_converter import convert_from_numerical_pinyin
import csv

# Open desired file, in this case hsk_level_6.csv
with open('hsk_level_6.csv', encoding ="utf8") as fh:
  reader = csv.DictReader(fh)
  new_word_list = []
  for row in reader:
    
    # Run pinyin converter function on each value for the Pronunciation key
    row['Pronunciation'] = convert_from_numerical_pinyin(row['Pronunciation'])
    new_word_list.append(row)

# Create and write new file, in this case called hsk_level_6_modified.csv
with open('hsk_level_6_modified.csv', 'w', newline='', encoding ="utf8") as fh:
  fieldnames = list(new_word_list[0].keys())
  writer = csv.DictWriter(fh, fieldnames=fieldnames)
  writer.writeheader()
  
  for row in new_word_list:
    writer.writerow(row)
