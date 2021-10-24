from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
import math
import pandas as pd
import multiprocessing
import pymssql
from datetime import datetime as dt
import datetime
import configparser
from PySide2.QtGui import QIcon
#pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo\logo.ico"
from PySide2.QtWidgets import QButtonGroup
#a=QButtonGroup.buttonToggled()
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/food_time.ui')
        self.ui.setWindowTitle('刷餐系統')
        self.ui.text.returnPressed.connect(self.get_data)
        #self.ui.buttonGroup.buttonClicked.connect(self.reset)
        #self.sheetCombo=self.ui.sheet.currentText()
        #self.sheetCombo=self.ui.buttonGroup.text()
        #self.ui.buttonGroup.buttonToggled(self.reset)
        #self.btn=self.ui.buttonGroup.checkedButton().text()
        self.datetime_dt = datetime.datetime.today()  # 獲得當地時間
        self.datetime_strr = self.datetime_dt.strftime("%Y/%m/%d %H:%M:%S")
        self.date_str = self.datetime_dt.strftime("%Y%m%d")
        self.bf=bf
        self.lunch=lunch
        self.dinner=dinner
        self.sup=sup
        self.buffer=buffer
        #print(self.datetime_strr)
        #print(self.time_check(datetime_dt=self.datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))
        #print(self.ui.buttonGroup.checkedButton())
    def get_data(self):
        #self.btn = self.ui.buttonGroup.checkedButton().text()
        self.ui.food.clear()
        self.ui.name.clear()
        self.ui.number.clear()
        barcode = self.ui.text.text()
        try:
            num=int(barcode[-8:])
        except:
            self.ui.food.appendPlainText("工號格式錯誤")
            #self.ui.food.appendPlainText("查無此人")
            self.ui.text.clear()
            return

        try:
            #print(self.time_check(datetime_dt=self.datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))
            df = pd.read_excel(file, usecols="H,I,K,M",sheet_name=self.time_check(datetime_dt=self.datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))#
        except:
            self.ui.food.appendPlainText("Data Error")
            #print("Data Error")
            return
        try:
            # if num in df['員工號碼\nEmployee No.'].values:
            #     mask = df['員工號碼\nEmployee No.'] == num
            #     idx = df[mask].index[0]
            #     name = df.loc[idx, "姓名\nName"]
            #     meal = df.loc[idx, "備註\nA.B.C\n素食"]
            if num in df['員工號碼\nEmployee No.'].values:
                mask = df['員工號碼\nEmployee No.'] == num
                idx = df[mask].index[0]
                name = df.loc[idx, "姓名\nName"]
                meal = df.loc[idx, "備註\nA.B.C\n素食"]
                # print(type(meal))
                # print(meal)
                # print(self.check_nan(meal))
                if self.check_nan(meal) or (meal==None) or (meal==" "):
                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText("You did not \nOrder the meal")
                    self.ui.food.appendPlainText("未訂餐")
                    self.ui.text.clear()
                    with open(f'{self.date_str}.txt', mode='a', encoding="utf-8") as f:
                        f.write(str(df[mask].values[0][0]) + ",")
                        f.write(df[mask].values[0][1] + ",")
                        f.write(df[mask].values[0][2][:2]+",")
                        f.write(f"{self.datetime_strr}"+"\n")

                else:

                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText(f"           Meal: {meal}\n      Thank You!")
                    #self.ui.food.appendPlainText("Thank You")
                    self.ui.text.clear()
            else:
                self.ui.food.appendPlainText("No Data")
                self.ui.number.setText("???")
                self.ui.name.setText("???")

                #self.ui.food.appendPlainText("查無此人")

                ng_num = self.ui.text.text()
                self.ui.text.clear()
                with open(f'{self.date_str}.txt', mode='a', encoding="utf-8") as f:
                    f.write(str(ng_num) + ",")
                    f.write(f"{self.datetime_strr}" + "\n")
                return

        except:

            num=str(num)
            if num in df['員工號碼\nEmployee No.'].values:
                mask = df['員工號碼\nEmployee No.'] == num
                idx = df[mask].index[0]
                name = df.loc[idx, "姓名\nName"]
                meal = df.loc[idx, "備註\nA.B.C\n素食"]
                if (math.isnan(meal)) or (meal==None) or (meal==" "):
                    self.ui.name.setText(name)
                    self.ui.number.setText(num)
                    self.ui.food.appendPlainText("You did not \nOrder a meal")
                    #self.ui.food.appendPlainText("未訂餐")
                    self.ui.text.clear()
                    with open(f'{self.date_str}.txt', mode='a', encoding="utf-8") as f:
                        f.write(str(df[mask].values[0][0]) + ",")
                        f.write(df[mask].values[0][1] + ",")
                        f.write(df[mask].values[0][2][0:1] + "\n")

                else:
                    self.ui.name.setText(name)
                    self.ui.number.setText(num)
                    self.ui.food.appendPlainText(f"    Meal: {meal}\n   Thank You!")
                    #self.ui.food.appendPlainText("")
                    self.ui.text.clear()
            else:
                self.ui.food.appendPlainText("\nNo Data")
                self.ui.number.setText("???")
                self.ui.name.setText("???")

                #self.ui.food.appendPlainText("\n查無此人")
                ng_num=self.ui.text.text()
                self.ui.text.clear()
                with open(f'{self.date_str}.txt', mode='a', encoding="utf-8") as f:
                    f.write(str(ng_num) + ",")
                    f.write(f"{self.datetime_strr}   ")
                    f.write(("No Data\n"))
                return

    def reset(self):
        self.ui.text.setFocus()

    def check_nan(self,meal):
        try:
            if math.isnan(meal):
                return True

        except:
            return False
    def time_check(self,datetime_dt,bf,lunch,dinner,sup,buffer):
        # bf=4
        # lunch=10
        # dinner=16
        # sup=23
        # now=datetime.strftime(now,"YY-mm-dd-hh")

        datetime_str = datetime_dt.strftime("%H:%M:%S")

        now_dt = datetime.datetime.strptime(datetime_str, "%H:%M:%S")

        dt_4 = datetime.datetime.strptime(f"{bf}:00:00", "%H:%M:%S")
        dt_10 = datetime.datetime.strptime(f"{lunch}:00:00", "%H:%M:%S")
        dt_16 = datetime.datetime.strptime(f"{dinner}:00:00", "%H:%M:%S")
        dt_21 = datetime.datetime.strptime(f"{sup}:00:00", "%H:%M:%S")

        time_buffer = int(buffer)
        time_delta = datetime.timedelta(hours=time_buffer)  # 時差

        dt_limit = dt_10 + time_delta  # 本地時間加4小時

        if dt_10 < now_dt < dt_10 + time_delta:
            return "午餐Lunch Bưã trưa"
        elif dt_4< now_dt < dt_4 + time_delta:
            return '早餐Breakfast Bữa sáng'
        elif dt_16< now_dt < dt_16 + time_delta:
            return '晚餐Dinner Bữa tối'
        elif dt_21< now_dt < dt_21 + time_delta:
            return '宵夜supper Bưã đêm '
        else:
            return "非用餐時間"


if __name__=='__main__':
    multiprocessing.freeze_support()
    config = configparser.ConfigParser()
    config.read('config.ini',encoding="utf-8")

    file=config['setting']['file']
    bf=config['setting']['早餐']
    lunch=config['setting']['午餐']
    dinner=config['setting']['晚餐']
    sup=config['setting']['宵夜']
    buffer=config['setting']['buffer']

    #sheet=config['setting']['sheet']
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\logo.png'))
    stats = Stats()
    stats.ui.showFullScreen()
    app.exec_()