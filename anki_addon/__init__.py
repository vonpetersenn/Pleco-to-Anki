from aqt import mw
from aqt.qt import *


# Import the GUI
# In GUI user sets options and runs create_anki_cards.py
from .ImportBookmarkGUI import ImportBookmarksGUI

# Function to add a menu item in the Tools menu
def add_checkbox_menu_item():
    action = QAction("Import Pleco Bookmarks", mw)
    action.triggered.connect(ImportBookmarksGUI.show_checkbox_gui)
    mw.form.menuTools.addAction(action)


# Initialize the checkbox menu item when Anki starts
add_checkbox_menu_item()
