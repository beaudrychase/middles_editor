import datetime
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
        self.output = self.create_output_json("test.json")
        self.entry_index = 0
        self.read_entry_data(self.entry_index)
        # self.ui.is_middle_button.clicked.connect(self.status_label.update)
        # self.ui.is_not_middle_button.clicked.connect(self.status_label.update)
        # self.ui.reset_entry_button.clicked.connect(self.status_label.update)

        self.ui.next_button.clicked.connect(self.next_entry)
        self.ui.previous_button.clicked.connect(self.previous_entry)
        self.show()

    # Creates the initial state for the output json and fills in the fields that need to be initialized.
    def create_output_json(self, input_file_name):
        output_json = {}
        # the time this program was run
        now = datetime.datetime.now()
        output_json["time_created"] = now.strftime("%Y/%m/%d %H:%M")
        # the time the input file was created
        output_json["source_time_created"] = self.input["time_created"]

        output_json["source_file_name"] = input_file_name
        output_json["results"] = list()
        output_json["complete"] = False
        output_json["sentences_status"] = [False] * len(self.input["results"])
        return output_json

    # Prepares the form for a new middle by enabling and disabling things. Doesn't display the middle
    def prepare_for_new_entry(self):
        self.ui.is_middle_button.setEnabled(True)
        self.ui.is_not_middle_button.setEnabled(True)

        #all of the widgets for editing the middle.
        self.ui.reset_entry_button.setEnabled(False)
        self.ui.note_editor.setEnabled(False)
        self.ui.which_middle_spin_box.setEnabled(False)
        self.ui.add_middle_button.setEnabled(False)
        self.ui.remove_middle_button.setEnabled(False)
        self.ui.subject_line_edit.setEnabled(False)
        self.ui.subject_spin_box.setEnabled(False)
        self.ui.verb_line_edit.setEnabled(False)
        self.ui.verb_spin_box.setEnabled(False)
        self.ui.adverb_line_edit.setEnabled(False)
        self.ui.adverb_spin_box.setEnabled(False)

    # Displays a entry.
    def read_entry_data(self, index):
        # I want this to set all of the fields to show the data.
        #TODO make this read in the values from the input file.
        entry = self.input['results'][index]
        self.ui.groupBox.setTitle("Middle {0}/{1}".format(index, self.input["sentence_number"] - 1))
        self.ui.note_editor.setPlainText(entry["middles"][0]["note"])
        self.ui.status_label.setText("unaccounted for")
        self.ui.sentence_label.setText(entry['sentence'])
        self.ui.subject_line_edit.setText(entry["middles"][0]["subject"]["word"])
        self.ui.subject_spin_box.setValue(entry["middles"][0]["subject"]["index"])
        self.ui.verb_line_edit.setText(entry["middles"][0]["verb"]["word"])
        self.ui.verb_spin_box.setValue(entry["middles"][0]["verb"]["index"])
        self.ui.adverb_line_edit.setText(entry["middles"][0]["adverb"]["word"])
        self.ui.adverb_spin_box.setValue(entry["middles"][0]["adverb"]["index"])

    def next_entry(self):
        if self.entry_index < len(self.input["results"]) - 1:
            self.entry_index += 1
            # TODO save entry
            self.prepare_for_new_entry()
            self.read_entry_data(self.entry_index)
        return True

    def previous_entry(self):
        if self.entry_index > 0:
            self.entry_index -= 1
            # TODO save entry
            self.prepare_for_new_entry()
            self.read_entry_data(self.entry_index)
        return True




app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
