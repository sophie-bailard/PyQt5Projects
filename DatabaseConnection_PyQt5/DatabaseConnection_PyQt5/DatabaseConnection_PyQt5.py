


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

# Description of Application: 
# this is the rough draft of the project menu

#Main Application
class App(QMainWindow):

    #initializes application
    def __init__(self):
        super().__init__()
        self.title = 'Demo menu window'
        self.width = 1500
        self.height = 800
        self.setFixedSize(self.width, self.height)
        self.initUI()

    #initializes the UI
    def initUI(self):
        self.setWindowTitle(self.title)
        self._menu()
        self._toolBar()
        p = self.palette()
        color = QColor(255, 255, 255)
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
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

##################### TOOLBAR #####################################

    #creates toolbar for main window
    def _toolBar(self):
        self.toolBar = QToolBar()
        self.LOtb = []
        self._addToolButtons()
        self._setAllToolButtonColor(self.LOtb)
        self.addToolBar(self.toolBar)

    #creates toolButtons and adds them to toolBar
    def _addToolButtons(self):
        button1 = self._addTButton("toolbar button")
        button1.clicked.connect(self._openPopUp)
        
    #creates toolbutton and adds to List-of Toolbuttons
    def _addTButton(self, text):
        toolButton = QToolButton()
        toolButton.setText(text)
        self.LOtb.append(toolButton)
        self.toolBar.addWidget(toolButton)
        return toolButton

    #sets all toolbuttons to a color
    def _setAllToolButtonColor(self, LOtb):
        if LOtb:
            for tb in LOtb:
                toolButtonColor = QColor(209, 220, 255)
                self._setWidgetColor(tb, toolButtonColor)

    #sets a widget's background color
    def _setWidgetColor(self, w, color):
        w.setAutoFillBackground(True)
        p = w.palette()
        p.setColor(w.backgroundRole(), color)
        w.setPalette(p)

    def _openPopUp(self):
        self.popup = CreateBoxPop()
        self.popup.show()

###############################################################

#creates widgets to put on main menu
class Create_Widgets(QWidget):

    #initializes widgets
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        
        self.setLayout(self.layout)


#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
















