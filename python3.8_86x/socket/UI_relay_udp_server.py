
import socket
from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
import threading
from PySide2.QtCore import Signal,QObject
from PySide2.QtGui import QIcon,QPixmap
import configparser
import os
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


def udp_server(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip,port))

    while True:
        print("UDP server up!")
        dic = dict()
        data,addr = s.recvfrom(1024)

        try:
            msg = data.decode('unicode_escape').split(',')
            tem = str(round(float(msg[1]), 1))
            aisle=msg[0]
            print(msg)

            if is_float(tem) & aisle.isdigit():
                dic[aisle] = tem
                temp_dict.update(dic)
                print(temp_dict)
        except :
            print("資料格式錯誤")
    s.close()


def handle():#client,addr

    while True:
        ts = socket.socket()  # 1、建立網路套接字s
        ts.bind((TCP_ip, TCP_port))  # 2、繫結地址
        ts.listen(5)  # 3、監聽
        try:
            client, addr = ts.accept()  # 4、接受客戶端連線
            text = client.recv(1024)

            # if not text:
            #     client.close()
            # recive = "501,0000719991,I,20025617,楊睿哲"
            ptext=text.decode('unicode-escape')

            #ptext = "501,0000719991,I,P,34.6"
            #temp_dict["1"]="39.5"
            #ptext="501,0000719991,I,20025617,楊睿哲"

            ptext_list=ptext.split(",")
            if len(ptext_list) == 5:
                # print(ptext_list)
                loc_num=ptext.split(",")[0][-1]#走道號碼
                ttext_str=str(temp_dict.get(loc_num,'0'))#取str溫度
                ttext_float=float(ttext_str)#溫度 to float
                if (ttext_float>low) and (ttext_float < high):
                    try:
                        tttext=ptext_list[0]+","+ptext_list[1]+",I,P,"+ttext_str
                        client.send(tttext.encode('unicode_escape'))
                        stats.send_name(ptext_list[-1], loc_num)
                        stats.send_num(ptext_list[3], loc_num)
                        stats.send_temp(temp_dict[loc_num], loc_num)
                        stats.send_pic(f'img\\{ptext_list[3]}.jpg', loc_num)
                        print(addr[0], addr[1], '>>', tttext)
                        temp_dict[loc_num] = '0'
                    except:
                        pass
                else:
                    try:

                        tttext=ptext_list[0]+","+ptext_list[1]+",I,F,"+ttext_str

                        client.send(tttext.encode('unicode_escape'))
                        print(addr[0], addr[1], '>>', tttext)

                        stats.send_name(ptext_list[-1],loc_num)
                        stats.send_num(ptext_list[3],loc_num)

                        stats.send_NGtemp(temp_dict[loc_num],loc_num)
                        stats.send_pic(f'img\{ptext_list[3]}.jpg',loc_num)
                        temp_dict[loc_num] = '0'
                    except:
                        pass

            else:
                try:
                    client.send('資料格式錯誤'.encode('unicode_escape'))
                    # print(addr[0], addr[1], '沒有收到溫度')
                    client.close()
                except:
                    pass

        except:
            try:
                client.send("somethings wrong".encode('unicode_escape'))
                client.close()
            except:
                pass
            #break



# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(QTextBrowser, str)

    # 还可以定义其他种类的信号
    update_table = Signal(str)
# 实例化
#global_ms = MySignals()

# class CommonHelper:
#     def __init__(self):
#         pass
#     @staticmethod
#     def readQss(style):
#         with open(style, 'r') as f:
#             return f.read()
class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('ui/mainn.ui')
        self.ui.setWindowTitle('門禁UI')
        self.ui.pic1.setPixmap(QPixmap(r"img\images.jpg"))
        self.ui.pic2.setPixmap(QPixmap(r"img\images.jpg"))
        self.ui.pic3.setPixmap(QPixmap(r"img\images.jpg"))
        #QSS_____________________
        # self.styleFile = 'qss\style.qss'
        # # 换肤时进行全局修改，只需要修改不同的QSS文件即可
        # self.style = CommonHelper.readQss(self.styleFile)
        # self.ui.setStyleSheet(self.style)
        # QSS_____________________

        # self.ui.exportToExcel.clicked.connect(self.export_excel)

        #global_ms.text_print.connect(self.printToGui)


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

    # def task2(self):
    #     def threadFunc():
    #         global_ms.text_print.emit(self.ui.infoBox2, '输出内容')
    #
    #     thread = threading.Thread(target=threadFunc)
    #     thread.start()


if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    temp_dict = dict()
    temp_value = []
    UDP_ip = config['socket']['UDP_ip']
    UDP_port = int(config['socket']['UDP_port'])
    TCP_ip = config['socket']['TCP_ip']
    TCP_port = int(config['socket']['TCP_port'])
    high = float(config['socket']['high'])
    low = float(config['socket']['low'])
    total_loc = config['socket']['total_loc']


    udp = threading.Thread(target=udp_server, args=(UDP_ip, UDP_port,))
    udp.setDaemon(True)
    udp.start()

    tcpp = threading.Thread(target=handle)
    tcpp.setDaemon(True)
    tcpp.start()

    app = QApplication([])
    app.setWindowIcon(QIcon('icon\images.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()






























