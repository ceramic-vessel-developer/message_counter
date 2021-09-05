import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QStackedWidget, QDialog
import sys,os,script,time,threading
name=''
path=''
script_list=[]

class Sc3Thread(QtCore.QThread):
    _signal=QtCore.pyqtSignal(int)
    def __init__(self,path,name,progressBar,processingLabel):
        super(Sc3Thread, self).__init__()
        self.path=path
        self.name=name
        self.progressBar=progressBar
        self.processingLabel=processingLabel

    def __del__(self):
        self.wait()
    def run(self):
        global script_list
        script_list=script.main(self.path, self.name,self._signal,self.processingLabel, self.progressBar)

# class PercentageWorker(QtCore.QObject):
#     started = QtCore.pyqtSignal()
#     finished = QtCore.pyqtSignal()
#     percentageChanged = QtCore.pyqtSignal(int)
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self._percentage = 0
#
#     @property
#     def percentage(self):
#         return self._percentage
#
#     @percentage.setter
#     def percentage(self, value):
#         if self._percentage == value:
#             return
#         self._percentage = value
#         self.percentageChanged.emit(self.percentage)
#
#     def start(self):
#         self.started.emit()
#
#     def finish(self):
#         self.finished.emit()
#
#
# class FakeWorker:
#     def start(self):
#         pass
#
#     def finish(self):
#         pass
#
#     @property
#     def percentage(self):
#         return 0
#
#     @percentage.setter
#     def percentage(self, value):
#         pass
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
        global path, name
        self.processingLabel.setHidden(True)
        self.progressBar.setHidden(True)
        self.pathLabel.setHidden(False)

        self.process_button.clicked.connect(self.process_clicked)
        self.previous_button.clicked.connect(self.previous_clicked)

        widget.currentChanged.connect(self.label_update)


    def label_update(self):
        global path, name
        self.thread = Sc3Thread(path, name, self.progressBar, self.processingLabel)
        self.thread._signal.connect(self.progressBar.setValue)
        self.nameLabel.setText(name)
        self.nameLabel.adjustSize()
        self.pathLabel.setText(path)
        self.pathLabel.adjustSize()
    def previous_clicked(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def process_clicked(self):
        #self.thread = Sc3Thread(path, name, self.progressBar, self.processingLabel)
        self.pathLabel.setHidden(True)
        self.nameLabel.setHidden(True)
        self.process_button.setHidden(True)
        self.infoLabel.setHidden(True)
        self.previous_button.setHidden(True)
        self.processingLabel.setHidden(False)
        self.progressBar.setHidden(False)
        self.thread.start()



screen_3=Screen3()
widget.addWidget(screen_3)
widget.setFixedWidth(400)
widget.setFixedHeight(300)

widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Its over xD')
#TODO Clear this mess

