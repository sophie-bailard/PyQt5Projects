
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Test(QMainWindow):
    def __init__(self):
        super(Test,self).__init__()
        loadUi('madlibs.ui', self)
        self.submit.clicked.connect(self.on_click)

    def on_click(self):
        self.stack2UI()

     #output page
    def stack2UI(self):
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addSpacing(5)

        #obtains inputs from user in text 
        #format and sets to simpler variables
        t1 = self.lineEdit1.text()
        t2 = self.lineEdit2.text()
        t3 = self.lineEdit3.text()
        t4 = self.lineEdit4.text()
        t5 = self.lineEdit5.text()
        t6 = self.lineEdit6.text()
        t7 = self.lineEdit7.text()

        #madlibs paragraph with user input inserted
        madlibs = QPlainTextEdit("Julia is so " + t1 + " to be graduating" \
            "from Northern State University. She has earned a degree in culinary arts, " \
            "but wishes she had majored in " + t2 + ". Julia spent " + t3 + " number of hours each" \
            " week studying, & stayed up late thanks to all the " + t4 + " she consumed." \
            "She is so " + t5 + "that she was able to finish college in 4 years instead of " + \
            t6 + " years, like everyone thought. So after studying, finals, & " + t7 + ", Julia" \
            " can't wait to enter the real world and start paying off those student loans!")

        #user cannot edit the output
        madlibs.setReadOnly(True)

        #play_again = QPushButton("Play Again?")
        #hbox.addWidget(play_again)
        #play_again.clicked.connect(self.on_click)

        layout.addWidget(madlibs)
        self.stack2.setLayout(layout)


app=QApplication(sys.argv)
widget=Test()
widget.show()
sys.exit(app.exec_())