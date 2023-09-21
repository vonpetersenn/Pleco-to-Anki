from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo

##TODO: Refactor anki_addon_playground into this atomic structure

# Function to handle the checkbox state
def on_checkbox_state_changed(state):
    if state == Qt.Checked:
        mw.col.conf['addon_checkbox_state'] = True
    else:
        mw.col.conf['addon_checkbox_state'] = False

# Function to create and show the GUI
def show_checkbox_gui():
    # Create a QDialog
    dialog = QDialog(mw)

    # Set dialog properties
    dialog.setWindowTitle("Checkbox GUI")
    dialog.setWindowModality(Qt.ApplicationModal)

    # Create a QVBoxLayout for the dialog
    layout = QVBoxLayout(dialog)

    # Create a checkbox
    checkbox = QCheckBox("Check this box")
    checkbox.stateChanged.connect(on_checkbox_state_changed)

    # Add the checkbox to the layout
    layout.addWidget(checkbox)

    # Create an "OK" button
    ok_button = QPushButton("OK")
    ok_button.clicked.connect(dialog.accept)

    # Add the "OK" button to the layout
    layout.addWidget(ok_button)

    # Show the dialog
    dialog.exec_()

# Function to add a menu item in the Tools menu
def add_checkbox_menu_item():
    action = QAction("Checkbox GUI", mw)
    action.triggered.connect(show_checkbox_gui)
    mw.form.menuTools.addAction(action)

# Initialize the checkbox menu item when Anki starts
add_checkbox_menu_item()
