
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot

# Description of Application: 


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

# creates widgets for gui
# MadLibs game
class Create_Widgets(QWidget):

    #initializes game
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        run_progress = QPushButton("Run")
        self.layout.addWidget(run_progress)
        run_progress.clicked.connect(self.clicked)
        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)
        self.setLayout(self.layout)
        
    def clicked(self):
        count = 0
        while count < 100:
            count += 0.00001
            self.progress.setValue(count)
        

#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




