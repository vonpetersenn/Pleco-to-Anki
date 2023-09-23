import unittest
from pleco.Bookmarks_old import Definition
import time
import pandas as pd

#run the following command in the terminal in the project root directory to run the tests:
#python -m unittest tests.test_Definition

def test_Definition_definition(test_file_path):
    definition = Definition(test_file_path)

    return definition.get_definition()

def test_Definition_example_sentences(test_file_path):
    definition = Definition(test_file_path)

    return definition.get_example_sentences()

def load_example_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
    return file_content

def test_Another_Definition_output(self):
    expected_output_definition = load_example_file('tests/test_Definition_output_definition_2.txt')
    expected_output_example_sentences = load_example_file('tests/test_Definition_output_example_sentences_2.txt')

    self.assertTrue(test_Definition_definition(
        load_example_file('tests/test_Definition_input_2.txt')) == expected_output_definition)
    self.assertTrue(test_Definition_example_sentences(
        load_example_file('tests/test_Definition_input_2.txt')) == expected_output_example_sentences)


class TestBookmarks(unittest.TestCase):
    def test_Definition_output(self):
        expected_output_definition = load_example_file('tests/test_Definition_output_definition_1.txt')
        expected_output_example_sentences = load_example_file('tests/test_Definition_output_example_sentences_1.txt')

        self.assertTrue(test_Definition_definition(load_example_file('tests/test_Definition_input_1.txt')) == expected_output_definition)
        self.assertTrue(test_Definition_example_sentences(load_example_file('tests/test_Definition_input_1.txt')) == expected_output_example_sentences)

    def test_Another_Definition_output(self):
        expected_output_definition = load_example_file('tests/test_Definition_output_definition_2.txt')
        expected_output_example_sentences = load_example_file('tests/test_Definition_output_example_sentences_2.txt')

        self.assertTrue(test_Definition_definition(load_example_file('tests/test_Definition_input_2.txt')) == expected_output_definition)
        self.assertTrue(test_Definition_example_sentences(load_example_file('tests/test_Definition_input_2.txt')) == expected_output_example_sentences)