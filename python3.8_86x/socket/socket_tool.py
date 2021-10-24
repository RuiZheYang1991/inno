import socket
from PySide2.QtWidgets import QApplication, QTextBrowser
from PySide2.QtUiTools import QUiLoader
import threading
from PySide2.QtCore import Signal,QObject
from PySide2.QtGui import QIcon,QPixmap
import os
# from pymssql import _mssql
# from pymssql import _pymssql
# import multiprocessing
# import uuid
# import decimal
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('ui/rwd.ui')
        self.ui.setWindowTitle('socket測試程式')
        self.ui.udp_send.clicked.connect(self.udp_Client)
        self.ui.udp_server_conn.clicked.connect(self.udp_Server)
        self.ui.tcp_client_send.clicked.connect(self.tcp_Client)
        self.ui.tcp_server_conn.clicked.connect(self.tcp_Server)
        self.ui.tcp_server_clear.clicked.connect(self.ui.tcp_server_show.clear)
        self.ui.tcp_client_clear.clicked.connect(self.ui.tcp_client_show.clear)
        self.ui.udp_server_clear.clicked.connect(self.ui.udp_server_show.clear)
        self.ui.udp_client_clear.clicked.connect(self.ui.udp_client_show.clear)

    def update_ip(self):
        self.tcp_client_encode = self.ui.tcp_client_encode.currentText()
        self.tcp_server_encode = self.ui.tcp_server_encode.currentText()
        self.udp_client_encode = self.ui.udp_client_encode.currentText()
        self.udp_server_encode = self.ui.udp_server_encode.currentText()
        self.tcp_server_send = self.ui.tcp_server_send.toPlainText()
        self.tcp_client_ip = self.ui.tcpcip.text()
        self.tcp_client_port = self.ui.tcport.text()
        self.tcp_server_ip = self.ui.tcpsip.text()
        self.tcp_server_port = self.ui.tcpsport.text()
        self.udp_client_ip = self.ui.ucip.text()
        self.udp_client_port = self.ui.ucport.text()
        self.udp_server_ip = self.ui.usip.text()
        self.udp_server_port = self.ui.usport.text()

    def udp_Server(self):
        def inner():
            try:
                self.update_ip()
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.bind((self.udp_server_ip,int(self.udp_server_port)))
                self.ui.udp_server_show.append(f'建立UDP Server成功:{self.udp_server_ip,int(self.udp_server_port)}')
            except:
                self.ui.udp_server_show.append(f'建立UDP Server失敗:{self.udp_server_ip, int(self.udp_server_port)}')
                return
            while True:
                data, addr = s.recvfrom(1024)
                msg = data.decode(self.udp_server_encode)
                self.ui.udp_server_show.append(f'recive:{msg}')
                self.ui.udp_server_show.ensureCursorVisible()
            s.close()
        thread = threading.Thread(target=inner)
        thread.setDaemon(True)
        thread.start()

    # def udp_Client(self):
    #     def inner():
    #         self.update_ip()
    #         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #         str1 = self.ui.udp_msg.text()
    #         if len(str1) != 0 :
    #             s.sendto(str1.encode(self.udp_client_encode), (self.udp_client_ip,int(self.udp_client_port)))
    #             self.ui.udp_client_show.append(f'send:{str1}')
    #             self.ui.udp_client_show.ensureCursorVisible()
    #             s.close()
    #         else:
    #             self.ui.udp_client_show.append('請輸入字串')
    #             self.ui.udp_client_show.ensureCursorVisible()
    #     thread = threading.Thread(target=inner)
    #     thread.setDaemon(True)
    #     thread.start()
    def udp_Client(self):

        self.update_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        str1 = self.ui.udp_msg.text()
        if len(str1) != 0 :
            s.sendto(str1.encode(self.udp_client_encode), (self.udp_client_ip,int(self.udp_client_port)))
            self.ui.udp_client_show.append(f'send:{str1}')
            self.ui.udp_client_show.ensureCursorVisible()
            s.close()
            return
        else:
            self.ui.udp_client_show.append('請輸入字串')
            self.ui.udp_client_show.ensureCursorVisible()
            return


    # def tcp_Client(self):
    #     def inner():
    #         try:
    #             self.update_ip()
    #             send_msg = self.ui.tcp_client_msg.text()
    #             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #             s.connect((self.tcp_client_ip, int(self.tcp_client_port)))
    #             if len(send_msg) != 0:
    #                 s.send(send_msg.encode(self.tcp_client_encode))
    #                 self.ui.tcp_client_show.append(f'send:{send_msg}')
    #                 recv_msg = s.recv(1024)
    #                 self.ui.tcp_client_show.append(f'recive:{recv_msg.decode(self.tcp_client_encode)}')
    #                 self.ui.tcp_client_show.ensureCursorVisible()
    #             else:
    #                 self.ui.tcp_client_show.append('請輸入字串')
    #                 self.ui.tcp_client_show.ensureCursorVisible()
    #         except:
    #             self.ui.tcp_client_show.append('與伺服器連接失敗')
    #             self.ui.tcp_client_show.ensureCursorVisible()
    #             return
    #     thread = threading.Thread(target=inner)
    #     thread.setDaemon(True)
    #     thread.start()

    def tcp_Client(self):

        try:
            self.update_ip()
            send_msg = self.ui.tcp_client_msg.text()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.tcp_client_ip, int(self.tcp_client_port)))
            if len(send_msg) != 0:
                s.send(send_msg.encode(self.tcp_client_encode))
                self.ui.tcp_client_show.append(f'send:{send_msg}')
                recv_msg = s.recv(1024)
                self.ui.tcp_client_show.append(f'recive:{recv_msg.decode(self.tcp_client_encode)}')
                self.ui.tcp_client_show.ensureCursorVisible()
            else:
                self.ui.tcp_client_show.append('請輸入字串')
                self.ui.tcp_client_show.ensureCursorVisible()
        except:
            self.ui.tcp_client_show.append('與伺服器連接失敗')
            self.ui.tcp_client_show.ensureCursorVisible()
            return


    def tcp_Server(self):
        def inner():
            self.update_ip()
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((self.tcp_server_ip,int(self.tcp_server_port)))
                s.listen(5)
                self.ui.tcp_server_show.append(f'建立TCP Server成功:{self.tcp_server_ip, int(self.tcp_server_port)}')
                print(f'建立TCP Server成功:{self.tcp_server_ip, int(self.tcp_server_port)}')
            except:
                self.ui.tcp_server_show.append('建立連線失敗')
                self.ui.tcp_server_show.ensureCursorVisible()
                return

            while True:
                conn, addr = s.accept()
                while True:
                    indata = conn.recv(1024)
                    if len(indata) == 0:
                        conn.close()
                        break
                    self.ui.tcp_server_show.append(f'recive from client:{indata.decode(self.tcp_server_encode)}')
                    self.ui.tcp_server_show.ensureCursorVisible()

                    if len(self.ui.tcp_server_send.toPlainText())==0:
                        outdata = 'echo ' + indata.decode(self.tcp_server_encode)
                        conn.send(outdata.encode(self.tcp_server_encode))
                        self.ui.tcp_server_show.append(f'send echo:{indata.decode(self.tcp_server_encode)}')
                        self.ui.tcp_server_show.ensureCursorVisible()
                    else:
                        outdata = self.ui.tcp_server_send.toPlainText()
                        conn.send(outdata.encode(self.tcp_server_encode))
                        self.ui.tcp_server_show.append(f'send:{self.ui.tcp_server_send.toPlainText()}')
                        self.ui.tcp_server_show.ensureCursorVisible()
        thread = threading.Thread(target=inner)
        thread.setDaemon(True)
        thread.start()

if __name__=='__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('icon\logo.jpg'))
    stats = Stats()
    stats.ui.show()
    app.exec_()






























