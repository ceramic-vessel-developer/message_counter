import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QStackedWidget, QDialog
import sys,os,script,test,time
name=''
path=''
class EmittingStream(QtCore.QObject):
    text_written=QtCore.pyqtSignal(str)
    def write(self,text):
        self.text_written.emit(str(text))
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
        else:
            self.error.setHidden(True)
            widget.setCurrentIndex(widget.currentIndex()+1)
class Screen2(QDialog):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi('screen_2.ui',self)
        self.error.setHidden(True)
        self.previous_button.clicked.connect(self.previous_clicked)
        self.next_button.clicked.connect(self.next_clicked)
        self.browse_button.clicked.connect(self.browse_clicked)
    def previous_clicked(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def next_clicked(self):
        global path
        path=self.line_path.text()

        if not path:
            self.error.setHidden(False)
        else:
            print(path)
            self.error.setHidden(True)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def browse_clicked(self):
        pathname=QtWidgets.QFileDialog.getExistingDirectory(self,'Choose directory',os.getcwd())
        self.line_path.setText(pathname)



app=QApplication(sys.argv)
screen_1=Screen1()
screen_2=Screen2()

widget=QStackedWidget()
widget.addWidget(screen_1)
widget.addWidget(screen_2)
class Screen3(QDialog):
    def __init__(self):
        super(Screen3,self).__init__()
        loadUi('screen_3.ui',self)
        self.processingLabel.setHidden(True)
        self.progressBar.setHidden(True)
        self.pathLabel.setHidden(False)

        self.process_button.clicked.connect(self.process_clicked)
        self.previous_button.clicked.connect(self.previous_clicked)
        widget.currentChanged.connect(self.label_update)
    def label_update(self):
        self.nameLabel.setText(name)
        self.nameLabel.adjustSize()
        self.pathLabel.setText(path)
        self.pathLabel.adjustSize()
    def previous_clicked(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def process_clicked(self):
        pass
screen_3=Screen3()
widget.addWidget(screen_3)
widget.setFixedWidth(400)
widget.setFixedHeight(300)

widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Its over xD')

