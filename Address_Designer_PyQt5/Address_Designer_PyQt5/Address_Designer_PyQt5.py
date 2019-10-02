
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from PyQt5.uic import loadUi



# This is an adddress book application 
# add contacts, display contacts, save file, open file

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
        self.limit = False
        self.progressValue = 0
        mt = []
        self.a = AddressBook(mt)
        self.initUI()

    #initializes the UI
    def initUI(self):
        loadUi('AddressDesigner.ui', self)
        self.add.clicked.connect(self.addContact)
        self.save_all.clicked.connect(self.saveAll)
        self.list.itemDoubleClicked.connect(self.contactClicked)
        self.save_all.hide()
        self.show()

    #deletes specified item in a list
    def _deleteItem(self, item):
        self.list.takeItem(self.list.currentRow())
    
    #contactClicked
    def contactClicked(self, item):
        for contact in self.a.contacts:
            if contact.name == item.text():
                selected = contact
        self.pop = ContactPopup(selected, self.a, item, self)
        self.pop.show()


### add contact and helpers

    #adds contact to address book
    def addContact(self):
        self._setTextVariables()
        if self.name_text == "":
            self._emptyName()
        elif self.address_text == "":
            self._emptyAddress()
        else:
            self._submitContact()

    #submits contact and saves to address book
    def _submitContact(self):
        c = Contact(self.name_text, self.address_text)
        self.a.addContact(c)
        self._addToList()
        self._clearInput()
        self._setProgress()
        self.save_all.show()

    #adds the name of the contact to the list of contacts 
    def _addToList(self):
        self.list.addItem(self.name_text)

    #sets variables for entries converted to text
    def _setTextVariables(self):
        self.name_text = self.name_entered.text()
        self.address_text = self.address_entered.toPlainText()

    #clears input boxes
    def _clearInput(self):
        self.name_entered.clear()
        self.address_entered.clear()

    #displays error dialog if no name in contact
    def _emptyName(self):
        QMessageBox.information(self, "Empty Field",
                    "Please enter a name.")

    #displays error dialog if no address in contact
    def _emptyAddress(self):
        QMessageBox.information(self, "Empty Field",
                    "Please enter an address.")

    #sets the progressbar 
    def _setProgress(self):
        self.progressValue += 10
        self.progressBar.setValue(self.progressValue)
        self._checkLimit()

    #popup when full
    def _checkLimit(self):
        if self.progressValue >= 100:
            self.limt = True
            self.add.hide()
            self.full = FullPopUp(self.a, self)
            self.full.show()
        else:
            self.limt = False
            self.add.show()

    #deletes incremental amount from progress
    def _deleteProgress(self):
        self.progressValue -= 10
        self.progressBar.setValue(self.progressValue)
        self._checkLimit()

### save contacts and helpers

    #saves all contacts to specified location as text file
    def saveAll(self):
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        if saveFile:
            file = open(saveFile, 'w')
            complete_text = self._contactsText()
            file.write(complete_text)
            file.close()

    #converts contacts into formatted text
    def _contactsText(self):
        return self.a.toText()

#represents a list of contacts 
class AddressBook(object):
    def __init__(self, contacts):
        super().__init__()
        self.contacts = contacts

    #adds a contact to the address book
    def addContact(self, contact):
        self.contacts.append(contact)

    #displays the address book (helps with testing)
    def displayAddressBook(self):
        for c in self.contacts:
            c.displayContact()

    #converts address book to text
    def toText(self):
        complete_text = ""
        for c in self.contacts:
            complete_text += c.toText()
        return complete_text

    #saves the addressbook with QFileDialog
    def saveAll(self, gui):
        saveFile = QFileDialog.getSaveFileName(gui, "Save File", '/', '.txt')[0]
        if saveFile:
            file = open(saveFile, 'w')
            complete_text = self.toText()
            file.write(complete_text)
            file.close()

    #deletes specified contact from address book
    def _deleteContact(self, contact):
        for c in self.contacts:
            if c.isSameAs(contact):
                self.contacts.remove(contact)
        for c in self.contacts:
            c.displayContact()

#represents a contact with name and address
class Contact(object):
    def __init__(self, name, address):
        super().__init__()
        self.name = name
        self.address = address

    #displays the contact (helps with testing)
    def displayContact(self):
        print(self.name)
        print(self.address)

    #converts contact to text 
    def toText(self):
        return self.name + ": \n" + self.address + "\n \n"

    #checks if two contacts are equal
    def isSameAs(self, contact):
        return self.name == contact.name and self.address == contact.address

#mini display of contact
class ContactPopup(QDialog):
    def __init__(self, contact, addressBook, item, gui):
        super().__init__()
        loadUi('AddressContactPopUp.ui', self)
        h = QLabel()
        self.gui = gui
        self.item = item
        self.contact = contact
        self.addressBook = addressBook
        self.name_entered.setText(contact.name)
        self.address_entered.setText(contact.address)
        self.deleteButton.clicked.connect(self._deleteContact)
        self.cancelButton.clicked.connect(self.close)
        self.show()

    #deletes a contact from the address book
    def _deleteContact(self):
        self.addressBook._deleteContact(self.contact)
        self.gui._deleteItem(self.item)
        self.gui._deleteProgress()
        self.close()

#warning popup signaling addressbook is full
class FullPopUp(QDialog):
    def __init__(self, addressbook, gui):
        super().__init__()
        self.gui = gui
        self.a = addressbook
        loadUi("Full.ui", self)
        self.save.clicked.connect(self._save)
        self.cancel.clicked.connect(self.close)
        
    #saves address book
    def _save(self):
        self.a.saveAll(self.gui)
            
#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())