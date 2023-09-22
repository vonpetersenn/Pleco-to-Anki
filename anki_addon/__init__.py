from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

from .Configuration import Configuration

configs = Configuration()


class ImportBookmarksGUI(QDialog):
    def __init__(self, parent=None):
        super(ImportBookmarksGUI, self).__init__(parent)

        self.setWindowTitle("Import Pleco Bookmarks GUI")
        self.setWindowModality(Qt.ApplicationModal)

        self.layout = QVBoxLayout(self)

        self.checkboxPinyin = QCheckBox("Reformat Pinyin")
        self.checkboxPinyin.setChecked(configs.reformat_pinyin)
        self.layout.addWidget(self.checkboxPinyin)

        self.checkboxKeywords = QCheckBox("Reformat Keywords")
        self.checkboxKeywords.setChecked(configs.reformat_keywords)
        self.layout.addWidget(self.checkboxKeywords)

        self.checkboxReformatExamples = QCheckBox("Reformat Example Sentences")
        self.checkboxReformatExamples.setChecked(configs.reformat_example_sentences)
        self.layout.addWidget(self.checkboxReformatExamples)

        self.checkboxGroupExamples = QCheckBox("Group Example Sentences")
        self.checkboxGroupExamples.setChecked(configs.group_example_sentences)
        self.layout.addWidget(self.checkboxGroupExamples)

        self.select_dir_button = QPushButton("Select Bookmarks to Import")
        self.select_dir_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_dir_button)


        self.ok_button = QPushButton("Start Import")
        self.ok_button.clicked.connect(self.accept)

        self.layout.addWidget(self.ok_button)

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
    @staticmethod
    def show_checkbox_gui():
        dialog = ImportBookmarksGUI()
        dialog.exec_()
        if dialog.check_selected_file():
            dialog.store_user_input_in_configs()
            dialog.run_code()

    def run_code(self):
        showInfo(str(configs.reformat_pinyin)
                 + str(configs.reformat_keywords)
                 + str(configs.reformat_example_sentences)
                 + str(configs.group_example_sentences)
                 + str(configs.file_name)
                 )


# Function to add a menu item in the Tools menu
def add_checkbox_menu_item():
    action = QAction("Import Pleco Bookmarks", mw)
    action.triggered.connect(ImportBookmarksGUI.show_checkbox_gui)
    mw.form.menuTools.addAction(action)


# Initialize the checkbox menu item when Anki starts
add_checkbox_menu_item()
