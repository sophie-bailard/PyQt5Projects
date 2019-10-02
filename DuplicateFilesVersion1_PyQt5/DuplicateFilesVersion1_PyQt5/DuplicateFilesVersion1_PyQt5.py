
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from shutil import copyfile
import os

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
        self.initUI()

    #initializes the UI
    def initUI(self):
        loadUi('interface.ui', self)
        self.progressBar.setValue(self.progressValue)
        self.start.clicked.connect(self.testMakeDir)
        self.show()

    #testing
    def testMakeDir(self):
        self.popup = ChooseDirectoryPopup(self)
        self.popup.show()
        
    def incrementProgress(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
       

    #sends to duplicateFile 
    def _duplicate(self):
        self._duplicateFile(self.name)

    def _duplicateFile(self):
        print("hi")

    #duplicates a file given its filepath
    def _createNewFile(self, fileName):
        file = "C:/Users/sbailard/source/repos/PyQt5/DuplicateFile_PyQt5/DuplicateFile_PyQt5/" + fileName + ".txt"
        fptr = open(file, "x")
        text = "hello there!"
        fptr.write(text)
        fptr.close()
        #copyfile("dailyReport.txt", "testFile.txt")

    #saves all contacts to specified location as text file
    def saveAll(self):
        saveFile = QFileDialog.getSaveFileName(self, "Save File", '/', '.txt')[0]
        if saveFile:
            file = open(saveFile, 'w')
            complete_text = self._contactsText()
            file.write(complete_text)
            file.close()

#allows user to create a directory
class ChooseDirectoryPopup(QDialog):
    def __init__(self, gui):
        super().__init__()
        loadUi('directory.ui', self)
        self.gui = gui
        self.submit.clicked.connect(self._start)

    def _start(self):
        print("hi")
        files = []
        location = self.location_entered.text() + self.name_entered.text() + "/"
        print(location)
        dir = Directory(self.name_entered.text(), files, location)
        list = ["name1", "name2"]
        for n in range(100):
            name = "name" + str(n+1)
            list.append(name)
        c = "asdnfkjlasdlsdgjdlaklasdfklgnsdljfklfjmvslasdnfkjlasdlsdgjdlaklasdfklgnsdljfklfjmvsl" 
        for n in list:
            file = File(n, c, dir)
            self.gui.incrementProgress()
            
      



#a class representing the file object
class File(object):
    def __init__(self, name, contents, dir):
        super().__init__()
        self.name = name
        self.contents = contents
        self.dir = dir
        self.makeFile()

    #change the contents of a file
    def _changeContents(self, newContents):
        self.contents = newContents

    #creates a new file in directory
    def makeFile(self):
        filepath = self.dir.path + self.name + ".txt"
        file = open(filepath, 'w')
        file.write(self.contents)
        file.close()

class Directory(object):
    def __init__(self, name, files, path):
        super().__init__()
        self.name = name
        self.files = files
        self.path = path
        self.makeDirectory()

    #write current list of files into directory
    def _writeCurrentFiles(self):
        for file in self.files:
            file.makeFile()

    #add singular file to dir
    def _addFile(self, file):
        file.makeFile()
        self.files.append(file)

    #add files to directory
    def _addFiles(self, files):
        for file in files:
            file.makeFile()
        self.files.append(files)

    #creates a new directory with specified name
    def makeDirectory(self):
        #dirpath = "C:/Users/sbailard/source/repos/PyQt5/DuplicateFile_PyQt5/DuplicateFile_PyQt5/" + self.name + "/"
        #self.path = dirpath
        directory = os.path.dirname(self.path)
        os.makedirs(directory)
        




#runs application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

