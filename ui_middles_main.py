# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'middles_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 964)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setToolTip("")
        self.groupBox.setStatusTip("")
        self.groupBox.setWhatsThis("")
        self.groupBox.setAccessibleName("")
        self.groupBox.setAccessibleDescription("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.is_middle_button = QtWidgets.QPushButton(self.groupBox)
        self.is_middle_button.setToolTip("<html><head/><body><p>Saves this middle</p></body></html>")
        self.is_middle_button.setStatusTip("")
        self.is_middle_button.setWhatsThis("")
        self.is_middle_button.setAccessibleName("")
        self.is_middle_button.setAccessibleDescription("")
        self.is_middle_button.setStyleSheet("font: 18pt \"Sans Serif\";")
        self.is_middle_button.setObjectName("is_middle_button")
        self.horizontalLayout_4.addWidget(self.is_middle_button)
        self.is_not_middle_button = QtWidgets.QPushButton(self.groupBox)
        self.is_not_middle_button.setToolTip("<html><head/><body><p>Deletes the middle and goes to next entry</p></body></html>")
        self.is_not_middle_button.setStatusTip("")
        self.is_not_middle_button.setWhatsThis("")
        self.is_not_middle_button.setAccessibleName("")
        self.is_not_middle_button.setAccessibleDescription("")
        self.is_not_middle_button.setStyleSheet("font: 18pt \"Sans Serif\";")
        self.is_not_middle_button.setObjectName("is_not_middle_button")
        self.horizontalLayout_4.addWidget(self.is_not_middle_button)
        self.reset_entry_button = QtWidgets.QPushButton(self.groupBox)
        self.reset_entry_button.setEnabled(False)
        self.reset_entry_button.setMinimumSize(QtCore.QSize(0, 23))
        self.reset_entry_button.setToolTip("<html><head/><body><p>Resets this entry to how it was before you started editing it. Marks it unaccounted for</p></body></html>")
        self.reset_entry_button.setStatusTip("")
        self.reset_entry_button.setWhatsThis("")
        self.reset_entry_button.setAccessibleName("")
        self.reset_entry_button.setAccessibleDescription("")
        self.reset_entry_button.setStyleSheet("font: 18pt \"Sans Serif\";")
        self.reset_entry_button.setObjectName("reset_entry_button")
        self.horizontalLayout_4.addWidget(self.reset_entry_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.status_label = QtWidgets.QLabel(self.groupBox)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_2.addWidget(self.status_label)
        self.sentence_label = QtWidgets.QLabel(self.groupBox)
        self.sentence_label.setToolTip("")
        self.sentence_label.setStatusTip("")
        self.sentence_label.setWhatsThis("")
        self.sentence_label.setAccessibleName("")
        self.sentence_label.setAccessibleDescription("")
        self.sentence_label.setStyleSheet("background-color: rgb(238, 238, 238);\n"
"font: 14pt \"Sans Serif\";")
        self.sentence_label.setLineWidth(4)
        self.sentence_label.setScaledContents(True)
        self.sentence_label.setWordWrap(True)
        self.sentence_label.setObjectName("sentence_label")
        self.verticalLayout_2.addWidget(self.sentence_label)
        self.editing_entry_box = QtWidgets.QGroupBox(self.groupBox)
        self.editing_entry_box.setEnabled(True)
        self.editing_entry_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.editing_entry_box.setToolTip("")
        self.editing_entry_box.setStatusTip("")
        self.editing_entry_box.setWhatsThis("")
        self.editing_entry_box.setAccessibleName("")
        self.editing_entry_box.setAccessibleDescription("")
        self.editing_entry_box.setFlat(False)
        self.editing_entry_box.setCheckable(False)
        self.editing_entry_box.setObjectName("editing_entry_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.editing_entry_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.note_editor = QtWidgets.QPlainTextEdit(self.editing_entry_box)
        self.note_editor.setEnabled(False)
        self.note_editor.setToolTip("")
        self.note_editor.setStatusTip("")
        self.note_editor.setWhatsThis("")
        self.note_editor.setAccessibleName("")
        self.note_editor.setAccessibleDescription("")
        self.note_editor.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.note_editor.setObjectName("note_editor")
        self.verticalLayout.addWidget(self.note_editor)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.editing_entry_box)
        self.label_4.setToolTip("")
        self.label_4.setStatusTip("")
        self.label_4.setWhatsThis("")
        self.label_4.setAccessibleName("")
        self.label_4.setAccessibleDescription("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.which_middle_spin_box = QtWidgets.QSpinBox(self.editing_entry_box)
        self.which_middle_spin_box.setEnabled(False)
        self.which_middle_spin_box.setToolTip("<html><head/><body><p>Select which middle to view, if there are multiple middles in this sentence</p></body></html>")
        self.which_middle_spin_box.setStatusTip("")
        self.which_middle_spin_box.setWhatsThis("")
        self.which_middle_spin_box.setAccessibleName("")
        self.which_middle_spin_box.setAccessibleDescription("")
        self.which_middle_spin_box.setObjectName("which_middle_spin_box")
        self.horizontalLayout_3.addWidget(self.which_middle_spin_box)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.add_middle_button = QtWidgets.QPushButton(self.editing_entry_box)
        self.add_middle_button.setEnabled(False)
        self.add_middle_button.setToolTip("<html><head/><body><p>If you see another middle in this sentence, add it then fill out the fields.</p></body></html>")
        self.add_middle_button.setStatusTip("")
        self.add_middle_button.setWhatsThis("")
        self.add_middle_button.setAccessibleName("")
        self.add_middle_button.setAccessibleDescription("")
        self.add_middle_button.setObjectName("add_middle_button")
        self.horizontalLayout_2.addWidget(self.add_middle_button)
        self.remove_middle_button = QtWidgets.QPushButton(self.editing_entry_box)
        self.remove_middle_button.setEnabled(False)
        self.remove_middle_button.setToolTip("<html><head/><body><p>If there are too many middles listed for this entry, this will delete the one currently viewed</p></body></html>")
        self.remove_middle_button.setStatusTip("")
        self.remove_middle_button.setWhatsThis("")
        self.remove_middle_button.setAccessibleName("")
        self.remove_middle_button.setAccessibleDescription("")
        self.remove_middle_button.setIconSize(QtCore.QSize(16, 16))
        self.remove_middle_button.setObjectName("remove_middle_button")
        self.horizontalLayout_2.addWidget(self.remove_middle_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.editing_entry_box)
        self.label.setToolTip("")
        self.label.setStatusTip("")
        self.label.setWhatsThis("")
        self.label.setAccessibleName("")
        self.label.setAccessibleDescription("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.editing_entry_box)
        self.label_2.setToolTip("")
        self.label_2.setStatusTip("")
        self.label_2.setWhatsThis("")
        self.label_2.setAccessibleName("")
        self.label_2.setAccessibleDescription("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.editing_entry_box)
        self.label_3.setToolTip("")
        self.label_3.setStatusTip("")
        self.label_3.setWhatsThis("")
        self.label_3.setAccessibleName("")
        self.label_3.setAccessibleDescription("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.subject_line_edit = QtWidgets.QLineEdit(self.editing_entry_box)
        self.subject_line_edit.setEnabled(False)
        self.subject_line_edit.setToolTip("")
        self.subject_line_edit.setStatusTip("")
        self.subject_line_edit.setWhatsThis("")
        self.subject_line_edit.setAccessibleName("")
        self.subject_line_edit.setAccessibleDescription("")
        self.subject_line_edit.setObjectName("subject_line_edit")
        self.gridLayout.addWidget(self.subject_line_edit, 0, 1, 1, 1)
        self.subject_spin_box = QtWidgets.QSpinBox(self.editing_entry_box)
        self.subject_spin_box.setEnabled(False)
        self.subject_spin_box.setObjectName("subject_spin_box")
        self.gridLayout.addWidget(self.subject_spin_box, 0, 2, 1, 1)
        self.verb_line_edit = QtWidgets.QLineEdit(self.editing_entry_box)
        self.verb_line_edit.setEnabled(False)
        self.verb_line_edit.setToolTip("")
        self.verb_line_edit.setStatusTip("")
        self.verb_line_edit.setWhatsThis("")
        self.verb_line_edit.setAccessibleName("")
        self.verb_line_edit.setAccessibleDescription("")
        self.verb_line_edit.setObjectName("verb_line_edit")
        self.gridLayout.addWidget(self.verb_line_edit, 1, 1, 1, 1)
        self.adverb_line_edit = QtWidgets.QLineEdit(self.editing_entry_box)
        self.adverb_line_edit.setEnabled(False)
        self.adverb_line_edit.setToolTip("")
        self.adverb_line_edit.setStatusTip("")
        self.adverb_line_edit.setWhatsThis("")
        self.adverb_line_edit.setAccessibleName("")
        self.adverb_line_edit.setAccessibleDescription("")
        self.adverb_line_edit.setObjectName("adverb_line_edit")
        self.gridLayout.addWidget(self.adverb_line_edit, 2, 1, 1, 1)
        self.verb_spin_box = QtWidgets.QSpinBox(self.editing_entry_box)
        self.verb_spin_box.setEnabled(False)
        self.verb_spin_box.setObjectName("verb_spin_box")
        self.gridLayout.addWidget(self.verb_spin_box, 1, 2, 1, 1)
        self.adverb_spin_box = QtWidgets.QSpinBox(self.editing_entry_box)
        self.adverb_spin_box.setEnabled(False)
        self.adverb_spin_box.setObjectName("adverb_spin_box")
        self.gridLayout.addWidget(self.adverb_spin_box, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.editing_entry_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_button = QtWidgets.QPushButton(self.groupBox)
        self.previous_button.setToolTip("")
        self.previous_button.setStatusTip("")
        self.previous_button.setWhatsThis("")
        self.previous_button.setAccessibleName("")
        self.previous_button.setAccessibleDescription("")
        self.previous_button.setStyleSheet("font: 18pt \"Sans Serif\";")
        self.previous_button.setIconSize(QtCore.QSize(16, 20))
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(self.groupBox)
        self.next_button.setToolTip("")
        self.next_button.setStatusTip("")
        self.next_button.setWhatsThis("")
        self.next_button.setAccessibleName("")
        self.next_button.setAccessibleDescription("")
        self.next_button.setStyleSheet("font: 18pt \"Sans Serif\";")
        self.next_button.setIconSize(QtCore.QSize(16, 20))
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 20))
        self.menubar.setObjectName("menubar")
        self.menuControls = QtWidgets.QMenu(self.menubar)
        self.menuControls.setObjectName("menuControls")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_and_Exit = QtWidgets.QAction(MainWindow)
        self.actionSave_and_Exit.setObjectName("actionSave_and_Exit")
        self.actionGo_to_next_Unaccounted = QtWidgets.QAction(MainWindow)
        self.actionGo_to_next_Unaccounted.setObjectName("actionGo_to_next_Unaccounted")
        self.menuControls.addAction(self.actionSave_and_Exit)
        self.menuControls.addAction(self.actionGo_to_next_Unaccounted)
        self.menubar.addAction(self.menuControls.menuAction())
        self.label_4.setBuddy(self.which_middle_spin_box)
        self.label.setBuddy(self.subject_line_edit)
        self.label_2.setBuddy(self.verb_line_edit)
        self.label_3.setBuddy(self.adverb_line_edit)

        self.retranslateUi(MainWindow)
        self.is_middle_button.clicked['bool'].connect(self.note_editor.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.which_middle_spin_box.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.add_middle_button.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.remove_middle_button.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.subject_line_edit.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.verb_line_edit.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.adverb_line_edit.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.subject_spin_box.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.verb_spin_box.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.adverb_spin_box.setDisabled)
        self.is_not_middle_button.clicked['bool'].connect(self.note_editor.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.which_middle_spin_box.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.add_middle_button.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.remove_middle_button.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.subject_line_edit.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.verb_line_edit.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.adverb_line_edit.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.subject_spin_box.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.verb_spin_box.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.adverb_spin_box.setEnabled)
        self.is_middle_button.clicked['bool'].connect(self.is_not_middle_button.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.is_middle_button.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.is_middle_button.setDisabled)
        self.reset_entry_button.clicked['bool'].connect(self.is_not_middle_button.setDisabled)
        self.reset_entry_button.clicked['bool'].connect(self.note_editor.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.which_middle_spin_box.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.add_middle_button.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.remove_middle_button.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.subject_line_edit.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.adverb_line_edit.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.subject_spin_box.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.verb_spin_box.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.adverb_spin_box.setEnabled)
        self.reset_entry_button.clicked['bool'].connect(self.verb_line_edit.setEnabled)
        self.is_not_middle_button.clicked['bool'].connect(self.reset_entry_button.setDisabled)
        self.is_middle_button.clicked['bool'].connect(self.reset_entry_button.setDisabled)
        self.reset_entry_button.clicked['bool'].connect(self.reset_entry_button.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.is_middle_button, self.is_not_middle_button)
        MainWindow.setTabOrder(self.is_not_middle_button, self.note_editor)
        MainWindow.setTabOrder(self.note_editor, self.which_middle_spin_box)
        MainWindow.setTabOrder(self.which_middle_spin_box, self.add_middle_button)
        MainWindow.setTabOrder(self.add_middle_button, self.remove_middle_button)
        MainWindow.setTabOrder(self.remove_middle_button, self.reset_entry_button)
        MainWindow.setTabOrder(self.reset_entry_button, self.subject_line_edit)
        MainWindow.setTabOrder(self.subject_line_edit, self.subject_spin_box)
        MainWindow.setTabOrder(self.subject_spin_box, self.verb_line_edit)
        MainWindow.setTabOrder(self.verb_line_edit, self.adverb_line_edit)
        MainWindow.setTabOrder(self.adverb_line_edit, self.verb_spin_box)
        MainWindow.setTabOrder(self.verb_spin_box, self.adverb_spin_box)
        MainWindow.setTabOrder(self.adverb_spin_box, self.previous_button)
        MainWindow.setTabOrder(self.previous_button, self.editing_entry_box)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Middle x/y"))
        self.is_middle_button.setText(_translate("MainWindow", "Has a Middle"))
        self.is_not_middle_button.setText(_translate("MainWindow", "Has No Middle"))
        self.reset_entry_button.setText(_translate("MainWindow", "Reset Entry"))
        self.status_label.setText(_translate("MainWindow", "Status"))
        self.sentence_label.setText(_translate("MainWindow", "this is a middle"))
        self.editing_entry_box.setTitle(_translate("MainWindow", "Editing Entry"))
        self.note_editor.setPlainText(_translate("MainWindow", "this is a good note"))
        self.label_4.setText(_translate("MainWindow", "Which Middle:"))
        self.add_middle_button.setText(_translate("MainWindow", "Add Middle"))
        self.remove_middle_button.setText(_translate("MainWindow", "Delete Last Middle"))
        self.label.setText(_translate("MainWindow", "Subject"))
        self.label_2.setText(_translate("MainWindow", "Verb"))
        self.label_3.setText(_translate("MainWindow", "Adverb"))
        self.subject_line_edit.setText(_translate("MainWindow", "middle"))
        self.verb_line_edit.setText(_translate("MainWindow", "reads"))
        self.adverb_line_edit.setText(_translate("MainWindow", "well"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.menuControls.setTitle(_translate("MainWindow", "Controls"))
        self.actionSave_and_Exit.setText(_translate("MainWindow", "Save and Exit"))
        self.actionGo_to_next_Unaccounted.setText(_translate("MainWindow", "Go to next Unaccounted"))
