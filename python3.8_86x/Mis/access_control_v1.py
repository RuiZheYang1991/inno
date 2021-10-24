from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
import math
import pandas as pd
import multiprocessing
import datetime
from PySide2.QtGui import QIcon
import os
import pyautogui
import sys
import qdarkstyle
from PySide2.QtWidgets import QApplication, QMainWindow

#pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo\logo.ico"
from PySide2.QtWidgets import QButtonGroup
#a=QButtonGroup.buttonToggled()
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/dark_v1.ui')
        self.ui.setWindowTitle('人員管制')
        self.ui.vendor_name.returnPressed.connect(self.combine)
        self.ui.send_vendor.clicked.connect(self.combine)
        self.ui.clear_btn.clicked.connect(self.clear_all)
        self.ui.checkout.clicked.connect(self.check_out)
        self.vendor_l=[]
        self.inside_l=[]
        self.total_count=int(0)
        self.check_time={}
        self.vendor_num={}
        self.ui.vendor_name.setFocus()
        self.df = pd.read_excel('employee.xlsx')
    def get_data(self):
        name=self.get_userdata("name")

        if name not in self.inside_l:
            ctime = self.get_time()
            self.inside_l.append(name)
            self.check_time[name]=ctime
            self.total_count += 1

        else:

            self.inside_l.remove(name)
            self.check_time.pop(name)
            self.total_count -= 1
        self.ui.inside.clear()
        if (len(self.inside_l) !=0):


            for user_name in self.inside_l:
                mask = self.df['name'] == user_name
                dept = self.df[mask]['dept'].values[0]
                num = self.df[mask]['usernumber'].values[0]
                self.ui.inside.appendPlainText(f"{user_name}    {num}    {dept}    {self.check_time.get(user_name)}")
        else:
            pass

        if len(self.vendor_l) !=0:

            for user_name in self.vendor_l:
                self.ui.inside.appendPlainText(f"{user_name}   人數: {self.vendor_num[user_name]} 人    {self.check_time.get(user_name)}")

        else:
            pass
        self.ui.total_num.setText(f'{self.total_count}')
        text = self.ui.inside.toPlainText()
        if len(text) == 0:
            self.ui.total_num.setText('0')
        self.ui.vendor_name.clear()
        self.ui.vendor_name.setFocus()
    def vendor(self):
        self.ui.vendor_name.setText()
        self.ui.vendor_num.setText()
    def reset(self):
        self.ui.vendor_name.setFocus()

    def check_nan(self,meal):
        try:
            if math.isnan(meal):
                return True

        except:
            return False

    def get_time(self):

        datetime_dt = datetime.datetime.today()  # 獲得當地時間
        datetime_strr = datetime_dt.strftime("%m/%d %H:%M:%S")
        return datetime_strr

    def get_num(self):
        barcode = self.ui.vendor_name.text()
        try:
            user_num = int(barcode[-8:])
            return user_num
        except:

            return barcode

    def get_userdata(self,key):
        num=self.get_num()
        key=key
        mask = self.df['usernumber'] == num
        if key=="name":
            name = self.df[mask]['name'].values[0]
            return name
        if key=="dept":
            dept = self.df[mask]['dept'].values[0]
            return dept

    def get_vendorName(self):
        name=self.ui.vendor_name.text()
        return name
    def get_vendorNum(self):

        num=self.ui.spinBox.value()
        return num

    def show_vendor(self):
        if len(self.get_vendorName())==0:
            QMessageBox.critical(
                self.ui,
                'Error',
                '請輸入工號或廠商名稱')
            self.ui.vendor_name.setFocus()
            return
        else:
            name=self.get_vendorName()
        ctime=self.get_time()

        if name not in self.vendor_l:
            self.vendor_l.append(name)
            self.total_count+=self.get_vendorNum()
            self.check_time[name] = ctime
            self.vendor_num[name]=self.get_vendorNum()
            self.ui.checkout.setText(name+':  簽退')

        else:
            if self.vendor_num[name]-self.get_vendorNum() <= 0 :
                self.vendor_l.remove(name)
                self.total_count -= self.vendor_num[name]
                self.check_time.pop(name)
                self.vendor_num.pop(name)
                if len(self.vendor_l) != 0:
                    self.ui.checkout.setText(self.vendor_l[-1]+":  簽退")
                else:
                    self.ui.checkout.setText("廠商簽退")
            else:
                dig=self.vendor_num[name]-self.get_vendorNum()
                reduce={name:dig}
                self.total_count -= self.get_vendorNum()
                self.vendor_num.update(reduce)
        self.ui.inside.clear()
        if len(self.inside_l) !=0:
            for user_name in self.inside_l:
                mask = self.df['name'] == user_name
                dept = self.df[mask]['dept'].values[0]
                num = self.df[mask]['usernumber'].values[0]
                self.ui.inside.appendPlainText(f"{user_name}    {num}    {dept}    {self.check_time.get(user_name)}")
        else:
            pass

        if len(self.vendor_l) !=0:
            for user_name in self.vendor_l:
                self.ui.inside.appendPlainText(f"{user_name}   人數: {self.vendor_num[user_name]} 人    {self.check_time.get(user_name)}")

        else:
            pass

        text = self.ui.inside.toPlainText()

        self.ui.total_num.setText(f'{self.total_count}')
        if len(text) == 0:
            self.ui.total_num.setText(f'0')
            self.total_count=int(0)
        self.ui.vendor_name.clear()
        self.ui.vendor_name.setFocus()


    def clear_all(self):
        self.ui.inside.clear()
        self.vendor_l = []
        self.inside_l = []
        self.total_count = int(0)
        self.check_time = {}
        self.vendor_num = {}
        self.ui.vendor_name.clear()
        self.ui.total_num.setText(f'0')
        self.ui.checkout.setText("廠商簽退")
        self.ui.vendor_name.setFocus()


    def combine(self):
        try:
            self.get_data()
        except:
            self.show_vendor()

    def check_out(self):

        if len(self.vendor_l) ==0:
            self.ui.checkout.setText("廠商簽退")
            self.ui.vendor_name.setFocus()
            return
        checkout=self.ui.checkout.text()

        if checkout == "廠商簽退":
            self.ui.vendor_name.setFocus()
            return
        name = checkout.split(':')[0]
        self.total_count-=self.vendor_num[name]
        self.vendor_l.remove(name)
        self.check_time.pop(name)
        self.vendor_num.pop(name)
        self.ui.inside.clear()
        if len(self.inside_l) !=0:
            for user_name in self.inside_l:
                mask = self.df['name'] == user_name
                dept = self.df[mask]['dept'].values[0]
                num = self.df[mask]['usernumber'].values[0]
                self.ui.inside.appendPlainText(f"{user_name}    {num}    {dept}    {self.check_time.get(user_name)}")
        else:
            pass

        if len(self.vendor_l) !=0:
            for user_name in self.vendor_l:
                self.ui.inside.appendPlainText(f"{user_name}   人數: {self.vendor_num[user_name]} 人    {self.check_time.get(user_name)}")
        else:
            pass

        if len(self.vendor_l) !=0:
            self.ui.checkout.setText(self.vendor_l[-1]+":  簽退")
        else:
            self.ui.checkout.setText("廠商簽退")


        text = self.ui.inside.toPlainText()
        self.ui.total_num.setText(f'{self.total_count}')
        if len(text) == 0:
            self.ui.total_num.setText(f'0')
            self.total_count=int(0)
        self.ui.vendor_name.clear()
        self.ui.vendor_name.setFocus()
if __name__=='__main__':
    multiprocessing.freeze_support()
    app = QApplication([])
    app.setWindowIcon(QIcon('ui\logo.png'))
    stats = Stats()
    stats.ui.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    #stats.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))
    stats.ui.showFullScreen()
    app.exec_()