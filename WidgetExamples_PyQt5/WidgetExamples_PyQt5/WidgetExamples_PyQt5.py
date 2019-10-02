

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 50
        self.top = 100
        self.width = 300
        self.height = 200
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_widgets = Create_Widgets(self)
        self.setCentralWidget(self.create_widgets)
        
        self.show()
    
    #statusbar
    #def _statusbar(self):
     #   self.statusBar().showMessage('Message in statusbar.')
    

class Create_Widgets(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.add_tabs()
     

     #creates widgets to go on UI
    def create_widgets(self):
        #self._statusbar()
        #self._button()
        #self._messagebox()
        #self._textbox()
        self._menu()
        #self._table()
       # self._tabs
         # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show()

    def add_tabs(self):

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)

        # Add tabs
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")
     
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

        self.bwidget = self._dock()
        self.tab1.layout.addWidget(self.bwidget)
        self.tab1.setLayout(self.tab1.layout)


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

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

    def _dock(self):
      self.items = QDockWidget(self)
      self.listWidget = QListWidget()
      self.listWidget.addItem("item1")
      self.listWidget.addItem("item2")
      self.listWidget.addItem("item3")
      self.items.setWidget(self.listWidget)
      self.items.setFloating(False)
      return self.items
    
    #table
    def _table(self):
        self.tableWidget = QTableWidget()

        #rows
        rows = 4
        self.tableWidget.setRowCount(rows)

        #columns
        cols = 5
        self.tableWidget.setColumnCount(cols)

        #set values for rows and columns
        for i in range(rows):
            for j in range(cols):
               self.tableWidget.setItem(i,j, QTableWidgetItem("Cell (" + str(i) + ", " + str(j) + ")"))

        self.tableWidget.move(0,0)

        self.tableWidget.doubleClicked.connect(self.on_click)


    #button
    def _button(self):
        button = QPushButton('show text', self)
        button.setToolTip("This is an example button")
        button.resize(120, 40)
        button.clicked.connect(self.on_click)
        return button

    #messagebox
    def _messagebox(self):
        buttonReply = QMessageBox.question(self, "message", "Is your favorite color blue?")
        if buttonReply == QMessageBox.Yes:
            print("Yes clicked")
        else:
            print("No clicked")

    #textbox
    def _textbox(self):
        self.textbox = QLineEdit(self)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


class Testing(QWidget):
     def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        grid.addWidget(self.createExampleGroup(), 1, 0)
        self.setLayout(grid)

     def createExampleGroup(self):
        groupBox = QGroupBox("Best Food")

        radio1 = QRadioButton("&Radio pizza")
        radio2 = QRadioButton("R&adio taco")
        radio3 = QRadioButton("Ra&dio burrito")

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())





















