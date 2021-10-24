from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2 import QtWidgets
import sys


class CV:
    def __init__(self):
        qfile=QFile("ui/ui.ui")
        #qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui=QUiLoader().load(qfile)
        #self.ui.open_btn.clicked.connect(self.open)
    def open(self):
        img=open(r"D:\96s0008p1qp91nop5r0.jpg")


if __name__ == '__main__':
    print("Program start")
    app = QApplication(sys.argv)
    window=CV()
    window.ui.show()
    app.exec_()