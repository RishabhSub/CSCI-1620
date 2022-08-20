from lzma import is_check_supported
from PyQt5.QtWidgets import *
from views import Ui_MainWindow
import csv


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
 
        self.save_button.clicked.connect(lambda: self.submit())

    def submit(self):
        name = self.name_input.text()
        age = int(self.age_input.text())
        status = ''
        if self.radio_student.isChecked():
            status = 'Student'
        if self.radio_staff.isChecked():
            status = 'Staff'
        if self.radio_both.isChecked():
            status = 'Both'
        with open('records.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow((name, age * 2, status))
        self.name_input.setText('')
        self.age_input.setText('')

        if self.buttonGroup.checkedButton() != 0:
            self.buttonGroup.setExclusive(False)
            self.buttonGroup.checkedButton().setChecked(False)
            self.buttonGroup.setExclusive(True)
