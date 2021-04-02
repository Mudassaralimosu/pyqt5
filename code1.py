import sys
from PyQt5.QtWidgets import QApplication,QWidget

class WindowExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.show()
        self.setWindowTitle("GeeksCoders.com")

app=QApplication(sys.argv)
window=WindowExample()
sys.exit(app.exec_())