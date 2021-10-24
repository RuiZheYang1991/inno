import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import numpy.core._dtype_ctypes


class WinForm(QMainWindow):

    def __init__(self, parent=None):
        self.img = np.zeros(1)
        super(WinForm, self).__init__(parent)
        self.setGeometry(150, 100, 1130, 750)  # 視窗起始位置，視窗大小
        layout = QVBoxLayout()

        self.btn1 = QPushButton('開啟圖片', self)
        self.btn1.setGeometry(10, 10, 60, 30)  # 按鈕啟始位置，按鈕大小
        self.btn1.clicked.connect(self.open)#連接

        self.btn2 = QPushButton('關閉視窗', self)
        self.btn2.setGeometry(710, 10, 60, 30)
        self.btn2.clicked.connect(self.close)

        self.btn3 = QPushButton('存檔', self)
        self.btn3.setGeometry(640, 10, 60, 30)
        self.btn3.clicked.connect(self.save)

        self.btn4 = QPushButton('HSV', self)
        self.btn4.setGeometry(80, 10, 60, 30)
        self.btn4.clicked.connect(self.HSV)

        self.btn5 = QPushButton('模糊', self)
        self.btn5.setGeometry(150, 10, 60, 30)
        self.btn5.clicked.connect(self.blurre)

        self.btn6 = QPushButton('灰階', self)
        self.btn6.setGeometry(220, 10, 60, 30)
        self.btn6.clicked.connect(self.gray)

        self.btn7 = QPushButton('二值化', self)
        self.btn7.setGeometry(290, 10, 60, 30)
        self.btn7.clicked.connect(self.canny)

        self.btn8 = QPushButton('膨脹', self)
        self.btn8.setGeometry(360, 10, 60, 30)
        self.btn8.clicked.connect(self.dilated)

        self.btn9 = QPushButton('侵蝕', self)
        self.btn9.setGeometry(430, 10, 60, 30)
        self.btn9.clicked.connect(self.eroded)

        self.btn10 = QPushButton('高倍偵測', self)
        self.btn10.setGeometry(500, 10, 60, 30)
        self.btn10.clicked.connect(self.circle)

        self.btn11 = QPushButton('低倍偵測', self)
        self.btn11.setGeometry(570, 10, 60, 30)
        self.btn11.clicked.connect(self.circle1)

        self.label = QLabel('', self)
        self.label.setGeometry(10, 45, 554, 739)
        layout.addWidget(self.label)
        self.label2 = QLabel('', self)
        self.label2.setGeometry(574, 45, 554, 739)
        layout.addWidget(self.label2)

        self.setLayout(layout)
        self.setWindowTitle('圖片測試')


    def Show(self):  # 提取圖像的尺寸和通道，用於將opencv下的image轉換成Qimage
        print('trigger show')
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        # Format_RGB888該圖像是用一個24位讀RGB格式(8-8-8)存儲
        # rgbSwapped()紅色和藍色的組件值交換，將RGB轉為BGR

        # 將Qimage顯示出來
        self.label.setPixmap(QPixmap(self.qImg))
        self.label.setScaledContents(True)
    def refreshShow(self):
        height, width, _ = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.label2.setPixmap(QPixmap(self.qImg))
        self.label2.setScaledContents(True)

    def GRAYrefreshShow(self):
        height, width = self.img.shape
        self.qImg = QImage(self.img.data, width, height, width, QImage.Format_Grayscale8)

        self.label2.setPixmap(QPixmap(self.qImg))
        self.label2.setScaledContents(True)

    def open(self):

        File, _ = QFileDialog.getOpenFileName(self, "Open File", 'c:\\', "Image Files(*.jpg *jpeg *.png)")
        if File is '':
            return
        self.img = cv2.imread(File, -1)
        if self.img.size == 1:
            return
        self.Show()
        self.refreshShow()

    def HSV(self):  # HSV偵測
        if self.img.size == 1:
            return
        lower_green = np.array([30, 0, 0])
        upper_green = np.array([150, 255, 255])
        mask = cv2.inRange(self.img, lower_green, upper_green)
        self.img = cv2.bitwise_and(self.img, self.img, mask=mask)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定義元素結構(以3x3 5x5 7x7 來設定)
        self.img = cv2.dilate(self.img, kernel, 5)  # 膨脹(數字為次數)
        self.img = cv2.erode(self.img, kernel, 5)  # 侵蝕
        self.refreshShow()
    def save(self):
        Filesave,_=QFileDialog.getSaveFileName(self,"Save File","c:\\","Image Files(*.jpg *.jpeg *.png)")
        cv2.imwrite(Filesave,self.img)

    def blurre(self):
        if self.img.size ==1:
            return
        self.img=cv2.GaussianBlur(self.img,(9,9),0)
        self.refreshShow()
    def gray(self):
        if self.img.size == 1:
            return
        self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        if self.img.ndim==2:
            self.GRAYrefreshShow()
            self.img = cv2.cvtColor(self.img,cv2.COLOR_GRAY2BGR)

        else:
            self.refreshShow()
    def canny(self):
        if self.img.size == 1:
            return
        self.img = cv2.Canny(self.img,50,25)
        if self.img.ndim == 2:
            self.GRAYrefreshShow()
            self.img = cv2.cvtColor(self.img,cv2.COLOR_GRAY2BGR)
        else:
            self.refreshShow()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())