class Configuration:
    def __init__(self):
        self.variable = ""
        self.file_name = ""
        self.output_file_name = ""

        self.reformat_pinyin = True
        self.reformat_keywords = True

        self.reformat_example_sentences = True
        self.group_example_sentences = True
        self.supress_cross_references = True

        self.spoonfed_examples = True
        self.number_of_spoons = 3

        self.trad_or_simp = 'trad'

    def __str__(self):
        return self.variable

    def read_config_from_JSON(self):
        pass