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

        self.checkbox = QCheckBox("Reformat Pinyin")
        self.layout.addWidget(self.checkbox)
        self.checkbox.setChecked(configs.reformat_pinyin)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        self.layout.addWidget(self.ok_button)

    def update_checkbox_state(self):
        # Update the checkbox state when the dialog is shown
        self.checkbox.setChecked(mw.col.conf.get('addon_checkbox_state', False))

    def store_checkbox_state_in_configs(self):
        if not self.checkbox.isChecked():
            configs.reformat_pinyin = False
        else:
            configs.reformat_pinyin = True

    @staticmethod
    def show_checkbox_gui():
        dialog = ImportBookmarksGUI()
        dialog.exec_()
        dialog.store_checkbox_state_in_configs()
        dialog.run_code()

    def run_code(self):
        if configs.reformat_pinyin:
            showInfo("Will reformat pinyin.")
        else:
            showInfo("Will not reformat pinyin.")


# Function to add a menu item in the Tools menu
def add_checkbox_menu_item():
    action = QAction("Import Pleco Bookmarks", mw)
    action.triggered.connect(ImportBookmarksGUI.show_checkbox_gui)
    mw.form.menuTools.addAction(action)

# Initialize the checkbox menu item when Anki starts
add_checkbox_menu_item()