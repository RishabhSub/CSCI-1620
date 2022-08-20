from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window

        # For the "Name" and Name's input box
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

        # For "Age" and Age's input box
        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=15, side='left')
        self.frame_age.pack(anchor='w', pady=10)

        # For the radio buttons underneath
        self.frame_radio = Frame(self.window)
        self.label_radio = Label(self.frame_radio, text='Status')
        self.radio_default = IntVar()
        self.radio_default.set(4)
        self.radio_student = Radiobutton(self.frame_radio, text='Student', variable=self.radio_default, value=0)
        self.radio_staff = Radiobutton(self.frame_radio, text='Staff', variable=self.radio_default, value=1)
        self.radio_both = Radiobutton(self.frame_radio, text='Both', variable=self.radio_default, value=2)

        self.label_radio.pack(side='left', padx=5)
        self.radio_student.pack(side='left')
        self.radio_staff.pack(side='left')
        self.radio_both.pack(side='left')
        self.frame_radio.pack(anchor='w', pady=10)

        # Submit button at the bottom
        self.frame_save = Frame(self.window)
        self.button_save = Button(self.frame_save, text='Save', command=self.clicked)
        self.button_save.pack()
        self.frame_save.pack(pady=10)

    def clicked(self):
        """
        - This method should only be called when the save button is clicked.
        - Retrieve the name, age, and status values.
        - The age must be doubled (e.g. if someone entered 5 for age, their age would be stored as 10).
        - Determine the person status based off the value of the radio button selected.

        - Open the records.csv file and append the new person's details.
        - I suggest first viewing the csv file's contents to understand how your data should be sent to it.

        - Clear the name and age values that were entered in the GUI.
        - Make sure you clear the status value (i.e, No status value should be selected).
        """
        name = self.entry_name.get()
        age = int(self.entry_age.get())
        status = self.radio_default.get()
        status_text = ''
        if status == 0:
            status_text = 'Student'
        elif status == 1:
            status_text = 'Staff'
        elif status == 2:
            status_text = 'Both'
        with open('records.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow((name, age * 2, status_text))
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio_default.set(4)

