import datetime
import json
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_middles_main import Ui_MainWindow


class AppWindow(QMainWindow):
    entry_index: int

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open("test.json", 'r') as f:
            self.input = json.load(f)
        self.output = self.create_output_json("test.json")
        self.entry_index = 0
        self.entry_result = self.output["data_results"][self.entry_index]
        self.read_entry_data()
        self.ui.is_middle_button.clicked.connect(self.save_middle)
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
        output_json["complete"] = False
        output_json["data_results"] = [None] * len(self.input["results"])
        return output_json

    # Runs when the is_middle_button is pressed
    def save_middle(self):
        # the middle could already be saved
        if self.entry_result is not None and self.entry_result is not False:
            return
        # it must not be saved
        # start it off as the entry from the input file. notes will be added and such
        self.entry_result = self.input["results"][self.entry_index]

    # Prepares the form for a new middle by enabling and disabling things. Doesn't display the middle
    def prepare_for_new_entry(self):
        self.entry_result = self.output["data_results"][self.entry_index]
        self.ui.is_middle_button.setEnabled(True)
        self.ui.is_not_middle_button.setEnabled(True)

        # all of the widgets for editing the middle.
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
    def read_entry_data(self):
        # I want this to set all of the fields to show the data.
        # TODO make this read in the values from the input file.

        # if the middle is not accounted for OR deleted, display the input file one
        entry = self.input['results'][self.entry_index]

        if self.entry_result is None:
            self.ui.status_label.setText("Unaccounted for")
        else:
            self.ui.status_label.setText("Deleted")

        if self.entry_result is not None and self.entry_result is not False:
            # The middle has been accounted for and extra data may have been added.
            entry = self.entry_result
            self.ui.status_label.setText("Saved")
        self.ui.which_middle_spin_box.setValue(0)
        self.ui.groupBox.setTitle("Middle {0}/{1}".format(self.entry_index, self.input["sentence_number"] - 1))
        self.ui.note_editor.setPlainText(entry["middles"][0]["note"])
        self.ui.sentence_label.setText(entry['sentence'])
        self.ui.subject_line_edit.setText(entry["middles"][0]["subject"]["word"])
        self.ui.subject_spin_box.setValue(entry["middles"][0]["subject"]["index"])
        self.ui.verb_line_edit.setText(entry["middles"][0]["verb"]["word"])
        self.ui.verb_spin_box.setValue(entry["middles"][0]["verb"]["index"])
        self.ui.adverb_line_edit.setText(entry["middles"][0]["adverb"]["word"])
        self.ui.adverb_spin_box.setValue(entry["middles"][0]["adverb"]["index"])

    def next_entry(self):
        if self.entry_index < len(self.input["results"]) - 1:
            self.record_current_entry()
            self.entry_index += 1
            # TODO save entry
            self.prepare_for_new_entry()
            self.read_entry_data()
        return True

    def previous_entry(self):
        if self.entry_index > 0:
            self.record_current_entry()
            self.entry_index -= 1
            # TODO save entry
            self.prepare_for_new_entry()
            self.read_entry_data()
        return True

    # called when changing entries. Saves the current data to the output JSON
    def record_current_entry(self):
        # if it is being saved, we need to save data.
        if self.entry_result is not None and self.entry_result is not False:
            # gather data stored in widgets into the result
            middle = self.entry_result["middles"][self.ui.which_middle_spin_box.value()]
            middle["note"] = self.ui.note_editor.toPlainText()
            middle["subject"]["word"] = self.ui.subject_line_edit.text()
            middle["subject"]["index"] = self.ui.subject_spin_box.value()
            middle["verb"]["word"] = self.ui.verb_line_edit.text()
            middle["verb"]["index"] = self.ui.verb_spin_box.value()
            middle["adverb"]["word"] = self.ui.adverb_line_edit.text()
            middle["adverb"]["index"] = self.ui.adverb_spin_box.value()
            self.entry_result["middles"][self.ui.which_middle_spin_box.value()] = middle

        self.output["data_results"][self.entry_index] = self.entry_result


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
