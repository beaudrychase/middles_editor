import json
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_middles_main import Ui_MainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open("test.json", 'r') as f:
            self.input = json.load(f)
        self.read_entry_data(0)
        self.show()

    def read_entry_data(self, index):
        # I want this to set all of the fields to show the data.
        entry = self.input['results'][index]
        self.ui.groupBox.setTitle("Middle {0}/{1}".format(index, self.input["sentence_number"]))
        self.ui.sentence_label.setText(entry['sentence'])
        self.ui.subject_line_edit.setText(entry["middles"][0]["subject"]["word"])
        self.ui.subject_spin_box.setValue(entry["middles"][0]["subject"]["index"])
        self.ui.verb_line_edit.setText(entry["middles"][0]["verb"]["word"])
        self.ui.verb_spin_box.setValue(entry["middles"][0]["verb"]["index"])
        self.ui.adverb_line_edit.setText(entry["middles"][0]["adverb"]["word"])
        self.ui.adverb_spin_box.setValue(entry["middles"][0]["adverb"]["index"])


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
