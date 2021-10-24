# import socket
#
#
# # 建立一個socket套接字，該套接字還沒有建立連線
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 繫結監聽埠
# server.bind(('localhost', 6688))
# # 開始監聽，並設定最大連線數
# server.listen(5)
# # 獲取未建立連線的服務端的IP和埠資訊
# print(server.getsockname())
# # 下面註釋掉的是獲取未建立連線的服務端套接字的遠端IP和埠資訊，執行下面語句會報錯，原因就是現在還沒有遠端客戶端程式連線
# # print(server.getpeername())
#
# print(u'waiting for connect...')
# # 等待連線，一旦有客戶端連線後，返回一個建立了連線後的套接字和連線的客戶端的IP和埠元組
# connect, (host, port) = server.accept()
# # 現在建立連線就可以獲取這兩個資訊了，注意server和connect套接字的區別，一個是未建立連線的套接字，一個是已經和客戶端建立了連線的套接字
# peer_name = connect.getpeername()
# sock_name = connect.getsockname()
# print(u'the client %s:%s has connected.' % (host, port))
# print('The peer name is %s and sock name is %s' % (peer_name, sock_name))
#
# # 接受客戶端的資料
# data = connect.recv(1024)
# # 傳送資料給客戶端告訴他接收到了
# connect.sendall(b'your words has received.')
# print(b'the client say:' + data)
#
# # 結束socket
# server.close()
#
#
#
# import socket
# HOST = '127.0.0.1'
# PORT = 8000
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((HOST, PORT))
# server.listen(10)
#
# while True:
#     conn, addr = server.accept()
#     clientMessage = str(conn.recv(1024), encoding='utf-8')
#
#     print('Client message is:', clientMessage)
#
#     serverMessage = 'I\'m here!'
#     conn.sendall(serverMessage.encode())
#     conn.close()
#
# # from  datetime import datetime as dt
# # sbef="2021-04-30 09:39"
# # bef=dt.strptime(sbef,"%Y-%m-%d %H:%M")
# # snow=dt.now().strftime("%Y-%m-%d %H:%M:%S")
# # now=dt.strptime(snow,"%Y-%m-%d %H:%M:%S")
# #
# # print(now-bef)
#
#
import pymssql
from datetime import datetime as dt
import socket
import threading
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
TCP_ip = config['socket']['TCP_ip']
TCP_port = int(config['socket']['TCP_port'])
host=config['SQL']['host']
user=config['SQL']['user']
pwd=config['SQL']['pwd']
db=config['SQL']['db']

class MSSQL:
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
            print("連接數據庫成功")
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

    def Insert(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
        print("寫入完成")

number="330HLJ"
ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
id_list = ms.ExecQuery(f"select ID from Car_inn where Number = '{number}'")
max_nid=max(id_list)[0]
print(max_nid)
