from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

from .Configuration import Configuration

configs = Configuration()

import webbrowser
import requests


class ImportBookmarksGUI(QDialog):
    def __init__(self, parent=None):
        super(ImportBookmarksGUI, self).__init__(parent)

        self.setWindowTitle("Import Pleco Bookmarks GUI")
        self.setWindowModality(Qt.ApplicationModal)


        self.checkboxPinyin = QCheckBox("Reformat Pinyin")
        self.checkboxPinyin.setChecked(configs.reformat_pinyin)

        self.checkboxKeywords = QCheckBox("Reformat Keywords")
        self.checkboxKeywords.setChecked(configs.reformat_keywords)

        self.checkboxReformatExamples = QCheckBox("Reformat Example Sentences")
        self.checkboxReformatExamples.setChecked(configs.reformat_example_sentences)

        self.checkboxGroupExamples = QCheckBox("Group Example Sentences")
        self.checkboxGroupExamples.setChecked(configs.group_example_sentences)

        self.select_dir_button = QPushButton("Select Bookmarks to Import")
        self.file_path = ""
        self.select_dir_button.clicked.connect(self.select_file)

        self.label_spoonfed = QLabel("Add Spoonfed examples?")
        self.group_spoonfed = QButtonGroup()
        self.radio_yes = QRadioButton("Yes")
        self.radio_no = QRadioButton("No")
        self.radio_no.setChecked(configs.spoonfed_examples)
        self.radio_yes.setChecked(not configs.spoonfed_examples)
        # Add radio buttons to the group
        self.group_spoonfed.addButton(self.radio_yes)
        self.group_spoonfed.addButton(self.radio_no)

        self.group_trad_or_simp = QButtonGroup()
        self.label_chars = QLabel("Select the type of chinese characters to use:")
        self.radio_trad = QRadioButton("Traditional")
        self.radio_simp = QRadioButton("Simplified")
        self.radio_trad.setChecked(configs.trad_or_simp == "trad")
        self.radio_simp.setChecked(configs.trad_or_simp == "simp")
        # Add radio buttons to the group
        self.group_trad_or_simp.addButton(self.radio_trad)
        self.group_trad_or_simp.addButton(self.radio_simp)

        self.more_options_button = QPushButton("More Options")
        self.more_options_button.clicked.connect(self.more_options_button_clicked)

        self.info_button = QPushButton("Info on Github-page")
        self.info_button.clicked.connect(self.info_button_clicked)

        self.ok_button = QPushButton("Ok")
        self.ok_button.clicked.connect(self.ok_button_clicked)


        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.checkboxPinyin)
        self.layout.addWidget(self.checkboxKeywords)
        self.layout.addWidget(self.checkboxReformatExamples)
        self.layout.addWidget(self.checkboxGroupExamples)

        self.layout.addWidget(self.select_dir_button)

        self.layout.addWidget(self.label_chars)
        self.layout.addWidget(self.radio_trad)
        self.layout.addWidget(self.radio_simp)

        self.layout.addWidget(self.label_spoonfed)
        self.layout.addWidget(self.radio_yes)
        self.layout.addWidget(self.radio_no)

        self.layout.addWidget(self.more_options_button)

        self.layout.addWidget(self.info_button)

        self.layout.addWidget(self.ok_button)


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
    #TODO: Build config.json

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
            showInfo("Please select a valid Pleco bookmark file, that ends with '.txt'")
            return False

    def store_user_input_in_configs(self):
        configs.reformat_pinyin = self.checkboxPinyin.isChecked()
        configs.reformat_keywords = self.checkboxKeywords.isChecked()
        configs.reformat_example_sentences = self.checkboxReformatExamples.isChecked()
        configs.group_example_sentences = self.checkboxGroupExamples.isChecked()
        configs.file_name = self.file_path
        configs.spoonfed_examples = self.radio_yes.isChecked()
        configs.trad_or_simp = "trad" if self.radio_trad.isChecked() else "simp"

    def ok_button_clicked(self):
        self.store_user_input_in_configs()
        if self.check_selected_file():
            self.run_code()
            self.close()

    @staticmethod
    def show_checkbox_gui():
        dialog = ImportBookmarksGUI()
        dialog.exec_()

    def run_code(self):
        showInfo(str(configs.reformat_pinyin)
                 + str(configs.reformat_keywords)
                 + str(configs.reformat_example_sentences)
                 + str(configs.group_example_sentences)
                 + str(configs.file_name)
                 + str(configs.spoonfed_examples)
                 + str(configs.trad_or_simp)
                 )


# Function to add a menu item in the Tools menu
def add_checkbox_menu_item():
    action = QAction("Import Pleco Bookmarks", mw)
    action.triggered.connect(ImportBookmarksGUI.show_checkbox_gui)
    mw.form.menuTools.addAction(action)


# Initialize the checkbox menu item when Anki starts
add_checkbox_menu_item()
