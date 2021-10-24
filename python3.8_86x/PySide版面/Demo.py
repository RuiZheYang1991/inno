
import socket
from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
import threading
from PySide2.QtCore import Signal,QObject
from PySide2.QtGui import QIcon,QPixmap
import configparser
import os
import serial
import time
import writeLog
# from pymssql import _mssql
# from pymssql import _pymssql
# import multiprocessing
# import uuid
# import decimal


def is_float(s):
    s = str(s)
    if s.count('.')==1:#判斷小數點個數
        sl = s.split('.')#按照小數點進行分割
        left = sl[0]#小數點前面的
        right = sl[1]#小數點後面的
        if left.isdigit() and right.isdigit():
            return True
    return False


class Stats:
    def __init__(self,port,baud):
        self.ui = QUiLoader().load('ui/main.ui')
        self.ui.setWindowTitle('門禁UI')
        #self.ui.pic1.setPixmap(QPixmap(r"img\images.jpg"))
        self.port = port
        self.baud = int(baud)
        self.open_com = None
        self.log = writeLog.WriteLog('ITC_LOG.LOG')
        self.get_data_flag = True
        self.real_time_data = ''



    def get_real_time_data(self):
        return self.real_time_data

    def clear_real_time_data(self):
        self.real_time_data = ''

    # set flag to receive data or not
    def set_get_data_flag(self, get_data_flag):
        self.get_data_flag = get_data_flag

    def open(self):
        try:
            self.open_com = serial.Serial(self.port, self.baud)
        except Exception as e:
            self.log.error('Open com fail:{}/{}'.format(self.port, self.baud))
            self.log.error('Exception:{}'.format(e))

    def close(self):
        if self.open_com is not None and self.open_com.isOpen:
            self.open_com.close()

    def send_data(self, data):
        if self.open_com is None:
            self.open()
        success_bytes = self.open_com.write(data.encode('UTF-8'))
        return success_bytes

    def get_data(self, over_time=30):
        all_data = ''
        if self.open_com is None:
            self.open()
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time < over_time and self.get_data_flag:
                data = self.open_com.read(self.open_com.inWaiting())
                # data = self.open_com.read() # read 1 size
                data = str(data)
                if data != '':
                    self.log.info('Get data is:{}'.format(data))
                    all_data = all_data + data
                    print(data)
                    self.real_time_data = all_data
            else:
                self.set_get_data_flag(True)
                break
        return all_data


    def printToGui(self, fb, text):
        fb.append(str(text))
        fb.ensureCursorVisible()

    def send_name(self, name, loc):
        def send_user_name():
            if loc == '1':
                self.ui.name1.setText(str(name))
            elif loc == '2':
                self.ui.name2.setText(str(name))
            elif loc == '3':
                self.ui.name3.setText(str(name))

        thread = threading.Thread(target=send_user_name)
        thread.setDaemon(True)#關閉程式同時關閉執行續
        thread.start()

    def send_num(self, num, loc):
        def send_user_num():
            if loc == '1':
                self.ui.num1.setText(str(num))
            elif loc == '2':
                self.ui.num2.setText(str(num))
            elif loc == '3':
                self.ui.num3.setText(str(num))

        thread = threading.Thread(target=send_user_num)
        thread.setDaemon(True)
        thread.start()

    def send_temp(self, temp, loc):
        def send_user_temp():
            if loc == '1':
                self.ui.temp1.setStyleSheet("color:green")
                self.ui.temp1.setText(str(temp))
            elif loc == '2':
                self.ui.temp2.setStyleSheet("color:green")
                self.ui.temp2.setText(str(temp))
            elif loc == '3':
                self.ui.temp3.setStyleSheet("color:green")
                self.ui.temp3.setText(str(temp))

        thread = threading.Thread(target=send_user_temp)
        thread.setDaemon(True)
        thread.start()


    def send_NGtemp(self, temp, loc):
        def send_user_temp():
            if loc == '1':
                self.ui.temp1.setStyleSheet("color:red")
                self.ui.temp1.setText(str(temp))
            elif loc == '2':
                self.ui.temp2.setStyleSheet("color:red")
                self.ui.temp2.setText(str(temp))
            elif loc == '3':
                self.ui.temp3.setStyleSheet("color:red")
                self.ui.temp3.setText(str(temp))

        thread = threading.Thread(target=send_user_temp)
        thread.setDaemon(True)
        thread.start()
    def send_pic(self,path, loc):
        def send_user_pic():
            try:
                if loc == '1' and os.path.isfile(path):
                    self.ui.pic1.setPixmap(QPixmap(path))
                elif loc == '2' and os.path.isfile(path):
                    self.ui.pic2.setPixmap(QPixmap(path))
                elif loc == '3' and os.path.isfile(path):
                    self.ui.pic3.setPixmap(QPixmap(path))
            except:
                if loc == '1':
                    self.ui.pic1.setPixmap(QPixmap(r"img\images.jpg"))
                elif loc == '2':
                    self.ui.pic2.setPixmap(QPixmap(r"img\images.jpg"))
                elif loc == '3':
                    self.ui.pic3.setPixmap(QPixmap(r"img\images.jpg"))


        thread = threading.Thread(target=send_user_pic)
        thread.setDaemon(True)
        thread.start()



if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    #com = Stats(port= 'com3', baud=115200)
    # com.open()
    # print(com.send_data('data'))
    # com.get_data(50)
    # com.close()
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\images.png'))
    stats = Stats(port= 'com3', baud=115200)
    stats.open()
    print(stats.send_data('data'))
    stats.get_data(50)
    stats.close()
    stats.ui.show()
    app.exec_()






























