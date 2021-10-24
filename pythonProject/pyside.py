from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import numpy as np
import numpy.core._dtype_ctypes
import cv2
import sys


class CV:
    def __init__(self):
        qfile=QFile("ui/cvqtt.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.img = np.zeros(1)
        self.ui=QUiLoader().load(qfile)


        self.ui.open_btn.clicked.connect(self.open)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.hsv_btn.clicked.connect(self.HSV)
        self.ui.blure_btn.clicked.connect(self.blurre)
        self.ui.circle_btn.clicked.connect(self.circle)
        self.ui.circle1_btn.clicked.connect(self.circle1)
        self.ui.gray_btn.clicked.connect(self.gray)
        self.ui.canny_btn.clicked.connect(self.canny)
        self.ui.dilate_btn.clicked.connect(self.dilated)
        self.ui.erode_btn.clicked.connect(self.eroded)

        layout = QVBoxLayout()
        self.ui.label = QLabel('', self.ui)
        self.ui.label.setGeometry(10, 100, 500, 500)
        layout.addWidget(self.ui.label)
        self.ui.label2 = QLabel('', self.ui)
        self.ui.label2.setGeometry(574, 100, 500, 500)
        layout.addWidget(self.ui.label2)

        self.ui.setLayout(layout)
        self.ui.setWindowTitle('圖片測試')

    def Show(self):  # 提取圖像的尺寸和通道，用於將opencv下的image轉換成Qimage
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        # Format_RGB888該圖像是用一個24位讀RGB格式(8-8-8)存儲
        # rgbSwapped()紅色和藍色的組件值交換，將RGB轉為BGR

        # 將Qimage顯示出來
        self.ui.label.setPixmap(QPixmap(self.qImg))
        self.ui.label.setScaledContents(True)

    def refreshShow(self):
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        self.ui.label2.setPixmap(QPixmap(self.qImg))
        self.ui.label2.setScaledContents(True)

    def GRAYrefreshShow(self):
        height, width = self.img.shape
        self.qImg = QImage(self.img.data, width, height, width,
                           QImage.Format_Grayscale8)
        self.ui.label2.setPixmap(QPixmap.fromImage(self.qImg))
        self.ui.label2.setScaledContents(True)

    # 開啟檔案
    def open(self):
        File, _ = QFileDialog.getOpenFileName(self.ui, 'Open File', r'c:\\', 'Image File(*.jpg *jpeg *.png)')

        if File is '':
            return  # return 沒有接東西就是回傳None, 但寫return相當於結束方法,後續程式不會執行
        self.img = cv2.imread(File, -1)
        if self.img.size == 1:
            return
        self.Show()
        self.refreshShow()

    # 關閉
    def close(self):
        sys.exit(app.exec_())

    # 存檔
    def save(self):
        FileSave, _ = QFileDialog.getSaveFileName(self.ui, 'Save File', r'c:\\', 'Image Files(*.jpg *jpeg *.png)')
        if FileSave is '':
            return  # 沒有這段取消存檔會掛掉
        cv2.imwrite(FileSave, self.img)

    # HSV 色彩空間
    def HSV(self):
        if self.img.size == 1:
            return
        lower_green = np.array([30, 0, 0])
        upper_green = np.array([150, 255, 255])
        mask = cv2.inRange(self.img, lower_green, upper_green)
        self.img = cv2.bitwise_and(self.img, self.img, mask=mask)
        # 定義元素結構以(3*3,5*5,7*7)設定
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        # 膨脹(圖片,結構,數字是次數)
        self.img = cv2.dilate(self.img, kernel, 5)
        # 侵蝕
        self.img = cv2.erode(self.img, kernel, 5)
        self.refreshShow()  # 因為影像效果是疊加的,所以每次都需要refreshShow.

    # 模糊
    def blurre(self):
        if self.img.size == 1:
            return
        self.img = cv2.GaussianBlur(self.img, (9, 9), 0)  # 高斯模糊
        if self.img.ndim == 2:
            self.GRAYrefreshShow()
        else:
            self.refreshShow()

    # 灰階
    def gray(self):
        if self.img.size == 1 or self.img.ndim == 2:
            return
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        if self.img.ndim == 2:
            self.GRAYrefreshShow()
        else:
            self.refreshShow()

    # 二值化
    def canny(self):
        if self.img.size == 1:
            return
        self.img = cv2.Canny(self.img, 50, 25)  # 閥值1,閥值2
        if self.img.ndim == 2:
            self.GRAYrefreshShow()
        else:
            self.refreshShow()

    # 膨脹
    def dilated(self):
        if self.img.size == 1:
            return
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定義結構
        self.img = cv2.dilate(self.img, kernel, 1)  # (圖片,結構,次數)
        if self.img.ndim == 2:
            self.GRAYrefreshShow()
        else:
            self.refreshShow()

    # 侵蝕
    def eroded(self):
        if self.img.size == 1:
            return
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定義結構
        self.img = cv2.erode(self.img, kernel, 1)
        if self.img.ndim == 2:
            self.GRAYrefreshShow()
        else:
            self.refreshShow()

    # 高倍偵測
    def circle(self):
        if self.img.size == 1:
            return
        circle = cv2.HoughCircles(self.img, cv2.HOUGH_GRADIENT, 1, 15, param1=50, param2=20, minRadius=5, maxRadius=30)
        # 影像,偵測方式,疊加器圖像,圓心最小距離,最高閥值,(默認100,此值一半為低閥值),偵測圓形(默認100,數值越大越接近完美的圓),最小圓半徑,最大圓半徑
        i = 0
        if circle is not None:
            for c in circle:
                for x, y, r in c:
                    cv2.line(self.img, (x + r + r + r, y + r + r), (x + r, y + r), (255, 255, 255), 2)
                    cv2.line(self.img, (x + r, y + r), (x + r + r, y + r + r), (255, 255, 255), 2)
                    cv2.line(self.img, (x + r + r, y + r + r + r), (x + r + r + r, y + r + r), (255, 255, 255), 2)
                    if (x > 0 and y > 0):
                        i + 1
                        print("總數:", i)
        cv2.putText(self.img, 'Quantity:', (10, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
        # 影像,文字,座標,字型,大小,顏色,線條寬度,線條種類
        cv2.putText(self.img, str(i), (330, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
        self.GRAYrefreshShow()

    # 低倍偵測
    def circle1(self):
        if self.img.size == 1:
            return
        circle = cv2.HoughCircles(self.img, cv2.HOUGH_GRADIENT, 1, 5, param1=50, param2=13, minRadius=2, maxRadius=20)
        # 影像,偵測方式,疊加器圖像,圓心最小距離,最高閥值,(默認100,此值一半為低閥值),偵測圓形(默認100,數值越大越接近完美的圓),最小圓半徑,最大圓半徑
        i = 0
        if circle is not None:
            for c in circle:
                for x, y, r in c:
                    cv2.line(self.img, (x + r + r + r, y + r + r), (x + r, y + r), (255, 255, 255), 2)
                    cv2.line(self.img, (x + r, y + r), (x + r + r, y + r + r), (255, 255, 255), 2)
                    cv2.line(self.img, (x + r + r, y + r + r + r), (x + r + r + r, y + r + r), (255, 255, 255), 2)
                    if (x > 0 and y > 0):
                        i + 1
                        print("總數:", i)
        cv2.putText(self.img, 'Quantity:', (10, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
        # 影像,文字,座標,字型,大小,顏色,線條寬度,線條種類
        cv2.putText(self.img, str(i), (330, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
        self.GRAYrefreshShow()

if __name__ == '__main__':
    print("Program start")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/logo.jpg"))
    window=CV()
    window.ui.show()
    app.exec_()