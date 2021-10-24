import threading
from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
import uuid
import decimal
import pandas as pd
from glob import glob
from decimal import Decimal
import configparser
import qdarkstyle
from datetime import datetime
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


class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/dark.ui')
        self.ui.setWindowTitle('熱感應分析')
        self.ui.crawl.clicked.connect(self.search_all)
        self.ui.save.clicked.connect(self.save_tread)
        self.ui.clearn.clicked.connect(self.clearn)
        self.ui.PID_btn.clicked.connect(self.search_pid_tread)

    def search_pid(self):
        pid=self.ui.PID.text()
        if len(pid) == 0:
            QMessageBox.critical(
                self.ui,
                '錯誤',
                '請輸入PID！')
        else:
            self.ui.show_data.clear()
            self.ui.show_data2.clear()
            try:
                single_df = self.combine_single(path, idx=idxx)
                double_df = self.combine_double(path, idx=idxx)
                mask=single_df['PID']==pid
                if len(single_df[mask]) != 0 :

                    self.ui.show_data.appendPlainText(f'                  PID   PCB1   Pannel1   Grade  Time')
                    self.ui.show_data.appendPlainText('\n')
                    for i in single_df[mask].values:

                        self.ui.show_data.appendPlainText(
                            f'{i[0]}   {i[1]}      {i[2]}       {i[3]}     {str(i[4]).split(" ")[0]}')
                    self.ui.show_data.appendPlainText('\n')
                mask2=double_df['PID']==pid
                if len(double_df[mask2]) != 0 :
                    self.ui.show_data.appendPlainText(f'                  PID   PCB1   Pannel1   PCB2   Pannel2   Grade  Time')
                    self.ui.show_data.appendPlainText('\n')
                    for i in double_df[mask2].values:

                        self.ui.show_data2.appendPlainText(f'{i[0]}   {i[1]}      {i[2]}      {i[3]}      {i[4]}        {i[5]}      {str(i[6]).split(" ")[0]}')

                if len(single_df[mask]) == 0 and len(double_df[mask2]) == 0 :
                    self.ui.show_data.appendPlainText('查無資料')
            except:
                QMessageBox.warning(
                    self.ui,
                    '注意',
                    '請檢查圖片路徑')

    def clearn(self):
        self.ui.show_data.clear()
        self.ui.show_data2.clear()

    def get_now(self):

        return datetime.today().strftime('%Y%m%d')

    def tofloat(self,num):
        dec = Decimal(str(num))
        return round(dec, 1)

    def sTodate(self,sdate):
        date = datetime.strptime(sdate, "%Y-%m-%d")
        return date

    def single(self,path, idx):
        l = glob(path)

        pid_l = []
        pcb_l = []
        pannel_l = []
        grade_l = []
        date_l = []
        for i in l:
            if len(i.split(';')) == 2:
                file_name = i.split('\\')[idx]
                pid = file_name.split('_')[1]
                grade = file_name.split('_')[3]
                #pcb = file_name.split('_')[4].split(';')[0].split(',')[0]
                pcb_thermal = self.tofloat(file_name.split(',')[1])
                pannel_thermal = self.tofloat(file_name.split(',')[3])
                sdate = file_name.split('_')[0]

                date = self.sTodate(sdate)
                pid_l.append(pid)
                pcb_l.append(pcb_thermal)
                pannel_l.append(pannel_thermal)
                grade_l.append(grade)
                date_l.append(date)
                # print(pcb_thermal)

                # print(date)
        data = {'PID': pid_l, 'PCB1': pcb_l, 'Pannel1': pannel_l, 'Grade': grade_l, "Date": date_l}

        df = pd.DataFrame(data)
        mask = df['Grade'] == "NG"
        # print("-----------------------------NG--------------------------")
        # print(df[mask])
        # print("-----------------------------NG--------------------------")
        return df

    def double(self,path, idx=3):
        l = glob(path)
        pid_l = []
        pcb1_l = []
        pannel1_l = []
        pcb2_l = []
        pannel2_l = []
        grade_l = []
        date_l = []


        for i in l:
            if len(i.split(';')) == 4:
                # print(i)
                # print(len(i))
                file_name = i.split('\\')[idx]
                # print(len(file_name.split(';')))
                pid = file_name.split('_')[1]
                grade = file_name.split('_')[3]
                #pcb = file_name.split('_')[4].split(';')[0].split(',')[0]
                pcb_thermal1 = self.tofloat(file_name.split(',')[1])
                pannel_thermal1 = self.tofloat(file_name.split(',')[3])
                pcb_thermal2 = self.tofloat(file_name.split(',')[5])

                pannel_thermal2 = self.tofloat(file_name.split(',')[7])
                sdate = file_name.split('_')[0]
                date = self.sTodate(sdate)
                pid_l.append(pid)
                pcb1_l.append(pcb_thermal1)
                pannel1_l.append(pannel_thermal1)
                pcb2_l.append(pcb_thermal2)
                pannel2_l.append(pannel_thermal2)
                grade_l.append(grade)
                date_l.append(date)

            # print(pcb_thermal1)
            # print(pannel_thermal1)
        data = {'PID': pid_l, 'PCB1': pcb1_l, 'Pannel1': pannel1_l, 'PCB2': pcb2_l, 'Pannel2': pannel2_l,
                'Grade': grade_l, "Date": date_l}

        df = pd.DataFrame(data)
        #mask = df['Grade'] == "NG"
        # print("--------------------NG-------------------------")
        # print(df[mask])
        return df

    def combine_single(self,path, key=0, idx=3):
        path_l = glob(path)
        df = pd.DataFrame()
        for path in path_l:
            # print(f'{path}\\*')
            df1 = self.single(f'{path}\\*', idx)
            df = df.append([df1])
        mask = df["Grade"] == "NG"
        if key == ("ng" or "NG"):
            return df[mask].reset_index(drop=True)
        else:
            return df.reset_index(drop=True)

    def combine_double(self,path, key=0, idx=3):
        path_l = glob(path)
        df = pd.DataFrame()

        for pathh in path_l:
            df1 = self.double(f'{pathh}\\*', idx)
            df = df.append([df1])

        mask = df["Grade"] == "NG"
        if key == ("ng" or "NG"):
            return df[mask].reset_index(drop=True)
        else:
            return df.reset_index(drop=True)

    def combine_all(self):
        try:
            self.ui.show_data.clear()
            self.ui.show_data2.clear()
            start_qdate = self.ui.startDateEdit.date()
            end_qdate = self.ui.endDateEdit.date()
            single_df=self.combine_single(path,idx=idxx)
            double_df=self.combine_double(path,idx=idxx)

            self.ui.show_data.appendPlainText(f'                  PID   PCB1   Pannel1   Grade  Time')
            self.ui.show_data.appendPlainText('\n')
            for i in single_df.values:
                if start_qdate <= i[4] <= end_qdate:
                    self.ui.show_data.appendPlainText(f'{i[0]}   {i[1]}      {i[2]}       {i[3]}     {str(i[4]).split(" ")[0]}')
            self.ui.show_data.appendPlainText('\n')
            self.ui.show_data.appendPlainText(f'                  PID   PCB1   Pannel1   PCB2   Pannel2   Grade  Time')
            self.ui.show_data.appendPlainText('\n')
            for i in double_df.values:
                if start_qdate <= i[6] <= end_qdate:
                    self.ui.show_data.appendPlainText(f'{i[0]}   {i[1]}      {i[2]}      {i[3]}      {i[4]}        {i[5]}      {str(i[6]).split(" ")[0]}')
                #print(i)

            single_dfng = self.combine_single(path,key='ng',idx=idxx)
            double_dfng = self.combine_double(path,key='ng',idx=idxx)

            self.ui.show_data2.appendPlainText(f'                  PID   PCB1   Pannel1   Grade  Time')
            self.ui.show_data2.appendPlainText('\n')


            for i in single_dfng.values:


                if start_qdate<= i[4] <=end_qdate:
                    self.ui.show_data2.appendPlainText(f'{i[0]}   {i[1]}      {i[2]}       {i[3]}     {str(i[4]).split(" ")[0]}')
            self.ui.show_data2.appendPlainText('\n')
            self.ui.show_data2.appendPlainText(f'                  PID   PCB1   Pannel1   PCB2   Pannel2   Grade  Time')
            self.ui.show_data2.appendPlainText('\n')
            for i in double_dfng.values:
                if start_qdate <= i[6] <= end_qdate:
                    self.ui.show_data2.appendPlainText(f'{i[0]}   {i[1]}      {i[2]}      {i[3]}      {i[4]}        {i[5]}      {str(i[6]).split(" ")[0]}')
        except:
            QMessageBox.warning(
                self.ui,
                '注意',
                '請檢查圖片路徑')


    def save_data(self):

        self.ui.show_data.clear()
        self.ui.show_data2.clear()
        self.combine_all()
        start_qdate = self.ui.startDateEdit.date()
        end_qdate = self.ui.endDateEdit.date()
        single_df = self.combine_single(path,idx=idxx)
        double_df = self.combine_double(path,idx=idxx)

        mask=single_df["Date"] <= end_qdate.toString("yyyy-MM-dd")
        mask2=start_qdate.toString("yyyy-MM-dd") <single_df["Date"]
        filter_singal_df=single_df[(mask | mask2)]

        mask = double_df["Date"] <= end_qdate.toString("yyyy-MM-dd")
        mask2 = start_qdate.toString("yyyy-MM-dd") <= double_df["Date"]
        filter_double_df=double_df[(mask | mask2)]
        all_df=filter_double_df.append(filter_singal_df).reset_index(drop=True)
        all_df.to_excel(f'all_data {self.get_now()}.xlsx')
        singal_ng=filter_singal_df[filter_singal_df["Grade"]=="NG"]
        double_ng=filter_double_df[filter_double_df["Grade"]=="NG"]
        ng_df=double_ng.append(singal_ng).reset_index(drop=True)
        ng_df.to_excel(f'ng_data {self.get_now()}.xlsx')

        QMessageBox.information(
            self.ui,
            '成功',
            '檔案已儲存')

    def save_tread(self):
        thread = threading.Thread(target=self.save_data())
        thread.setDaemon(True)
        thread.start()

    def search_pid_tread(self):

        thread = threading.Thread(target=self.search_pid())
        thread.setDaemon(True)
        thread.start()

    def search_all(self):
        thread = threading.Thread(target=self.combine_all())
        thread.setDaemon(True)
        thread.start()
if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('ui\config.ini',encoding='utf8')
    path = config['setting']['path']
    idxx= int(config['setting']['idx'])
    app = QApplication([])
    app.setWindowIcon(QIcon('ui\logo.png'))
    stats = Stats()
    stats.ui.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    stats.ui.show()
    app.exec_()