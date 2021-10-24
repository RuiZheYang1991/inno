from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
import math
import pandas as pd
import multiprocessing
import datetime
import configparser
from PySide2.QtGui import QIcon
import os

#pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo\logo.ico"
from PySide2.QtWidgets import QButtonGroup
#a=QButtonGroup.buttonToggled()
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/rwd.ui')
        self.ui.setWindowTitle('人員管制')
        self.ui.text.returnPressed.connect(self.get_data)
        self.ui.vendor_name.returnPressed.connect(self.show_vendor)
        self.ui.send_vendor.clicked.connect(self.show_vendor)
        self.ui.clear_btn.clicked.connect(self.clear_all)
        self.vendor_l=[]
        self.inside_l=[]
        self.total_count=int(0)
        self.check_time={}
        self.ui.text.setFocus()
    def get_data(self):
        df = pd.read_excel('employee.xlsx')
        name=self.get_userdata("name")
        print(name)
        if name not in self.inside_l:
            ctime = self.get_time()
            self.inside_l.append(name)
            self.check_time[name]=ctime
            self.total_count += 1
            print(self.check_time)
        else:

            self.inside_l.remove(name)
            self.check_time.pop(name)
            self.total_count -= 1
        self.ui.inside.clear()
        if len(self.inside_l) !=0:
            for user_name in self.inside_l:
                mask = df['name'] == user_name
                dept = df[mask]['dept'].values[0]
                num = df[mask]['usernumber'].values[0]
                self.ui.inside.appendPlainText(f"{user_name}    {num}    {dept}    {self.check_time.get(user_name)}")
        else:
            pass

        if len(self.vendor_l) !=0:
            for user_name in self.vendor_l:
                self.ui.inside.appendPlainText(f"{user_name}   {self.check_time.get(user_name)}    入場人數:{num}人")

        else:
            pass
        self.ui.total_num.setText(f'{self.total_count}')
        text = self.ui.inside.toPlainText()
        if len(text) == 0:
            self.ui.total_num.setText('0')
        self.ui.text.clear()
        self.ui.text.setFocus()
    def vendor(self):
        self.ui.vendor_name.setText()
        self.ui.vendor_num.setText()
    def reset(self):
        self.ui.text.setFocus()

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
        barcode = self.ui.text.text()
        try:
            user_num = int(barcode[-8:])
        except:


            self.ui.text.clear()
            self.ui.text.setFocus()
            return
        return user_num

    def get_userdata(self,key):
        num=self.get_num()
        df = pd.read_excel('employee.xlsx')
        key=key
        mask = df['usernumber'] == num
        if key=="name":
            name = df[mask]['name'].values[0]
            return name
        if key=="dept":
            dept = df[mask]['dept'].values[0]
            return dept

    def get_vendorName(self):
        name=self.ui.vendor_name.text()
        return name
    def get_vendorNum(self):
        # num=self.ui.vendor_number.text()
        num=self.ui.spinBox.value()
        print(num)
        print(type(num))
        return num

    def show_vendor(self):

        df = pd.read_excel('employee.xlsx')
        if len(self.get_vendorName())==0:
            QMessageBox.critical(
                self.ui,
                'Error',
                '請輸入廠商名稱')
            self.ui.text.setFocus()
            return
        else:
            name=self.get_vendorName()
        # try:
        #     num=self.get_vendorNum()
        # except:
        #     QMessageBox.critical(
        #         self.ui,
        #         'Error',
        #         '請輸入數字')
        #     self.ui.text.setFocus()
        #     return
        ctime=self.get_time()

        if name not in self.vendor_l:
            self.vendor_l.append(name)
            self.total_count+=self.get_vendorNum()
            self.check_time[name] = ctime
        else:
            self.vendor_l.remove(name)
            self.total_count -= self.get_vendorNum()
            self.check_time.pop(name)
        self.ui.inside.clear()
        if len(self.inside_l) !=0:
            for user_name in self.inside_l:
                mask = df['name'] == user_name
                dept = df[mask]['dept'][0]
                num = df[mask]['usernumber'][0]
                self.ui.inside.appendPlainText(f"{user_name}    {num}    {dept}    {self.check_time.get(user_name)}\n")
        else:
            pass

        if len(self.vendor_l) !=0:
            for user_name in self.vendor_l:
                self.ui.inside.appendPlainText(f"{user_name}   {self.check_time.get(user_name)}    入場人數:{self.get_vendorNum()}人\n")

        else:
            pass

        text = self.ui.inside.toPlainText()

        self.ui.total_num.setText(f'{self.total_count}')
        if len(text) == 0:
            self.ui.total_num.setText(f'0')
            self.total_count=int(0)
        self.ui.text.clear()
        self.ui.text.setFocus()
        # print(num,name)
        # print(self.total_count)
    def get_totalNum(self):
        pass


    def clear_all(self):
        self.ui.inside.clear()
        self.vendor_l = []
        self.inside_l = []
        self.total_count = int(0)
        self.check_time = {}
        self.ui.text.clear()
        self.ui.vendor_name.clear()
        self.ui.total_num.setText(f'0')
        self.ui.text.setFocus()

if __name__=='__main__':
    multiprocessing.freeze_support()
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\logo.jpg'))
    stats = Stats()
    stats.ui.showFullScreen()
    app.exec_()