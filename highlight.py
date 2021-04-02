import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat


class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parnet):
        super().__init__(parnet)
        self._highlight_lines= {}

    def highlight_line(self, line_num, fnt):
        if isinstance(line_num, int) and line_num >= 0 and isinstance(fnt, QTextCharFormat):
            self._highlight_lines[line_num]=fnt
            block = self.document().findBlockByLineNumber(line_num)
            self.rehighlightBlock(block)
        

    def clear_highlight(self):
        self._highlight_lines={}
        self.rehighlight()


    def highlightBlock(self, text):
        blockNumber = self.currentBlock().blockNumber()
        fnt= self._highlight_lines.get(blockNumber)
        if fnt is not None:
            self.setFormat(0, len(text), fnt)




class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)

        mainLayout = QVBoxLayout()

        validator=QRegExpValidator(QRegExp(r'[0-9 ]+'))

        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet('font-size: 30px; height: 50px')
        self.lineEdit.setValidator(validator)
        self.lineEdit.textChanged.connect(self.onTextChanged)
        mainLayout.addWidget(self.lineEdit)

        self.textEditor =QPlainTextEdit()
        self.textEditor.setStyleSheet('font-size: 30px; color:green')
        mainLayout.addWidget(self.textEditor) 

        for i in range(1,21):
            self.textEditor.appendPlainText('line {0}'.format(i))

        self.highlighter = SyntaxHighlighter(self.textEditor.document())
        self.setLayout(mainLayout)


    def onTextChanged(self, text):
        fnt=QTextCharFormat()
        fnt.setBackground(QColor('yellow'))
        self.highlighter.clear_highlight()

        try:
            lineNumber = int(text)-1
            self.highlighter.highlight_line(lineNumber, fnt)

        except ValueError:
            pass
  
app=QApplication(sys.argv)
demo=AppDemo()
demo.show()
sys.exit(app.exec_())