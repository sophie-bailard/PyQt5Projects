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
        #attributes of addressbook
        self.contacts = []
        self.address = []
        self.value = 0
        self.downloadedText = ""

        #widgetsk
        self._setLayouts()
        self._list()
        self._title()
        self._input()
        self._addContactButton()
        self._saveContactButton()
        self._progressBar()
        self._formatLayout()
        
        
#
#
# widget object functions
#
#

## title
    def _title(self):
        #Title
        self.title = QLabel("New Contact")
        font = QFont("Times", 16)
        self.title.setFont(font)


### inputs

    def _input(self):
        #input
        self._nameInput()
        self._addressInput()

    def _nameInput(self):
        self.entered_name = QLineEdit()
        self.entered_name.clear()
        self.formInputLayout.addRow("Name: ", self.entered_name)
        self.name_text = self.entered_name.text()

    def _addressInput(self):
        self.entered_address = QTextEdit()
        self.entered_address.clear()
        self.formInputLayout.addRow("Address: ", self.entered_address)
        self.address_text = self.entered_address.toPlainText()

### buttons

    def _addContactButton(self):
        #add contact button 
        self.add = QPushButton("Add")
        self.add.setFixedWidth(150)
        self.add.clicked.connect(self.submit)

    def _saveContactButton(self):
        #save contact button
        self.saveContacts = QPushButton("Save Contacts")
        self.saveContacts.setFixedWidth(150)
        self.saveContacts.clicked.connect(self.saveAllContactNoForm)
        self.saveContacts.hide()

## progress

    def _progressBar(self):
        #adds progress bar (hiden)
        self.progress = QProgressBar()
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        self.progress.setValue(0)

### contact list 

    def _list(self):
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.listDoubleClicked)
        #self.list.itemClicked.connect(self.listClicked)

### layout management

    def _setLayouts(self):
        #layouts
        self.layout = QVBoxLayout()
        self.listFormLayout = QHBoxLayout()
        self.formatInputFormLayout = QVBoxLayout()
        self.formInputLayout = QFormLayout()
        self.buttonLayout = QHBoxLayout()

    def _formatLayout(self):
        #formats layouts 
        self.buttonLayout.addSpacing(450)
        self.buttonLayout.addWidget(self.saveContacts)
        self.buttonLayout.addWidget(self.add)
        self.formatInputFormLayout.addWidget(self.title)
        self.formatInputFormLayout.addLayout(self.formInputLayout)
        self.formatInputFormLayout.addLayout(self.buttonLayout)
        self.listFormLayout.addWidget(self.list)
        self.listFormLayout.addLayout(self.formatInputFormLayout)
        self.layout.addWidget(self.progress)
        self.layout.addLayout(self.listFormLayout)
        self.setLayout(self.layout)

        
#
#
#on-click functions:
#
#

### submit 

    #saves name and address 
    #displays name on list
    def submit(self):
        self._setTextVariables()
        if self.name_text == "":
            self._emptyName()
        elif self.address_text == "":
            self._emptyAddress()
        else:
            self._submitContact()
            
        self.saveContacts.show()

    #converts name and address into text and stores values
    def _setTextVariables(self):
        self.name_text = self.entered_name.text()
        self.address_text = self.entered_address.toPlainText()

    #submits the contact
    def _submitContact(self):
        self._storeContact()
        self._successMessage()
        self._addNameToList()
        self._resetForm()
        self._setProgress() 

    #displays success message dialog
    def _successMessage(self):
        msg = QMessageBox.information(self, "Success!",
                "You added %s to your contacts!" % self.name_text, QMessageBox.Ok)

    #adds contact name to list of contacts
    def _addNameToList(self):
        self.list.addItem(self.name_text)

    #stores contact name and address to arrays
    def _storeContact(self):
        self.contacts.append(self.name_text)
        self.address.append(self.address_text)

    #displays error dialog if no name in contact
    def _emptyName(self):
        QMessageBox.information(self, "Empty Field",
                    "Please enter a name.")

    #displays error dialog if no address in contact
    def _emptyAddress(self):
        QMessageBox.information(self, "Empty Field",
                    "Please enter an address.")

    #clears name and address input from TextEdits 
    def _resetForm(self):
        self.entered_address.clear()
        self.entered_name.clear()

    # sets progress bar values and checks to see if full
    def _setProgress(self):
        self.value += 10
        self.progress.setValue(self.value)
        if self.value >= 100:
            self.full()

