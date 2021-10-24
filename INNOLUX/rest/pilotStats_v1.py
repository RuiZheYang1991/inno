from threading import Thread
from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QImage,QPixmap
from PySide2 import QtGui
from PySide2 import QtWidgets
import sys
import pymssql
from datetime import datetime as dt
import configparser
from PySide2.QtGui import  QIcon
from pymssql import _mssql
from pymssql import _pymssql
import uuid
import decimal
import pandas as pd
#pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo\logo.ico"

def str_toDate(sdate):
    from datetime import datetime as dt
    Y=sdate[0:4]
    m=sdate[4:6]
    d=sdate[6:8]
    H=sdate[8:10]
    M=sdate[10:12]
    S=sdate[12:14]
    st=f'{Y}-{m}-{d}-{H}-{M}-{S}'


    date=dt.strptime(st,'%Y-%m-%d-%H-%M-%S')
    return date
def str_toDay(sdate):
    from datetime import datetime as dt
    Y=sdate[0:4]
    m=sdate[4:6]
    d=sdate[6:8]
    st=f'{Y}-{m}-{d}'
    #print(st)

    date=dt.strptime(st,'%Y-%m-%d')
    return date
class MSSQL():
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "沒有設置數據庫信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        # self.conn = pymssql.connect(host='localhost',user='sa',password='645713039', database='PythonWebServerDemo',charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "連接數據庫失敗")
        else:
            #print("連接數據庫成功")
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def Insert(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
        print("寫入完成")



# class CommonHelper:
#     def __init__(self):
#         pass
#     @staticmethod
#     def readQss(style):
#         with open(style, 'r') as f:
#             return f.read()
class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('ui/demo.ui')
        self.ui.setWindowTitle('MOD1確診足跡分析')
        self.ui.crawl.clicked.connect(self.get_date)
        self.ui.clearn.clicked.connect(self.clearn)
        self.ui.user_number.setPlaceholderText('請輸入工號')
        #self.ui.exportToExcel.clicked.connect(self.export_excel)
        self.ui.progressBar.setVisible(False)
        self.res = pymssql.connect(server='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', password='P@ss1234', database='CLTestDB')

        self.no_l = []
        self.name_l = []
        self.seat_l = []
        self.io_l = []
        self.time_l = []
        self.check_dic = {}
        # QSS_____________________
        # self.styleFile = 'qss\style.qss'
        # # 换肤时进行全局修改，只需要修改不同的QSS文件即可
        # self.style = CommonHelper.readQss(self.styleFile)
        # self.ui.setStyleSheet(self.style)
        # QSS_____________________

    def getInOut_time(self,num):
        I_time = ms.ExecQuery(f"select Time from OfficeCheckData where UserNo = {num} and IO = 'I'")
        O_time = ms.ExecQuery(f"select Time from OfficeCheckData where UserNo = {num} and IO = 'O'")
        name = ms.ExecQuery(f"select UserName from OfficeCheckData where UserNo = {num}")
        for i, y in zip(I_time, O_time):
            #print(f'{name[0][0]}  進入時間', str_toDate(i[0]), '  離開時間', str_toDate(y[0]))
            return f'{name[0][0]}  進入時間', str_toDate(i[0]), '  離開時間', str_toDate(y[0])

    def get_covid(self,num):
        df0 = pd.read_sql("select * from OfficeCheckData", self.res)
        df = pd.DataFrame(df0)
        for no, name, seat, io, timee in zip(df['UserNo'], df['UserName'], df['Seat'], df['IO'],
                                             df['Time']):

            if (len(self.name_l) == 0) and (io == "I"):
                self.no_l.append(no)
                self.name_l.append(name)
                self.seat_l.append(seat)
                self.io_l.append(io)
                self.time_l.append(timee)
                self.check_dic[no] = io
            else:
                # check_dic[no] = io
                # print(check_dic.get(no), io)
                if self.check_dic.get(no) != io:  # io == io_l[-1]
                    # print(check_dic.get(no),io)
                    self.no_l.append(no)
                    self.name_l.append(name)
                    self.seat_l.append(seat)
                    self.io_l.append(io)
                    self.time_l.append(timee)
                    self.check_dic[no] = io
                else:
                    pass
        rname = []
        rno = []
        rseat = []
        rtime = []
        rio = []
        for name, io, timee, number, seat in zip(self.name_l, self.io_l, self.time_l, self.no_l, self.seat_l):
            if number == num:
                rname.append(name)
                rno.append(number)
                rio.append(io)
                rseat.append(seat)
                rtime.append(timee)
        return rname, rno, rio, rseat, rtime
    def clearn(self):
        self.ui.show_data.clear()
        self.ui.show_data2.clear()
    def get_date(self):
        self.ui.progressBar.setVisible(True)
        start_qdate=self.ui.startDateEdit.dateTime()
        end_qdate = self.ui.endDateEdit.dateTime()
        int_start_date=int(start_qdate.toString('yyyyMMddHHmmss'))
        int_end_date = int(end_qdate.toString('yyyyMMddHHmmss'))
        #start_date=dt.strptime(str_start_date,'%Y-%m-%d-%H')
        #end_date = dt.strptime(str_end_date, '%Y-%m-%d-%H')
        self.ui.show_data.clear()
        self.ui.show_data2.clear()
        # self.day_set = set()
        # self.lapping_name = set()
        # self.lapping_seat = set()
        self.NG_seat = set()
        self.NG_time_zoon=[]
        num = self.ui.user_number.toPlainText()
        I_time = ms.ExecQuery(f"select Time,Seat from OfficeCheckData where UserNo = {num} and IO = 'I'")
        O_time = ms.ExecQuery(f"select Time,Seat from OfficeCheckData where UserNo = {num} and IO = 'O'")
        name = ms.ExecQuery(f"select UserName from OfficeCheckData where UserNo = {num}")
        all = ms.ExecQuery(f"select UserName,UserNo,Time,Seat from OfficeCheckData where IO = 'I'")


        if not (num.isdigit() and (len(num)==8)):
            print("請輸入正確工號")
            QMessageBox.critical(
                self.ui,
                '錯誤',
                '請輸入正確工號')
        else:

            try:
                print(int_start_date)
                self.ui.progressBar.setValue(20)
                #顯示show_data
                n,nu,i,s,t=self.get_covid(num)
                print(n)
                key=0
                for name,number,io,seat,timee in zip(n,nu,i,s,t):
                    key+=1
                    if int_start_date<int(timee)<int_end_date:
                        print(name,number,io,seat,timee)
                        self.ui.show_data.appendPlainText(f"{name} {number} {io} {seat} {timee}")
                        self.NG_time_zoon.append(int(timee))
                        self.NG_seat.add(seat)
                        if key%2==0:
                            for it in all:
                                if ((self.NG_time_zoon[0]-buffer*10000)<int(it[2])<(self.NG_time_zoon[1]+buffer*10000)) and (it[3] in self.NG_seat):
                                    self.ui.show_data2.appendPlainText(f'{it[0]}  {it[1]}   {it[2]}   {it[3]}')
                            self.NG_time_zoon=[]
                            self.NG_seat=set()
                    else:
                        pass
                    #f'{name[0][0]}  進入時間', str_toDate(i[0]), '  離開時間', str_toDate(y[0])
                #print(self.NG_seat)
                    self.ui.progressBar.setVisible(False)
                    self.ui.progressBar.reset()
                #顯示show_data2
                # try:
                #
                #     for ng_date in self.day_set:#確診者的日期
                #         for data in all:
                #
                #             if (ng_date == str_toDay(data[2])) and (data[3] in self.NG_seat):#匹配與確診者同一天進出
                #                 self.lapping_name.add(data[0])
                #                 #print(data[2], data[3])
                #
                #                 #print(all_data)
                #     #print(self.lapping_name)
                #     self.ui.progressBar.setValue(70)
                #     for lap in self.lapping_name:
                #
                #         set_namee = ms.ExecQuery(f"select UserName,UserNo,Time,Seat from OfficeCheckData where UserName = '{lap}'")
                #         self.ui.show_data2.appendPlainText(f'{set_namee[0][0]:<10}  {set_namee[0][1]}   {set_namee[0][3]}   {str_toDate(set_namee[0][2])}')
                #
                #     self.ui.progressBar.setValue(100)
                #     self.ui.progressBar.setVisible(False)
                #     self.ui.progressBar.reset()

                # except:
                #     QMessageBox.critical(
                #         self.ui,
                #         '錯誤',
                #         '足跡查詢失敗')
            # except:
            #     QMessageBox.critical(
            #         self.ui,
            #         '錯誤',
            #         '查無此人')



    # def overLapping(self):
    #
    #     start_qdate=self.ui.startDateEdit.dateTime()
    #     end_qdate = self.ui.endDateEdit.dateTime()
    #     str_start_date=start_qdate.toString('yyyy-MM-dd-HH')
    #     str_end_date = end_qdate.toString('yyyy-MM-dd-HH')
    #     start_date=dt.strptime(str_start_date,'%Y-%m-%d-%H')
    #     end_date = dt.strptime(str_end_date, '%Y-%m-%d-%H')
    #     self.ui.show_data.clear()
    #
    #     num = self.ui.user_number.toPlainText()
    #     if not (num.isdigit() and (len(num)==8)):
    #         print("請輸入正確工號")
    #         QMessageBox.critical(
    #             self.ui,
    #             '錯誤',
    #             '請輸入正確工號')
    #     else:
    #         try:
    #             I_time = ms.ExecQuery(f"select Time,Seat from OfficeCheckData where UserNo = {num} and IO = 'I'")
    #             O_time = ms.ExecQuery(f"select Time,Seat from OfficeCheckData where UserNo = {num} and IO = 'O'")
    #             name = ms.ExecQuery(f"select UserName from OfficeCheckData where UserNo = {num}")
    #             self.ui.show_data.appendPlainText(name[0][0])
    #             for i, y in zip(I_time, O_time):
    #                 if start_date<str_toDate(i[0])<end_date:
    #                     self.ui.show_data.appendPlainText(f'{i[1]}進入時間 {str_toDate(i[0])}   離開時間 {str_toDate(y[0])}')
    #                 #f'{name[0][0]}  進入時間', str_toDate(i[0]), '  離開時間', str_toDate(y[0])
    #
            except:
                QMessageBox.critical(
                    self.ui,
                    '錯誤',
                    '查無此人')

    # def export_excel(self):
    #     start_date = self.ui.startDateEdit.date()
    #     end_date = self.ui.endDateEdit.date()
    #     str_start_date = start_date.toString('yyyy-MM-dd')
    #     str_end_date = end_date.toString('yyyy-MM-dd')
    #     print(str_start_date)
    #     print(str_end_date)
    #     num = self.ui.user_number.toPlainText()
    #     if not (num.isdigit() and (len(num) == 8)):
    #         print("請輸入正確工號")
    #     else:
    #         try:
    #             print(num)
    #         except:
    #             print('資料庫連線失敗')

if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config['SQL']['host']
    user = config['SQL']['user']
    pwd = config['SQL']['pwd']
    db = config['SQL']['db']

    buffer=int(config['setting']['buffer'])
    ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\logo.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()