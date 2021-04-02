
from PyQt5.QtWidgets import QApplication,QDialog, QGroupBox,\
    QHBoxLayout,QLabel ,QVBoxLayout, QRadioButton
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
 
 
 
 
class Window(QDialog):
    def __init__(self):
        super().__init__()
 
        #winow requirement
        self.setGeometry(200,200, 400,300)
        self.setWindowTitle("PyQt5 QRadioButton")
        self.setWindowIcon(QIcon('python.png'))
 
        #our method call
        self.create_radiobutton()
 
        #we need to create vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
 
        #this is our label
        self.label = QLabel("")
        self.label.setFont(QFont("Sanserif", 14))
 
        #add your widgets in the vbox layout
        vbox.addWidget(self.label)
 
 
        #set your main window layout
        self.setLayout(vbox)
 
 
 
 
    def create_radiobutton(self):
 
        #this is our groupbox
        self.groupbox = QGroupBox("What is your favorite sport ?")
        self.groupbox.setFont(QFont("Sanserif", 15))
 
 
        #this is hbox layout
        hbox = QHBoxLayout()
 
        #these are the radiobuttons
        self.rad1 = QRadioButton("Football")
        self.rad1.setChecked(True)
        self.rad1.setIcon(QIcon('football.png'))
        self.rad1.setIconSize(QSize(40,40))
        self.rad1.setFont(QFont("Sanserif", 14))
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)
 
        self.rad2 = QRadioButton("Cricket")
        self.rad2.setIcon(QIcon('cricket.png'))
        self.rad2.setIconSize(QSize(40, 40))
        self.rad2.setFont(QFont("Sanserif", 14))
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)
 
        self.rad3 = QRadioButton("Tennis")
        self.rad3.setIcon(QIcon('tennis.png'))
        self.rad3.setIconSize(QSize(40, 40))
        self.rad3.setFont(QFont("Sanserif", 14))
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)
 
 
 
 
        self.groupbox.setLayout(hbox)
 
 
 
 
    #method or slot for the toggled signal
    def on_selected(self):
        radio_button = self.sender()
 
        if radio_button.isChecked():
            self.label.setText("You have selected : " + radio_button.text())
 
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
