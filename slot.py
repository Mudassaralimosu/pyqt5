from PySide2.QtWidgets import *
from PySide2.QtCore import Slot

@Slot()
def youClicked():
    label.setText("You clicked the button")


app=QApplication([])
window=QWidget()
layout=QVBoxLayout()
button=QPushButton(" I'M JUST A KID FROM KOLKATA ")
label=QLabel('z("&)_|')
button.clicked.connect(youClicked)
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()
