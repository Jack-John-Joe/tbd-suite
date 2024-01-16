# note to self: install PyQt5 in install.TBD!!!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Create menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # Create actions for open, save, and exit
        openAct = QAction('Open', self)
        openAct.triggered.connect(self.openFile)

        saveAct = QAction('Save', self)
        saveAct.triggered.connect(self.saveFile)

        exitAct = QAction('Exit', self)
        exitAct.triggered.connect(self.close)

        # Add actions to the file menu
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('easy-writer')
        self.show()

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if fileName:
            with open(fileName, 'r') as file:
                text = file.read()
                self.textEdit.setPlainText(text)

    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if fileName:
            with open(fileName, 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
