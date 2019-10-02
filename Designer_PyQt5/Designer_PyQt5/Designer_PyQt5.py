
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from PyQt5.uic import loadUi



# This is an adddress book application 
# add contacts, display contacts, save file, open file, 


#Main Application
class App(QDialog):

    #initializes application
    def __init__(self):
        super(App, self).__init__()
        self.title = 'Address'
        self.left = 200
        self.top = 150
        self.width = 600
        self.height = 300
        self.initUI()

    #initializes the UI
    def initUI(self):
        loadUi('AddressDesigner.ui', self)
        self.show()


#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())










