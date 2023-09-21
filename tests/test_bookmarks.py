import unittest
from pleco.Bookmarks import Bookmarks # Use relative import
import time
import pandas as pd


#run the following command in the terminal in the project root directory to run the tests:
#python -m unittest test.test_bookmarks

#TODO: different test. the spoonfed method is not deterministic, so it will be hard to test.
#      we can test for empty and non-empty results, but not for the exact results
#       we can also test for definition and example sentences exactly
#TODO: Make sure to keek the test_file1_output.txt file up to date with the expected output when improving the
#      Bookmarks class

def test_bookmarks(test_file_path):
    bookmarks1 = Bookmarks(test_file_path)  # Use the provided file path
    bookmarks1.reformat_pinyin()
    bookmarks1.build_english_and_definition_fields()
    print('Adding Spoonfed examples...')
    start_time = time.time()
    bookmarks1.add_spoonfed_sentences()
    end_time = time.time()
    print('Runtime of Spoonfed lookups: ' + str(round(end_time - start_time, 1)) + 's')
    return bookmarks1.anki_notes


def load_example_output(file_name):
    column_names = ['Hanzi', 'Pinyin', 'English', 'Example', 'Spoonfed']
    df = pd.read_csv(file_name, sep='|', names=column_names)
    print('Importing Pleco Bookmarks from ' + file_name + '...')
    return df


class TestBookmarks(unittest.TestCase):
    def test_bookmarks_output(self):
        # Define the expected output as a DataFrame
        expected_output = load_example_output('tests/test_output1.txt')

        # Get the actual output as a DataFrame
        actual_output = test_bookmarks('tests/test_input1.txt')

        # Compare the DataFrames for equality
        self.assertTrue(expected_output.equals(actual_output))
