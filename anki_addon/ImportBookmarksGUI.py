from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

import webbrowser
import requests

from anki_addon.Configuration import Configuration


class ImportBookmarksGUI(QDialog):
    def __init__(self, parent=None):
        super(ImportBookmarksGUI, self).__init__(parent)

        self.configs = Configuration()

        self.setWindowTitle("Import Pleco Bookmarks GUI")
        self.setWindowModality(Qt.ApplicationModal)

        self.checkboxPinyin = QCheckBox("Reformat Pinyin")
        self.checkboxPinyin.setChecked(self.configs.reformat_pinyin)

        self.checkboxKeywords = QCheckBox("Reformat Keywords")
        self.checkboxKeywords.setChecked(self.configs.reformat_keywords)

        self.checkboxReformatExamples = QCheckBox("Reformat Example Sentences")
        self.checkboxReformatExamples.setChecked(self.configs.reformat_example_sentences)

        self.checkboxGroupExamples = QCheckBox("Group Example Sentences")
        self.checkboxGroupExamples.setChecked(self.configs.group_example_sentences)

        self.select_dir_button = QPushButton("Select Bookmarks to Import")
        self.file_path = ""
        self.select_dir_button.clicked.connect(self.select_file)

        self.label_spoonfed = QLabel("Add Spoonfed examples?")
        self.group_spoonfed = QButtonGroup()
        self.radio_yes = QRadioButton("Yes")
        self.radio_no = QRadioButton("No")
        self.radio_no.setChecked(self.configs.spoonfed_examples)
        self.radio_yes.setChecked(not self.configs.spoonfed_examples)
        # Add radio buttons to the group
        self.group_spoonfed.addButton(self.radio_yes)
        self.group_spoonfed.addButton(self.radio_no)

        self.group_trad_or_simp = QButtonGroup()
        self.label_chars = QLabel("Select the type of chinese characters to use:")
        self.radio_trad = QRadioButton("Traditional")
        self.radio_simp = QRadioButton("Simplified")
        self.radio_trad.setChecked(self.configs.trad_or_simp == "trad")
        self.radio_simp.setChecked(self.configs.trad_or_simp == "simp")
        # Add radio buttons to the group
        self.group_trad_or_simp.addButton(self.radio_trad)
        self.group_trad_or_simp.addButton(self.radio_simp)

        self.more_options_button = QPushButton("More Options")
        self.more_options_button.clicked.connect(self.more_options_button_clicked)

        self.info_button = QPushButton("Info on Github-page")
        self.info_button.clicked.connect(self.info_button_clicked)

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.ok_button_clicked)

        ##############################
        # layout
        ##############################

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.more_options_button)
        button_layout.addWidget(self.info_button)

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.checkboxPinyin)
        main_layout.addWidget(self.checkboxKeywords)
        main_layout.addWidget(self.checkboxReformatExamples)
        main_layout.addWidget(self.checkboxGroupExamples)

        main_layout.addWidget(self.select_dir_button)

        main_layout.addWidget(self.label_chars)
        main_layout.addWidget(self.radio_trad)
        main_layout.addWidget(self.radio_simp)

        main_layout.addWidget(self.label_spoonfed)
        main_layout.addWidget(self.radio_yes)
        main_layout.addWidget(self.radio_no)

        main_layout.addLayout(button_layout)

        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def info_button_clicked(self):
        # URL of the website you want to open
        url = "https://github.com/vonpetersenn/pleco-to-anki"

        try:
            # Fetch the website's content
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Save the content to a temporary HTML file
                with open("temp.html", "wb") as f:
                    f.write(response.content)

                # Open the HTML file in the default web browser
                webbrowser.open("temp.html")
            else:
                print(f"Failed to fetch the website. Status code: {response.status_code}")

        except Exception as e:
            showInfo("github.com/vonpetersenn/pleco-to-anki")

    def more_options_button_clicked(self):
        showInfo(""
                 "For more options, please edit the configuration file directly.\n"
                 "Tools -> AddOns -> Pleco to Anki -> Config"
                 "")

    # TODO: Build config.json

    def select_file(self):
        self.file_path = QFileDialog.getOpenFileName(self, 'Select File')[0]
        if self.file_path:
            self.select_dir_button.setText(self.file_path)

    def update_checkbox_state(self):
        # Update the checkbox state when the dialog is shown
        self.checkboxPinyin.setChecked(mw.col.conf.get('addon_checkbox_state', False))
        self.checkboxKeywords.setChecked(mw.col.conf.get('addon_checkbox_state', False))
        self.checkboxReformatExamples.setChecked(mw.col.conf.get('addon_checkbox_state', False))
        self.checkboxGroupExamples.setChecked(mw.col.conf.get('addon_checkbox_state', False))

    def check_selected_file(self):
        if isinstance(self.file_path, str) and self.file_path.endswith(".txt"):
            return True
        else:
            showInfo("Please select a valid Pleco bookmark file. More info on Github-page.")
            return False

    def store_user_input_in_configs(self):
        self.configs.reformat_pinyin = self.checkboxPinyin.isChecked()
        self.configs.reformat_keywords = self.checkboxKeywords.isChecked()
        self.configs.reformat_example_sentences = self.checkboxReformatExamples.isChecked()
        self.configs.group_example_sentences = self.checkboxGroupExamples.isChecked()
        self.configs.file_name = self.file_path
        self.configs.spoonfed_examples = self.radio_yes.isChecked()
        self.configs.trad_or_simp = "trad" if self.radio_trad.isChecked() else "simp"

    def ok_button_clicked(self):
        self.store_user_input_in_configs()
        if self.check_selected_file():
            self.close()

    @staticmethod
    def config_from_user_input():
        dialog = ImportBookmarksGUI()
        dialog.exec_()
        return dialog.configs


#    def run_code(self):

#       showInfo(str(mw.col.note_count()))
#       showInfo(create_anki_cards(self.configs))