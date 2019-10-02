

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

#this application asks the user for their favorites and displays them on the next pages

#Main Application
class App(QMainWindow):

    #initializes application
    def __init__(self):
        super().__init__()
        self.title = 'Hello!'
        self.left = 200
        self.top = 150
        self.width = 500
        self.height = 200
        self.initUI()

    #initializes the UI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self._menu()
        self.create_widgets = Create_Widgets(self)
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


class Create_Widgets(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.stack = self._stack()
        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)
        
    #sets and organizes the input/output pages
    def _stack(self):
        self.stack1 = QWidget()
        self.stack2 = QWidget()

        self.stack1UI()

        self.final_stack = QStackedWidget(self)
        self.final_stack.addWidget(self.stack1)
        self.final_stack.addWidget(self.stack2)

        return self.final_stack

    #input page
    def stack1UI(self):
        vbox_main = QVBoxLayout()
        form = QFormLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()

        #title 
        title = QLabel("Enter Your Favorites: ")
        title.setFont(QFont("SansSerif", 18))
        hbox2.addWidget(title)

        #stores user input
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()

        #creating input form
        form.addRow("What is your favorite color? ", self.lineEdit1)
        form.addRow("What is your favorite season? ", self.lineEdit2)
        form.addRow("What is your favorite movie? ", self.lineEdit3)
        form.addRow("What is your favorite food? ", self.lineEdit4)

        # submit button
        # on_click --> stores data and displays output page
        submit = QPushButton("submit")
        hbox.addWidget(submit)
        submit.clicked.connect(self.on_click)

        #combines and formats layouts
        vbox_main.addLayout(hbox2)
        vbox_main.addLayout(form)
        vbox_main.addLayout(hbox)

        #sets stack1's layout
        self.stack1.setLayout(vbox_main)

    # sets output page based on inputs
    # displays output page
    def on_click(self):
        self.stack2UI()
        self.final_stack.setCurrentIndex(1)

    #output page
    def stack2UI(self):
        layout = QVBoxLayout()

        #creates labels from stored Data
        label1 = QLabel("Favorite color: " + self.lineEdit1.text())
        label2 = QLabel("Favorite season: " + self.lineEdit2.text())
        label3 = QLabel("Favorite movie: " + self.lineEdit3.text())
        label4 = QLabel("Favorite food: " + self.lineEdit4.text())

        #adds labels to layout
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        #sets stack2 to layout
        self.stack2.setLayout(layout)

#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


