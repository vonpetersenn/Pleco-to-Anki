def create_anki_cards(configs = "configs"):

    nice_string = ""

    nice_string += "Reformat pinyin: " + str(configs.reformat_pinyin) + "\n"
    nice_string += "Reformat keywords: " + str(configs.reformat_keywords) + "\n"
    nice_string += "Reformat example sentences: " + str(configs.reformat_example_sentences) + "\n"
    nice_string += "Group example sentences: " + str(configs.group_example_sentences) + "\n"
    nice_string += "File name: " + str(configs.file_name) + "\n"
    nice_string += "Spoonfed examples: " + str(configs.spoonfed_examples) + "\n"
    nice_string += "Traditional or simplified: " + str(configs.trad_or_simp) + "\n"



    return nice_string