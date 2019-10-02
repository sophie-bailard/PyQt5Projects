import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from string import Template
import urllib.request

# This is an adddress book application 
# add contacts, display contacts, save file, open file, 


#Main Application
class App(QMainWindow):

    #initializes application
    def __init__(self):
        super().__init__()
        self.title = 'Address'
        self.left = 200
        self.top = 150
        self.width = 600
        self.height = 300
        self.initUI()

    #initializes the UI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)
        self._menu()
        self.create_widgets = AddressBook(self)
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

#
#
#
# NEW CLASS
#
#
#

# represents the AddressBook
class AddressBook(QWidget):

    #initializes game
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.contacts = []
        self.address = []
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.listDoubleClicked)
        #self.list.itemClicked.connect(self.listClicked)
        self.value = 0
        self.downloadedText = ""

        #layouts
        main = QHBoxLayout()
        layout = QVBoxLayout()
        form = QFormLayout()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        #Title
        title = QLabel("New Contact")
        font = QFont("Times", 16)
        title.setFont(font)

        #input
        self.entered_name = QLineEdit()
        self.entered_name.clear()
        form.addRow("Name: ", self.entered_name)
        self.entered_address = QTextEdit()
        self.entered_address.clear()
        form.addRow("Address: ", self.entered_address)
        
        #add contact button 
        add = QPushButton("Add")
        add.setFixedWidth(150)
        add.clicked.connect(self.submit)

        #save contact button
        self.saveContacts = QPushButton("Save Contacts")
        self.saveContacts.setFixedWidth(150)
        self.saveContacts.clicked.connect(self.saveAll)
        self.saveContacts.hide()

        #adds progress bar (hiden)
        self.progress = QProgressBar()
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        self.progress.setValue(0)

        #formats layouts 
        hbox.addSpacing(450)
        hbox.addWidget(self.saveContacts)
        hbox.addWidget(add)
        layout.addWidget(title)
        layout.addLayout(form)
        layout.addLayout(hbox)
        main.addWidget(self.list)
        main.addLayout(layout)
        self.layout.addWidget(self.progress)
        self.layout.addLayout(main)
        self.setLayout(self.layout)

#
#
#on-click functions:
#
#

    #saves name and address 
    #displays name on list
    def submit(self):
        if self.entered_name.text() == "":
            QMessageBox.information(self, "Empty Field",
                    "Please enter a name.")
            return 
        elif self.entered_address.toPlainText() == "":
            QMessageBox.information(self, "Empty Field",
                    "Please enter an address.")
            return
        else:
            self.contacts.append(self.entered_name.text())
            self.address.append(self.entered_address.toPlainText())
            msg = QMessageBox.information(self, "Success!",
                    "You added %s to your contacts!" % self.entered_name.text(), QMessageBox.Ok)
            self.list.addItem(self.entered_name.text())
            self.entered_address.clear()
            self.entered_name.clear()
            self.value += 50
            self.progress.setValue(self.value)
            if self.value >= 100:
                self.full()
        self.saveContacts.show()
       
    #opens a basic text file into the adress input area
    def openTextFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File")

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()

        self.downloadedText = data
        print(self.downloadedText)
        self.convertDownload()


     #prints a directory's location
    def openMultFiles(self):
        dialog = QFileDialog()
        #dialog.setFileMode(QFileDialog.Directory)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files = dialog.getExistingDirectory(self,"QFileDialog.getOpenFileNames()", "", options=options)
        if files:
            print(files)

    #saves a contact to specified location as text file
    def saveContact(self):   
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        file = open(saveFile, 'w')
        name_text = self.entered_name.text()
        address_text = self.entered_address.toPlainText()
        complete_text = name_text + ": \n" + address_text + "\n"
        file.write(complete_text)
        file.close()    

    #saves all contacts to specified location as text file
    def saveAll(self):
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        if saveFile:
            file = open(saveFile, 'w')
            complete_text = ""
            for count in range(0, len(self.contacts)):
                complete_text += self.contacts[count] + ": \n" + self.address[count] + "\n \n"
               

            file.write(complete_text)
            file.close()
            
    #saves all contacts to specified location as text file
    def saveAllContactForm(self):
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        if saveFile:
            file = open(saveFile, 'w')
            complete_text = ""
            contacts = ""
            addresses =""
            for count in range(0, len(self.contacts)):
                contacts = contacts + self.contacts[count] + " "
                addresses = addresses + self.address[count] + " "

            complete_text += contacts + "/" + addresses

            file.write(complete_text)
            file.close()

    #comverts downloaded text file to contact
    def convertDownload(self):
        print("hi")

    #displays contact when contact name in list clicked
    def listDoubleClicked(self, item):
        name = item.text()
        index = -1
        for val in range(len(self.contacts)):
            if self.contacts[val]  == name:
                index = val
                
        if index != -1:
            self.n = self.contacts[val]
            self.a = self.address[val]
            self.item = item
            popup = ContactPopUP(self.n, self.a, self)

            
            popup.show()

    #asks if user would like to delete contact if contact double clicked
    def ex(self, item):
        name = item.text()
        index = -1
        for val in range(len(self.contacts)):
            if self.contacts[val]  == name:
                index = val
                
        if index != -1:
            n = self.contacts[val]
            a = self.address[val]
            popup = QDialog()
            question = QLabel("Delete Contact?")
            delete = QPushButton("Delete")
            delete.clicked.connect(self.delete(a, n, item))
            cancel = QPushButton("Cancel")
            cancel.clicked.connect(self.popup.close)
            layout = QHBoxLayout()
            layout.addWidget(question)
            layout.addWidget(delete)
            layout.addWidget(cancel)
            popup.setLayout(layout)

    def delete(self):
        self.address.remove(self.a)
        self.contacts.remove(self.n)
        self.list.removeItemWidget(self.item)
                

#
# helper methods
#
#

    #if progress bar is full popup
    def full(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        self.dialog = QDialog()
        title = QLabel("Looks like your contact book is full! Save?")
        save = QPushButton("Save")
        save.clicked.connect(self.saveAll)
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.dialog.close)
        vbox.addWidget(title)
        hbox.addSpacing(50)
        hbox.addWidget(save)
        hbox.addWidget(cancel)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)
        self.dialog.show()
        
#
#
#
# NEW CLASS
#
#
#

#contact pop up
#pop up with name and address of contact
class ContactPopUP(QDialog):
     def __init__(self, name, address, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.name = "Name: " + name
        self.address = "Address: " + address
        self.label1 = QLabel(self.name, self)
        self.label2 = QLabel(self.address, self)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.setLayout(self.layout)



###################################################################

#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


