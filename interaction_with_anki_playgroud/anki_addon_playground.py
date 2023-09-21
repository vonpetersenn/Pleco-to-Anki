import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel, QButtonGroup,\
    QFileDialog, QCheckBox, QSpinBox

#TODO: Force user to select good txt file. otherwise throw error. right now it just crashes if nothing is selected
#TODO: Close Window after applying changes

class AnkiGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.TradOrSimp = "Trad"  # Default selection
        self.spoonfed_selection = "No"  # Default selection
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.features_label = QLabel("Features")


        # Create checkboxes and add them to the layout
        self.checkboxPinyin = QCheckBox("Reformat Pinyin")
        self.checkboxKeywords = QCheckBox("Reformat Keywords")
        self.checkboxReformatExamples = QCheckBox("Reformat Example Sentences")
        self.checkboxGroupExamples = QCheckBox("Group Example Sentences")


        # Set the checkboxes to be checked by default
        self.checkboxPinyin.setChecked(True)
        self.checkboxKeywords.setChecked(True)
        self.checkboxReformatExamples.setChecked(True)
        self.checkboxGroupExamples.setChecked(True)


        # Button to select the file
        self.select_dir_button = QPushButton("Select Bookmarks to Import")
        self.select_dir_button.clicked.connect(self.select_file)

        # Spoonfed yes or no
        self.label_spoonfed = QLabel("Add Spoonfed examples?")

        self.group_spoonfed = QButtonGroup()

        self.radio_yes = QRadioButton("Yes")
        self.radio_no = QRadioButton("No")

        # Set the default selection
        self.radio_no.setChecked(True)

        # Add radio buttons to the group
        self.group_spoonfed.addButton(self.radio_yes)
        self.group_spoonfed.addButton(self.radio_no)

        # Radio buttons for Trad and Simp
        self.label_chars = QLabel("Select the type of chinese characters to use:")

        self.group_chars = QButtonGroup()

        self.radio_trad = QRadioButton("Traditional")
        self.radio_simp = QRadioButton("Simplified")

        # Set the default selection
        self.radio_trad.setChecked(True)

        # Add radio buttons to the group
        self.group_chars.addButton(self.radio_trad)
        self.group_chars.addButton(self.radio_simp)

        # Number selector (spin box)
        self.label_number = QLabel("Maximum number of spoonfed examples to add:")
        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(1)  # Set the minimum value
        self.spin_box.setMaximum(10)  # Set the maximum value
        self.spin_box.setValue(3)  # Set the default value

        self.label_explanation = QLabel("Manual on \n github.com/vonpetersenn/Pleco-to-Anki")


        self.label_explanation.setWordWrap(True)

        self.label_explanation.setStyleSheet("QLabel {font-size: 15px;}")

        self.label_explanation.setFixedWidth(400)

        layout.addWidget(self.label_explanation)
        layout.addWidget(self.features_label)
        layout.addWidget(self.checkboxPinyin)
        layout.addWidget(self.checkboxKeywords)
        layout.addWidget(self.checkboxReformatExamples)
        layout.addWidget(self.checkboxGroupExamples)

        layout.addWidget(self.select_dir_button)

        layout.addWidget(self.label_spoonfed)
        layout.addWidget(self.radio_yes)
        layout.addWidget(self.radio_no)

        layout.addWidget(self.label_chars)
        layout.addWidget(self.radio_trad)
        layout.addWidget(self.radio_simp)

        layout.addWidget(self.label_number)
        layout.addWidget(self.spin_box)


        # Button to apply the selection
        apply_button = QPushButton("Import Bookmarks Now")
        apply_button.clicked.connect(self.apply_selection)
        layout.addWidget(apply_button)

        self.setLayout(layout)
        self.setWindowTitle("Import Pleco Bookmarks")



    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        directory, _ = QFileDialog.getOpenFileName()
        self.directory = directory
        return self.directory

    def checkbox_state_changed(self, state):
        if self.checkboxPinyin.isChecked():
            print("Option 1 is checked.")
        else:
            print("Option 1 is unchecked.")

        if self.checkboxKeywords.isChecked():
            print("Option 2 is checked.")
        else:
            print("Option 2 is unchecked.")

    def apply_selection(self):
        # This function can be used to perform some action based on the selected options
        print(f"Selected TradOrSimp option: {self.group_chars.checkedButton().text()}")
        print(f"Selected Spoonfed option: {self.group_spoonfed.checkedButton().text()}")
        print(f"Selected directory: {self.directory}")
        print(f"Selected Reformat Pinyin: {self.checkboxPinyin.isChecked()}")
        print(f"Selected Reformat Keywords: {self.checkboxKeywords.isChecked()}")
        print(f"Selected Reformat Example Sentences: {self.checkboxReformatExamples.isChecked()}")
        print(f"Selected Group Example Sentences: {self.checkboxGroupExamples.isChecked()}")
        print(f"Selected number of spoonfed examples: {self.spin_box.value()}")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnkiGUI()
    window.show()
    sys.exit(app.exec_())
