from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
import math
import pandas as pd
import multiprocessing
import datetime
import configparser
from PySide2.QtGui import QIcon
import os
import qq
#pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo\logo.ico"
from PySide2.QtWidgets import QButtonGroup
#a=QButtonGroup.buttonToggled()
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/food_time_img.ui')
        self.ui.setWindowTitle('刷餐系統')
        self.ui.text.returnPressed.connect(self.get_data)

        #self.ui.buttonGroup.buttonClicked.connect(self.reset)
        #self.sheetCombo=self.ui.sheet.currentText()
        #self.sheetCombo=self.ui.buttonGroup.text()
        #self.ui.buttonGroup.buttonToggled(self.reset)
        #self.btn=self.ui.buttonGroup.checkedButton().text()
        # datetime_dt = datetime.datetime.today()  # 獲得當地時間
        # datetime_strr = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")
        # date_str = datetime_dt.strftime("%Y%m%d")

        #print(self.datetime_strr)
        #print(self.time_check(datetime_dt=self.datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))
        #print(self.ui.buttonGroup.checkedButton())
    def get_data(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding="utf-8")
        self.file = self.config['setting']['file']
        self.bf = self.config['setting']['早餐']
        self.lunch = self.config['setting']['午餐']
        self.dinner = self.config['setting']['晚餐']
        self.sup = self.config['setting']['宵夜']
        self.buffer = self.config['setting']['buffer']
        datetime_dt = datetime.datetime.today()  # 獲得當地時間
        datetime_strr = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")
        date_str = datetime_dt.strftime("%Y%m%d")
        self.ui.food.clear()
        self.ui.name.clear()
        self.ui.number.clear()
        barcode = self.ui.text.text()
        #barcode = '¹F ¥ß20025617'
        if not os.path.exists("log"):
            os.mkdir('log')
        try:
            num=int(barcode[-8:])
        except:
            self.ui.food.appendPlainText("工號格式錯誤")
            #self.ui.food.appendPlainText("查無此人")

            self.ui.text.clear()
            self.ui.text.setFocus()
            return
        # try:
        #     with open(f"log\{self.datetime_strr}.txt", mode="a", encoding="UTF-8") as f:
        #         data = f.readlines()
        #         for i in data:
        #             if i.split(",")[0] != barcode[-8:]:
        #                 continue
        # except:
        #     self.ui.food.appendPlainText("Repeated meal collection")
        #     self.ui.food.appendPlainText("重複領取")
        #     return

        try:
            # self.ui.food.appendPlainText(
            #     self.time_check(datetime_dt=datetime_dt, bf=self.bf, dinner=self.dinner, lunch=self.lunch, sup=self.sup,
            #                     buffer=self.buffer))

            #print(self.time_check(datetime_dt=self.datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))
            if self.time_check(datetime_dt=datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer) == "非用餐時間":
                #self.ui.food.appendPlainText(self.time_check(datetime_dt=datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))

                self.ui.food.appendPlainText("非用餐時間")
                return
            else:
                df = pd.read_excel(self.file, usecols="H,I,K,M,J",sheet_name=self.time_check(datetime_dt=datetime_dt,bf=self.bf,dinner=self.dinner,lunch=self.lunch,sup=self.sup,buffer=self.buffer))#
        #print(df)
        except:

            self.ui.food.appendPlainText("Data Error")
            # #print("Data Error")
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
                dep = df.loc[idx, "課別.1"]
                # print(type(meal))
                # print(meal)
                # print(self.check_nan(meal))
                if self.check_nan(meal) or (meal==None) or (meal==" "):
                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText("未訂餐")
                    self.ui.food.appendPlainText("Did not order a meal")
                    self.ui.food.appendPlainText("Không theo thứ tự")
                    self.ui.text.clear()
                    try:

                        with open(f'log\\{date_str}_NG.txt', mode='a', encoding="utf-8") as f:
                            f.write(str(num) + ",")
                            f.write(df[mask].values[0][1] + ",")
                            f.write(dep + ",")
                            f.write(df[mask].values[0][3][:2]+",")
                            f.write(f"{datetime_strr} 未訂餐刷卡\n")
                            #print(df[mask].values[0][2])
                    except:
                        pass


                else:

                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText(f" 餐點:  【 {meal} 】\n Meal:  【 {meal} 】\n Thank You!")
                    #self.ui.food.appendPlainText("Thank You")
                    self.ui.text.clear()
                    try:
                        if not os.path.exists(f"log\{date_str}_OK.txt"):
                            with open(f"log\{date_str}_OK.txt", mode="w", encoding="UTF-8") as f:
                                f.write()
                        if not os.path.exists(f"log\{date_str}_NG.txt"):
                            with open(f"log\{date_str}_NG.txt", mode="w", encoding="UTF-8") as f:
                                f.write()
                    except:
                        pass
                    try:
                        with open(f"log\{date_str}_OK.txt", mode="r", encoding="UTF-8") as f:
                            data = f.readlines()
                            for i in data:

                                if (i.split(",")[0] != str(num)) or (df[mask].values[0][3][:2] != i.split(",")[3]) :

                                    continue
                                else:
                                    self.ui.food.appendPlainText("重複領取\nRepeated meals\nGạt thẻ lặp lại")
                                    # self.ui.food.appendPlainText("Repeated meals")
                                    # self.ui.food.appendPlainText("Gạt thẻ lặp lại")
                                    with open(f"log\{date_str}_NG.txt", mode="a", encoding="UTF-8") as f:
                                        f.write(str(num) + ",")
                                        f.write(df[mask].values[0][1] + ",")
                                        f.write(dep + ",")
                                        f.write(df[mask].values[0][3][:2] + ",")
                                        f.write(f"{datetime_strr} 重複領取\n")
                                        return
                        with open(f"log\{date_str}_OK.txt", mode="a", encoding="UTF-8") as f:
                            f.write(str(num) + ",")
                            f.write(df[mask].values[0][1] + ",")
                            f.write(dep + ",")
                            f.write(df[mask].values[0][3][:2] + ",")
                            f.write(f"{datetime_strr} 取餐成功\n")
                    except:
                        pass
            else:
                self.ui.food.appendPlainText("未訂餐")
                self.ui.food.appendPlainText("Did not order a meal")
                self.ui.food.appendPlainText("Không theo thứ tự")


                #self.ui.food.appendPlainText("查無此人")


                try:
                    ng_num = int(barcode[-8:])
                    # print(num)
                except:
                    self.ui.food.appendPlainText("工號格式錯誤")
                    # self.ui.food.appendPlainText("查無此人")
                    self.ui.text.clear()
                df_data = pd.read_excel(self.file, sheet_name='人員主檔')
                mask = df_data['＊工號'] == ng_num
                idx = df_data[mask].index[0]
                name = df_data.loc[idx, "＊姓名"]
                dep = df_data.loc[idx, "課別"]
                self.ui.number.setText(str(ng_num))
                self.ui.name.setText(name)
                self.ui.text.clear()
                self.ui.text.setFocus()
                try:
                    if not os.path.exists("log"):
                        os.mkdir('log')
                    with open(f'log\\{date_str}_NG.txt', mode='a', encoding="utf-8") as f:
                        f.write(f'{str(ng_num)},{name},{dep},{datetime_strr} 未訂餐刷卡\n')
                        #f.write(f"{self.datetime_strr}" + "\n")
                except FileExistsError:
                    print("無資料人員LOG寫入失敗")

                self.ui.text.clear()
                self.ui.text.setFocus()
                return

        except:

            num=str(num)
            if num in df['員工號碼\nEmployee No.'].values:
                mask = df['員工號碼\nEmployee No.'] == num
                idx = df[mask].index[0]
                name = df.loc[idx, "姓名\nName"]
                meal = df.loc[idx, "備註\nA.B.C\n素食"]
                dep= df.loc[idx, "課別.1"]
                if (math.isnan(meal)) or (meal==None) or (meal==" "):
                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText("未訂餐")
                    self.ui.food.appendPlainText("Did not order a meal")

                    self.ui.food.appendPlainText("Không theo thứ tự")
                    self.ui.text.clear()
                    try:
                        if not os.path.exists("log"):
                            os.mkdir('log')

                        with open(f'log\\{date_str}_NG.txt', mode='a', encoding="utf-8") as f:
                            f.write(f'{str(ng_num)},{name},{dep}')
                            f.write(df[mask].values[0][1] + ",")
                            f.write(df[mask].values[0][3][0:2] + " 未訂餐刷卡\n")
                    except FileExistsError:
                        print("無資料人員LOG寫入失敗")



                else:
                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText(f" 餐點:  【 {meal} 】\n Meal:  【 {meal} 】\n Thank You!")
                    #self.ui.food.appendPlainText("")
                    self.ui.text.clear()
                    try:
                        if not os.path.exists(f"log\{date_str}_OK.txt"):
                            with open(f"log\{date_str}_OK.txt", mode="w", encoding="UTF-8") as f:
                                f.write()
                        if not os.path.exists(f"log\{date_str}_NG.txt"):
                            with open(f"log\{date_str}_NG.txt", mode="w", encoding="UTF-8") as f:
                                f.write()
                    except:
                        pass
                    try:
                        with open(f"log\{date_str}_OK.txt", mode="r", encoding="UTF-8") as f:
                            data = f.readlines()
                            for i in data:

                                if i.split(",")[0] != str(num) or (df[mask].values[0][3][:2] == i.split(",")[3]):
                                    continue
                                else:
                                    self.ui.food.appendPlainText("重複領取\nRepeated meals\nGạt thẻ lặp lại")
                                    # self.ui.food.appendPlainText("Repeated meals")
                                    # self.ui.food.appendPlainText("Gạt thẻ lặp lại")
                                    with open(f"log\{date_str}_NG.txt", mode="a", encoding="UTF-8") as f:
                                        f.write(str(ng_num) + ",")
                                        f.write(df[mask].values[0][1] + ",")
                                        f.write(dep + ",")
                                        f.write(df[mask].values[0][3][:2] + ",")
                                        f.write(f"{datetime_strr} 重複領取\n")
                                        return
                        with open(f"log\{date_str}_OK.txt", mode="a", encoding="UTF-8") as f:
                            f.write(str(num) + ",")
                            f.write(df[mask].values[0][1] + ",")
                            f.write(dep + ",")
                            f.write(df[mask].values[0][3][:2] + ",")
                            f.write(f"{datetime_strr}\n")
                    except:
                        pass
            else:
                self.ui.food.appendPlainText("未訂餐")
                self.ui.food.appendPlainText("Did not order a meal")
                self.ui.food.appendPlainText("Không theo thứ tự")


                #self.ui.food.appendPlainText("\n查無此人")

                try:
                    ng_num = int(barcode[-8:])
                    # print(num)
                except:
                    self.ui.food.appendPlainText("工號格式錯誤")
                    # self.ui.food.appendPlainText("查無此人")
                    self.ui.text.clear()
                    self.ui.text.setFocus()
                    return

                df_data = pd.read_excel(self.file, sheet_name='人員主檔')
                mask = df_data['＊工號'] == ng_num
                idx = df_data[mask].index[0]
                name = df_data.loc[idx, "＊姓名"]
                dep = df_data.loc[idx, "課別.1"]
                self.ui.number.setText(str(ng_num))
                self.ui.name.setText(name)
                self.ui.text.clear()
                self.ui.text.setFocus()
                try:
                    if not os.path.exists("log"):
                        os.mkdir('log')
                    with open(f'{date_str}_NG.txt', mode='a', encoding="utf-8") as f:
                        f.write(f'{str(ng_num)},{name},{dep},{datetime_strr} 未訂餐刷卡\n')
                        # f.write(f"{self.datetime_strr}" + "\n")
                except:
                    pass
                self.ui.text.clear()
                self.ui.text.setFocus()
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
            #self.ui.food.appendPlainText(f'{dt_10}<{now_dt}<{dt_10 + time_delta}')
            return "午餐Lunch Bưã trưa"
        elif dt_4< now_dt < dt_4 + time_delta:
            #self.ui.food.appendPlainText(f'{dt_4}<{now_dt}<{dt_4+time_delta}')
            return '早餐Breakfast Bữa sáng'
        elif dt_16< now_dt < dt_16 + time_delta:
            #self.ui.food.appendPlainText(f'{dt_16}<{now_dt}<{dt_16 + time_delta}')
            return '晚餐Dinner Bữa tối'
        elif dt_21< now_dt < dt_21 + time_delta:
            #self.ui.food.appendPlainText(f'{dt_21}<{now_dt}<{dt_21 + time_delta}')
            return '宵夜supper Bưã đêm '
        else:
            return "非用餐時間"

#pyinstaller -F -w -c --paths C:\Users\yang\python3.8_86x\venv\Lib\site-packages\shiboken2 meal_time.py -p qq.py --noconsole --hidden-import PySide2
#.QtXml --icon="icon\logo.ico"

if __name__=='__main__':
    multiprocessing.freeze_support()
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\logo.jpg'))
    stats = Stats()
    stats.ui.showFullScreen()
    app.exec_()