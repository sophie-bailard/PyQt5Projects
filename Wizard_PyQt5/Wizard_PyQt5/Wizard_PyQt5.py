

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

# A Fake installation Wizard: 


#Main Application
class App(QMainWindow):

    #initializes application
    def __init__(self):
        super().__init__()
        self.title = 'Title'
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
        self.create_widgets = Wizard(self)
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

#creates installation wizard
class Wizard(QWidget):

    #initializes game
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        begin = QPushButton("Begin")
        begin.clicked.connect(self.begin_clicked)
        self.layout.addWidget(begin)
        self._wizard()

    def _wizard(self):
        layout = QHBoxLayout()
        self.list = self._list()
        layout.addLayout(self.list)
        self.wizard = QWizard()
        self.intro()
        
    def _list(self):
        layout = QVBoxLayout
        to_do = QListWidget()
        to_do.addItem("intro")
        to_do.addItem("selection")
        to_do.addItem("licensing")
        to_do.addItem("download")
        to_do.addItem("complete")
        layout.addWidget(to_do)
        return layout


    def intro(self):
        intro_page = QWizardPage()
        intro_page.setTitle("Installation")
        intro_page.setSubTitle("subtitle")




    def begin_clicked(self):
        self.wizard.open()
        

#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



