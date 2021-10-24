from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader
import math
import pandas as pd
import multiprocessing
import pymssql
from datetime import datetime as dt
import configparser
from PySide2.QtGui import QIcon
#pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo\logo.ico"
from PySide2.QtWidgets import QButtonGroup
#a=QButtonGroup.buttonToggled()
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/food.ui')
        self.ui.setWindowTitle('刷餐系統')
        self.ui.text.returnPressed.connect(self.get_data)
        self.ui.buttonGroup.buttonClicked.connect(self.reset)
        #self.sheetCombo=self.ui.sheet.currentText()
        #self.sheetCombo=self.ui.buttonGroup.text()
        #self.ui.buttonGroup.buttonToggled(self.reset)
        self.btn=self.ui.buttonGroup.checkedButton().text()

        #print(self.ui.buttonGroup.checkedButton())
    def get_data(self):
        self.btn = self.ui.buttonGroup.checkedButton().text()
        self.ui.food.clear()
        self.ui.name.clear()
        self.ui.number.clear()
        barcode = self.ui.text.text()
        try:
            num=int(barcode[-8:])
        except:
            self.ui.food.appendPlainText("No Data")
            self.ui.food.appendPlainText("查無此人")
            self.ui.text.clear()
            return
        if self.btn =="早餐":
            sheet='早餐Breakfast Bữa sáng'
        elif self.btn =="午餐":
            sheet='午餐Lunch Bưã trưa'
        elif self.btn =="晚餐":
            sheet='晚餐Dinner Bữa tối'
        elif self.btn =="宵夜":
            sheet='宵夜supper Bưã đêm '
        df = pd.read_excel(file, usecols="H,I,K,M",sheet_name=sheet)
        try:
            if num in df['員工號碼\nEmployee No.'].values:
                mask = df['員工號碼\nEmployee No.'] == num
                idx = df[mask].index[0]
                name = df.loc[idx, "姓名\nName"]
                meal = df.loc[idx, "備註\nA.B.C\n素食"]

                if meal.isdigit():
                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText("You did not order a meal")
                    self.ui.food.appendPlainText("未訂餐")
                    self.ui.text.clear()
                    with open(r'result.txt', mode='a', encoding="utf-8") as f:
                        f.write(str(df[mask].values[0][0]) + ",")
                        f.write(df[mask].values[0][1] + ",")
                        f.write(df[mask].values[0][2].split(" ")[0]+",")
                        f.write(f"{dt.now()}"+"\n")

                else:
                    self.ui.name.setText(name)
                    self.ui.number.setText(str(num))
                    self.ui.food.appendPlainText(f"Meal:{meal}")
                    self.ui.food.appendPlainText("Thank You")
                    self.ui.text.clear()
            else:
                self.ui.food.appendPlainText("No Data")
                self.ui.food.appendPlainText("查無此人")
                self.ui.text.clear()

        except:

            num=str(num)
            if num in df['員工號碼\nEmployee No.'].values:
                mask = df['員工號碼\nEmployee No.'] == num
                idx = df[mask].index[0]
                name = df.loc[idx, "姓名\nName"]
                meal = df.loc[idx, "備註\nA.B.C\n素食"]
                if meal.isdigit():
                    self.ui.name.setText(name)
                    self.ui.number.setText(num)
                    self.ui.food.appendPlainText("You did not order a meal")
                    self.ui.food.appendPlainText("未訂餐")
                    self.ui.text.clear()
                    with open(r'result.txt', mode='a', encoding="utf-8") as f:
                        f.write(str(df[mask].values[0][0]) + ",")
                        f.write(df[mask].values[0][1] + ",")
                        f.write(df[mask].values[0][2].split(" ")[0] + "\n")

                else:
                    self.ui.name.setText(name)
                    self.ui.number.setText(num)
                    self.ui.food.appendPlainText(f"Meal:{meal}")
                    self.ui.food.appendPlainText("Thank You")
                    self.ui.text.clear()
            else:
                self.ui.food.appendPlainText("No Data")
                self.ui.food.appendPlainText("查無此人")
                self.ui.text.clear()


    def reset(self):

        self.ui.text.setFocus()
if __name__=='__main__':
    multiprocessing.freeze_support()
    config = configparser.ConfigParser()
    config.read('config.ini',encoding="utf-8")
    file=config['setting']['file']
    #sheet=config['setting']['sheet']
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\logo.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()