import  PyQt5
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QStackedWidget, QDialog
import sys
import script
name=''
path=''
class Screen1(QDialog):
    def __init__(self):
        super(Screen1,self).__init__()
        loadUi('screen_1.ui',self)
        self.error.setHidden(True)
        self.next_button.clicked.connect(self.button_clicked)
    def button_clicked(self):
        global name
        name=self.name.text()
        if not name:
            self.error.setHidden(False)
app=QApplication(sys.argv)
screen_1=Screen1()
widget=QStackedWidget()
widget.addWidget(screen_1)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Its over xD')