#########################################################################################################
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

### open basic text file 
       
    #opens a basic text file into the adress input area
    def openTextFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open File")
        self._storeFile(filename)
        self._convertDownload()

    #comverts downloaded text file to contact
    def _convertDownload(self):
        print("hi")

    #stores file if file exists
    def _storeFile(self, file):
        if file[0]:
            f = open(file[0], 'r')
            with f:
                self.downloadedText = f.read()

### open multiple files

     #prints a directory's location
    def openMultFiles(self):
        dialog = QFileDialog()
        #dialog.setFileMode(QFileDialog.Directory)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files = dialog.getExistingDirectory(self,"QFileDialog.getOpenFileNames()", "", options=options)
        if files:
            print(files)


### saves one specific contact

    #saves a contact to specified location as text file
    def saveContact(self):   
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        file = open(saveFile, 'w')
        self._formatText()
        file.write(self.complete_text)
        file.close()    

    # formats contact into text 
    def _formatText(self):
        self.complete_text = self.name_text + ": \n" + self.address_text + "\n"

### saveAll

    #saves all contacts to specified location as text file
    def saveAll(self):
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        if saveFile:
            file = open(saveFile, 'w')
            complete_text = self._textAllContactsForm()
            file.write(complete_text)
            file.close()
        self.test = saveFile

    #converts contacts into formatted text
    def _textAllContactsForm(self):
        complete_textForm = ""
        for count in range(0, len(self.contacts)):
            complete_textForm += self.contacts[count] + ": \n" + self.address[count] + "\n \n"
        return complete_textForm

### saveAllContact
            
    #saves all contacts to specified location as text file ("organized" not formatted)
    def saveAllContactNoForm(self):
        self.saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        if self.saveFile:
            file = open(self.saveFile, 'w')
            complete_text = self._textAllContactsNoForm()
            file.write(complete_text)
            file.close()
    
    #concatenates names and addresses into one string
    def _textAllContactsNoForm(self):
        contacts = self._setContactsText()
        addresses = self._setAddressesText()
        complete_text = contacts + "/" + addresses
        return complete_text

    #concatenates names into one string
    def _setContactsText(self):
        contacts = ""
        for count in range(0, len(self.contacts)):
            contacts = contacts + self.contacts[count] + " "
        return contacts
    
    #concatenates addresses into one string
    def _setAddressesText(self):
        addresses = ""
        for count in range(0, len(self.address)):
            addresses = addresses + self.address[count] + " "
        return addresses

###ListDoubleClicked    

    #displays contact when contact name in list clicked
    def listDoubleClicked(self, item):
        print(self.saveFile)
        name = item.text()
        index = -1
        for val in range(len(self.contacts)):
            if self.contacts[val]  == name:
                index = val
                
        if index != -1:
            self.n = self.contacts[val]
            self.a = self.address[val]
            self.item = item
            #popup = ContactPopUP(self.n, self.a, self)

            popup = QDialog()
            popLayout = QVBoxLayout()
            nameForm = "Name: " + self.n
            addressForm = "Address: " + self.a
            label1 = QLabel(nameForm, popup)
            label2 = QLabel(addressForm, popup)
            popLayout.addWidget(label1)
            popLayout.addWidget(label2)
            popup.setGeometry(100,200,100,100)
            question = QLabel("Delete Contact?")
            delete = QPushButton("Delete")
            delete.clicked.connect(self.delete)
            cancel = QPushButton("Cancel")
            cancel.clicked.connect(popup.close)
            layout = QHBoxLayout()
            layout.addLayout(popLayout)
            layout.addWidget(question)
            layout.addWidget(delete)
            layout.addWidget(cancel)
            popup.setLayout(layout)
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


