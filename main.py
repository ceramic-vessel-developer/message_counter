import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QStackedWidget, QDialog,QScrollArea,QWidget,QVBoxLayout,QLabel
import sys,os,script,time,threading
name=''
path=''
script_list=[]
final_string=''
class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)
class Sc3Thread(QtCore.QThread):
    _signal=QtCore.pyqtSignal(int)
    finished_signal=QtCore.pyqtSignal(bool)
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
        script_list=script.main(self.path, self.name,self._signal,self.processingLabel, self.progressBar,self.finished_signal)

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
        self.next.setHidden(True)

        self.process_button.clicked.connect(self.process_clicked)
        self.previous_button.clicked.connect(self.previous_clicked)
        self.next.clicked.connect(self.next_clicked)

        widget.currentChanged.connect(self.label_update)


    def label_update(self):
        global path, name
        self.thread = Sc3Thread(path, name, self.progressBar, self.processingLabel)
        self.thread._signal.connect(self.progressBar.setValue)
        self.thread.finished_signal.connect(self.next.setHidden)
        self.nameLabel.setText(name)
        self.nameLabel.adjustSize()
        self.pathLabel.setText(path)
        self.pathLabel.adjustSize()
    def previous_clicked(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def process_clicked(self):
        self.pathLabel.setHidden(True)
        self.nameLabel.setHidden(True)
        self.process_button.setHidden(True)
        self.infoLabel.setHidden(True)
        self.previous_button.setHidden(True)
        self.processingLabel.setHidden(False)
        self.progressBar.setHidden(False)
        self.thread.start()
    def next_clicked(self):
        global final_string
        for i in script_list:
            i.users = i.users.values()
        for i in script_list:
            final_string+=f'{i.conv_name}\n'
            for k in i.users:
                final_string+=f'\t{k.name}\n\t\tmessages: {k.mes}\n\t\tcharacters:{k.char}\n'
        widget.setCurrentIndex(widget.currentIndex() + 1)
class Screen4(QDialog):
    def __init__(self):
        super(Screen4,self).__init__()
        self.setWindowTitle("Message Counter")
        self.setObjectName("dialog")
        self.resize(400, 300)
        self.finishbutton = QtWidgets.QPushButton(self)
        self.finishbutton.setGeometry(QtCore.QRect(290, 260, 89, 25))
        self.finishbutton.setObjectName("finishbutton")
        self.finishbutton.setText('Finish')
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = ScrollLabel(self)
        self.label.setGeometry(200, 200, 200, 80)

        self.verticalLayout.addWidget(self.label)
        self.finishbutton.clicked.connect(lambda: sys.exit())
        widget.currentChanged.connect(lambda: self.label.setText(final_string))



screen_3=Screen3()
screen_4=Screen4()
widget.addWidget(screen_3)
widget.addWidget(screen_4)
widget.setFixedWidth(400)
widget.setFixedHeight(300)

widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Its over xD')
#TODO Clear this mess

