#Time and date

#!/usr/in/python3 #Defines where the interpretor is located. Tells the operating system that it is a python script?
# -*- coding: utf-8 -*- #Necessary?

import sys #Necessary?
#from PyQt5.QtCore import QDate, QTime, QDateTime, Qt #Why should "Qt" be imported? What does it stand for?
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QTextEdit, QFileDialog
from PyQt5.QtGui import QFont

"""
def date_time():
    now = QDate.currentDate() #Defines a variable (or function?) "now" with the current date.

    #Uses the variable "now" to print the current date in different ways
    print("Date as ISO: ", now.toString(Qt.ISODate)) #The toString simply returns the date as a string. ISO stands for "international date format"
    print("Date as set on this computer: ", now.toString(Qt.DefaultLocaleLongDate)) #Local refers to the local time zone in which the computer is set (?)

    datetime = QDateTime.currentDateTime() #Declares a variable (?) "datetime" with both the date and time

    print("The date and time: ", datetime.toString())

    time = QTime.currentTime()

    print("The time as set on this computer", time.toString(Qt.DefaultLocaleLongDate)) #Why should this way of converting to string be used?
"""

def small_window():
    class Window(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):

            QToolTip.setFont(QFont('SansSerif', 10)) #Sets the font for the Tooltip elements (the text explaining the function of a widget by popping up when hovering

            #Run button
            buttonRun = QPushButton('Run', self) #Creates a pushbutton
            buttonRun.setToolTip('Press to run the test') #Sets the Tooltip for the button
            buttonRun.resize(buttonRun.sizeHint()) #Results in a recommended size for the button
            buttonRun.move(100,50) #Moves the button

            #Save button
            buttonSave = QPushButton('Save', self) #Creates a pushbutton
            buttonSave.setToolTip('Press to save your changes') #Sets the Tooltip för the button
            buttonSave.resize(buttonSave.sizeHint()) #Results in a recommended size for the button
            buttonSave.move(25,50) #Moves the button

            #Dropdown menu
            self.lbl = QLabel('Files', self)
            dropDown = QComboBox(self)
            dropDown.addItem("File 1")
            dropDown.addItem("File 2")
            dropDown.addItem("File 3")
            dropDown.move(25, 25)
            self.lbl.move(50,150)
            dropDown.activated[str].connect(self.on_activated)

            self.setGeometry(300,300,300,220)
            self.setWindowTitle('GUI')
            self.show()

        def open_text(self):
            filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
            with open(filename[0], 'r') as f:
                file_text = f.read()
                self.text.setText(file_text)

        def on_activated(self, text):
            self.lbl.setText(text)
            self.lbl.adjustSize()


    app = QApplication(sys.argv) #Creates an application object. sys.argv is a list of command line arguments.
    ex = Window()
    sys.exit(app.exec_())

"""
    window = QWidget() #Creates a window (that is, a widget without a parent)
    window.resize(250, 150) #Resizes the window
    window.move(300, 300) # Moves the window on the screen (x,y)
    window.setWindowTitle('Small Window') #Sets the title of the window
    window.show() #Shows the window on the screen

    sys.exit(app.exec_()) #Closes the application (?)

"""

def main():
    #date_time()

    small_window()

if __name__ == '__main__' :
    main()
