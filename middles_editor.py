import datetime
import json
import re
import sys

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QShortcut
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
        self.entry_result = self.output["results"][self.entry_index]
        self.displayed_entry = self.output["results"][self.entry_index]
        self.change_entries(0)
        self.ui.is_middle_button.clicked.connect(self.save_middle)
        self.ui.is_not_middle_button.clicked.connect(self.delete_middle)
        self.ui.reset_entry_button.clicked.connect(self.reset_middle)
        self.ui.next_button.clicked.connect(self.next_entry)
        self.ui.previous_button.clicked.connect(self.previous_entry)
        # The value that was previously held in which_middle_spin_box
        self.which_middle_old = 0
        self.ui.which_middle_spin_box.valueChanged.connect(self.which_middle_changed)
        self.ui.add_middle_button.clicked.connect(self.add_middle)
        self.ui.remove_middle_button.clicked.connect(self.remove_middle)
        # Updating display when middle is edited
        self.ui.subject_line_edit.editingFinished.connect(self.edit_middle)
        self.ui.subject_spin_box.editingFinished.connect(self.edit_middle)
        self.ui.verb_line_edit.editingFinished.connect(self.edit_middle)
        self.ui.verb_spin_box.editingFinished.connect(self.edit_middle)
        self.ui.adverb_line_edit.editingFinished.connect(self.edit_middle)
        self.ui.adverb_spin_box.editingFinished.connect(self.edit_middle)

        # shortcuts
        self.next_shortcut = QShortcut(QKeySequence("Right"), self)
        self.next_shortcut.activated.connect(self.next_entry)
        self.next_shortcut = QShortcut(QKeySequence("Left"), self)
        self.next_shortcut.activated.connect(self.previous_entry)
        self.save_shortcut = QShortcut(QKeySequence("s"), self)
        self.save_shortcut.activated.connect(self.save_middle)
        self.delete_shortcut = QShortcut(QKeySequence("d"), self)
        self.delete_shortcut.activated.connect(self.delete_middle)
        self.show()

    # Called when the displayed middle's markup needs to be changed
    def edit_middle(self):
        assert self.entry_result is not None and self.entry_result is not False
        self.ui.sentence_label.setText(self.markup_sentence())



    # called when the add middle button is pressed.
    def add_middle(self):
        assert self.entry_result is not None and self.entry_result is not False
        empty_middle = {"subject": {"word": "", "index": 0},
                        "verb": {"word": "", "index": 0},
                        "adverb": {"word": "", "index": 0},
                        "note": ""}
        self.entry_result["middles"].append(empty_middle)
        self.ui.which_middle_spin_box.setMaximum(self.ui.which_middle_spin_box.maximum() + 1)

    def remove_middle(self):
        assert self.entry_result is not None and self.entry_result is not False
        # there always has to be at least one middle saved and the last one can't be deleted while viewing
        if len(self.entry_result["middles"]) > 1 and \
                self.ui.which_middle_spin_box.value() != len(self.entry_result["middles"]) - 1:
            self.entry_result["middles"] = self.entry_result["middles"][:-1]
            self.ui.which_middle_spin_box.setMaximum(self.ui.which_middle_spin_box.maximum() - 1)
    # Called when the user selects a new middle to be viewed.
    # Saves the data currently in the widgets and changes them to show the new middle

    def which_middle_changed(self):
        # save the values in the widgets
        # assert that the middle is saved already
        if self.entry_result is not None and self.entry_result is not False:
            # save the values
            new_middle_values = {"note": self.ui.note_editor.toPlainText(),
                                 "subject": {"word": self.ui.subject_line_edit.text(),
                                             "index": self.ui.subject_spin_box.value()},
                                 "verb": {"word": self.ui.verb_line_edit.text(),
                                          "index": self.ui.verb_spin_box.value()},
                                 "adverb": {"word": self.ui.adverb_line_edit.text(),
                                            "index": self.ui.adverb_spin_box.value()},
                                 "source_of_transitivity": "Data Entry"}
            self.entry_result["middles"][self.which_middle_old] = new_middle_values
            # display new values
            if len(self.entry_result["middles"]):
                self.ui.remove_middle_button.setEnabled(False)
            else:
                self.ui.remove_middle_button.setEnabled(True)
            in_focus_middle = self.entry_result["middles"][self.ui.which_middle_spin_box.value()]
            self.ui.sentence_label.setText(self.markup_sentence())
            self.ui.note_editor.setPlainText(in_focus_middle["note"])
            self.ui.subject_line_edit.setText(in_focus_middle["subject"]["word"])
            self.ui.subject_spin_box.setValue(in_focus_middle["subject"]["index"])
            self.ui.verb_line_edit.setText(in_focus_middle["verb"]["word"])
            self.ui.verb_spin_box.setValue(in_focus_middle["verb"]["index"])
            self.ui.adverb_line_edit.setText(in_focus_middle["adverb"]["word"])
            self.ui.adverb_spin_box.setValue(in_focus_middle["adverb"]["index"])

        self.which_middle_old = self.ui.which_middle_spin_box.value()

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
        output_json["results"] = [None] * len(self.input["results"])
        return output_json

    # Runs when the is_middle_button is pressed
    def save_middle(self):
        # the middle could already be saved
        if self.entry_result is not None and self.entry_result is not False:
            return
        # it must not be saved
        # start it off as the entry from the input file. notes will be added and such
        self.entry_result = self.input["results"][self.entry_index]
        self.change_entries(self.entry_index)
        self.ui.note_editor.setFocus(True)

    # Called when the delete middle button is pressed
    def delete_middle(self):
        self.entry_result = False
        # Saves this update to the file and clears any extra data
        self.change_entries(self.entry_index)

    # Called when the reset middle button is pressed
    def reset_middle(self):
        self.entry_result = None
        self.change_entries(self.entry_index)

    # Displays a entry and restricts widgets values (e.i subject_spin_box value must be an index of the sentence)
    def read_entry_data(self):
        # I want this to set all of the fields to show the data.
        # TODO Set the maximum of the spin boxes to be the number of words in sentence.
        # if the middle is not accounted for OR deleted, display the input file one
        entry = self.input['results'][self.entry_index]

        if self.entry_result is not None and self.entry_result is not False:
            # The middle has been accounted for and extra data may have been added.
            entry = self.entry_result
        self.displayed_entry = entry
        words_in_sentence = len(entry["sentence"].split(" "))
        self.ui.which_middle_spin_box.setValue(0)
        self.ui.which_middle_spin_box.setMaximum(len(entry["middles"]) - 1)
        self.ui.groupBox.setTitle("Middle {0}/{1}".format(self.entry_index, self.input["sentence_number"] - 1))
        self.ui.note_editor.setPlainText(entry["middles"][0]["note"])
        self.ui.subject_line_edit.setText(entry["middles"][0]["subject"]["word"])
        # words in sentence - 1 because you select indices
        self.ui.subject_spin_box.setMaximum(words_in_sentence - 1)
        self.ui.subject_spin_box.setValue(entry["middles"][0]["subject"]["index"])

        self.ui.verb_line_edit.setText(entry["middles"][0]["verb"]["word"])
        self.ui.verb_spin_box.setMaximum(words_in_sentence - 1)
        self.ui.verb_spin_box.setValue(entry["middles"][0]["verb"]["index"])

        self.ui.adverb_line_edit.setText(entry["middles"][0]["adverb"]["word"])
        self.ui.adverb_spin_box.setMaximum(words_in_sentence - 1)
        self.ui.adverb_spin_box.setValue(entry["middles"][0]["adverb"]["index"])
        # Using the values in the widgets, markup_sentence
        self.ui.sentence_label.setText(self.markup_sentence())
        self.which_middle_changed() # since it was just changed above

    # adds color and underlines to the words of the middle currently displayed
    # Information is gathered from the widgets
    def markup_sentence(self):
        middle = self.displayed_entry["middles"][self.ui.which_middle_spin_box.value()]
        split_sentence = self.displayed_entry["sentence"].split(" ")
        for e in [(self.ui.subject_line_edit.text(), self.ui.subject_spin_box.value(), "red"),
                  (self.ui.verb_line_edit.text(), self.ui.verb_spin_box.value(), "green"),
                  (self.ui.adverb_line_edit.text(), self.ui.adverb_spin_box.value(), "blue")]:
            index = e[1]
            word = e[0]
            for i in range(index, index - 3, -1):
                if 0 <= i < len(split_sentence) and re.search('(\W|^)' + word, split_sentence[i]) is not None:
                    split_sentence[i] = "<font color=\"{0}\"><u>{1}</u></font>".format(e[2], split_sentence[i])
        return " ".join(split_sentence)

    def next_entry(self):
        self.change_entries(self.entry_index + 1)

    def previous_entry(self):
        self.change_entries(self.entry_index - 1)

    def change_entries(self, new_index):
        # make sure any changes made to the entry are saved to the output file
        # if the entry needs to be saved
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
        # save the updated entry to the output json
        self.output["results"][self.entry_index] = self.entry_result
        # change data to point to new entry
        # check extreme values
        if new_index < 0:
            self.entry_index = 0
        elif new_index > len(self.input["results"]) - 1:
            self.entry_index = len(self.input["results"]) - 1
        else:
            self.entry_index = new_index
        # load in the status of the new entry
        self.entry_result = self.output["results"][self.entry_index]
        # there are three cases the widgets need to be aware of.
        if self.entry_result is None or self.entry_index is False:
            # all of the widgets for editing the middle.
            # we don't want them enabled
            self.ui.note_editor.setEnabled(False)
            self.ui.which_middle_spin_box.setEnabled(False)
            self.ui.which_middle_spin_box.setMaximum(0)
            self.ui.add_middle_button.setEnabled(False)
            self.ui.remove_middle_button.setEnabled(False)
            self.ui.subject_line_edit.setEnabled(False)
            self.ui.subject_spin_box.setEnabled(False)
            self.ui.verb_line_edit.setEnabled(False)
            self.ui.verb_spin_box.setEnabled(False)
            self.ui.adverb_line_edit.setEnabled(False)
            self.ui.adverb_spin_box.setEnabled(False)
        if self.entry_result is None:
            self.ui.is_not_middle_button.setEnabled(True)
            self.ui.is_middle_button.setEnabled(True)
            self.ui.reset_entry_button.setEnabled(False)
            self.ui.status_label.setText("Unaccounted For")
        elif self.entry_result is False:
            self.ui.is_not_middle_button.setEnabled(True)
            self.ui.is_middle_button.setEnabled(False)
            self.ui.reset_entry_button.setEnabled(True)
            self.ui.status_label.setText("Deleted")

        else:
            # the middle is saved and all of the editing widgets need to be enabled
            self.ui.status_label.setText("Saved")
            self.ui.is_not_middle_button.setEnabled(False)
            self.ui.is_middle_button.setEnabled(True)
            self.ui.reset_entry_button.setEnabled(True)
            self.ui.note_editor.setEnabled(True)
            self.ui.which_middle_spin_box.setEnabled(True)
            self.ui.add_middle_button.setEnabled(True)
            self.ui.remove_middle_button.setEnabled(True)
            self.ui.subject_line_edit.setEnabled(True)
            self.ui.subject_spin_box.setEnabled(True)
            self.ui.verb_line_edit.setEnabled(True)
            self.ui.verb_spin_box.setEnabled(True)
            self.ui.adverb_line_edit.setEnabled(True)
            self.ui.adverb_spin_box.setEnabled(True)
        # load the data into the widgets
        self.read_entry_data()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
