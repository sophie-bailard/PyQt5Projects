

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

# This is a "MadLibs" application
# Given constraints, user inputs values to be inserted in a paragraph
# after inputs submitted, the story is displayed


#Main Application
class App(QMainWindow):

    #initializes application
    def __init__(self):
        super().__init__()
        self.title = 'MadLibs'
        self.left = 200
        self.top = 150
        self.width = 500
        self.height = 450
        self.initUI()

    #initializes the UI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedHeight(self.height)
        self._menu()
        self.create_widgets = MadLibs(self)
        self.setCentralWidget(self.create_widgets)
        self.show()

    #menu
    def _menu(self):
        mainMenu = self.menuBar()
        #drop down labels
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        
        #drop down content
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

# creates widgets for gui
# MadLibs game
class MadLibs(QWidget):

    #initializes game
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.stack = self._stack()
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)
        
    #organizes different levels of madlibs
    #first input page then output page
    def _stack(self):
        self.stack1 = QWidget()
        self.stack2 = QWidget()

        self.stack1UI()

        self.final_stack = QStackedWidget(self)
        self.final_stack.addWidget(self.stack1)
        self.final_stack.addWidget(self.stack2)

        return self.final_stack

    #user input page
    def stack1UI(self):
        #layout structures
        vbox_main = QVBoxLayout()
        form = QFormLayout()
        hboxform = QHBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()

        #Title for form
        title = QLabel("Enter Your Favorites: ")
        font = QFont("SansSerif", 18)
        font.setBold(True)
        title.setFont(font)
        hbox2.addWidget(title)

        #storing user input
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.lineEdit7 = QLineEdit()

        #adds rows to the form layout
        #gives constraints and takes in user input
        form.addRow("An adjective: ", self.lineEdit1)
        form.addRow("A major: ", self.lineEdit2)
        form.addRow("A number: ", self.lineEdit3)
        form.addRow("A food or drink: ", self.lineEdit4)
        form.addRow("Another adjective: ", self.lineEdit5)
        form.addRow("Another number: ", self.lineEdit6)
        form.addRow("A verb: ", self.lineEdit7)

        hboxform.addSpacing(30)
        hboxform.addLayout(form)
                
        #submit button
        #when clicked, transition to next stack
        submit = QPushButton("submit")
        hbox.addWidget(submit)
        submit.clicked.connect(self.on_click)
        
        #adding other layouts to main one
        vbox_main.addLayout(hbox2)
        vbox_main.addSpacing(20)
        vbox_main.addLayout(hboxform)
        vbox_main.addSpacing(20)
        vbox_main.addLayout(hbox)

        #sets the first stack layout
        self.stack1.setLayout(vbox_main)

    #sets the output page based on inputs
    #transitions input page to output page when called
    def on_click(self):
        self.stack2UI()
        #if(self.final_stack.currentIndex == 0): 
        self.final_stack.setCurrentIndex(1)
        #else:
           # self.final_stack.setCurrentIndex(0)
        

    #output page
    def stack2UI(self):
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addSpacing(5)
        
        #obtains inputs from user in text 
        #format and sets to simpler variables
        t1 = self.lineEdit1.text()
        t2 = self.lineEdit2.text()
        t3 = self.lineEdit3.text()
        t4 = self.lineEdit4.text()
        t5 = self.lineEdit5.text()
        t6 = self.lineEdit6.text()
        t7 = self.lineEdit7.text()

        #madlibs paragraph with user input inserted
        madlibs = QPlainTextEdit("Julia is so " + t1 + " to be graduating" \
            "from Northern State University. She has earned a degree in culinary arts, " \
            "but wishes she had majored in " + t2 + ". Julia spent " + t3 + " number of hours each" \
            " week studying, & stayed up late thanks to all the " + t4 + " she consumed." \
            "She is so " + t5 + "that she was able to finish college in 4 years instead of " + \
            t6 + " years, like everyone thought. So after studying, finals, & " + t7 + ", Julia" \
            " can't wait to enter the real world and start paying off those student loans!")

        #user cannot edit the output
        madlibs.setReadOnly(True)

        #play_again = QPushButton("Play Again?")
        #hbox.addWidget(play_again)
        #play_again.clicked.connect(self.on_click)

        layout.addWidget(madlibs)
        self.stack2.setLayout(layout)

#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


