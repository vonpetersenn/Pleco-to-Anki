class Configuration:
    def __init__(self):

        self.run_code = False

        self.file_name = "/pleco_to_anki/exampledata.txt"
        self.output_file_name = ""

        self.reformat_pinyin = True
        self.reformat_keywords = True

        self.reformat_example_sentences = True
        self.group_example_sentences = True
        self.supress_cross_references = True

        self.reformat_keywords = True

        self.spoonfed_examples = True
        self.number_of_spoons = 2
        self.reformat_spoonfed_examples = self.reformat_example_sentences
        self.trad_or_simp = 'trad'

    def read_config_from_JSON(self):
        pass