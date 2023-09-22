from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

##TODO: Refactor anki_addon_playground into this atomic structure


class CheckboxGUI(QDialog):
    def __init__(self, parent=None):
        super(CheckboxGUI, self).__init__(parent)

        self.setWindowTitle("Checkbox GUI")
        self.setWindowModality(Qt.ApplicationModal)

        self.layout = QVBoxLayout(self)

        self.checkbox = QCheckBox("Check this box")
        self.layout.addWidget(self.checkbox)


        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        self.layout.addWidget(self.ok_button)

    def update_checkbox_state(self):
        # Update the checkbox state when the dialog is shown
        self.checkbox.setChecked(mw.col.conf.get('addon_checkbox_state', False))

    def show_checkbox_state(self):
        if self.checkbox.isChecked():
            showInfo("Checkbox is checked.")
        elif not self.checkbox.isChecked():
            showInfo("Checkbox is not checked")
        else:
            showInfo("Checkbox is in an unknown state")

    @staticmethod
    def show_checkbox_gui():
        dialog = CheckboxGUI()
        dialog.exec_()
        dialog.show_checkbox_state()
        if dialog.checkbox.isChecked():
            dialog.run_code()

    def run_code(self):
        showInfo("Instead of showing a message box, we could run the code here.")


# Function to add a menu item in the Tools menu
def add_checkbox_menu_item():
    action = QAction("Import Pleco Bookmarks", mw)
    action.triggered.connect(CheckboxGUI.show_checkbox_gui)
    mw.form.menuTools.addAction(action)

# Initialize the checkbox menu item when Anki starts
add_checkbox_menu_item()