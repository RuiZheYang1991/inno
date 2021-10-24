# from socket import *
#
# def tcp_client_socket(send):
#     # 創建socket
#     tcp_client_socket = socket(AF_INET, SOCK_STREAM)#AF_INET
#
#     # 目的信息
#     server_ip = "127.0.0.1"
#     server_port = 8000
#
#     # 鏈接服務器
#     tcp_client_socket.connect((server_ip, server_port))
#
#     # 提示用户輸入數據
#     send_data = send
#
#     tcp_client_socket.send(send_data.encode("gbk"))
#
#     # 接收對方發送過來的數據，最大接收1024個字節
#     recvData = tcp_client_socket.recv(1024)
#     print('接收到的數據為:', recvData.decode('gbk'))
#
#     # 關閉套接字
#     tcp_client_socket.close()
#
# tcp_client_socket("hihi")


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




def find_img_path(id):
    ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
    img_name = ""
    reslist = ms.ExecQuery("select id,Date from Car_inn")
    for i, date in reslist:
        # print(i.strip(), id)
        sdata = dt.strftime(date, "%Y-%m-%d")
        if str(i).strip() == id:
            img_name = sdata + f"_{id}.jpg"
            break
    path = r"\\%s\Share_SQL\img\in\%s" % (TCP_ip,img_name)
    return path


#def find_out_path(id):
    # ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
    # img_name = ""
    # reslist = ms.ExecQuery("select id,Date from Car_inn")
    # for i, date in reslist:
    #     # print(i.strip(), id)
    #     sdata = dt.strftime(date, "%Y-%m-%d")
    #     if str(i).strip() == id:
    #         img_name = sdata + f"_{id}.jpg"
    #         break
    # path = r"\\192.168.1.106\Share_SQL\img\out\%s" % img_name
    # return path
def out_img_path(path,send_id):
    import os

    # 指定要查詢的路徑
    yourPath = path
    # 列出指定路徑底下所有檔案(包含資料夾)
    allFileList = os.listdir(yourPath)
    # 逐一查詢檔案清單
    for file in allFileList:
        #   這邊也可以視情況，做檔案的操作(複製、讀取...等)
        #   使用isdir檢查是否為目錄
        #   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)
        if os.path.isdir(os.path.join(yourPath, file)):
            print("I'm a directory: " + file)
        #   使用isfile判斷是否為檔案
        elif os.path.isfile(yourPath + file):
            print(file)
        # else:
        #     print('OH MY GOD !!')

    # 與listdir不同的是，listdir只是將指定路徑底下的目錄和檔案列出來
    # walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
    allList = os.walk(yourPath)
    # 列出所有子目錄與子目錄底下所有的檔案
    l = []
    for root, dirs, files in allList:
        #   列出目前讀取到的路徑
        # print("path：", root)
        #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
        # print("directory：", dirs)
        #   列出在這個路徑下讀取到的所有檔案
        print(len(files))
        if len(files)==0:
            print("資料夾沒有圖片")
        else:
            for i in files:
                sid = i.split("_")[1].split(".")[0]
                intid = int(sid)
                if sid == send_id:
                    path = r"\\%s\Share_SQL\img\out\%s" % (TCP_ip,i)
                    return path

    print("資料夾內找不到編號為%s的圖片"%send_id)
def in_img_path(path,send_id):
    import os

    # 指定要查詢的路徑
    yourPath = path
    # 列出指定路徑底下所有檔案(包含資料夾)
    allFileList = os.listdir(yourPath)
    # 逐一查詢檔案清單
    for file in allFileList:
        #   這邊也可以視情況，做檔案的操作(複製、讀取...等)
        #   使用isdir檢查是否為目錄
        #   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)
        if os.path.isdir(os.path.join(yourPath, file)):
            print("I'm a directory: " + file)
        #   使用isfile判斷是否為檔案
        elif os.path.isfile(yourPath + file):
            print(file)


    # 與listdir不同的是，listdir只是將指定路徑底下的目錄和檔案列出來
    # walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
    allList = os.walk(yourPath)
    # 列出所有子目錄與子目錄底下所有的檔案
    l = []
    for root, dirs, files in allList:
        #   列出目前讀取到的路徑
        # print("path：", root)
        #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
        # print("directory：", dirs)
        #   列出在這個路徑下讀取到的所有檔案
        print("圖片數量為:",len(files))
        if len(files)==0:
            print("資料夾沒有圖片")
        else:
            for i in files:
                sid = i.split("_")[1].split(".")[0]
                intid = int(sid)
                if sid == send_id:
                    path = path + i

                    return path
    print("資料夾內找不到編號為%s的圖片" % send_id)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def in_port():
    HOST = TCP_ip
    PORT = TCP_port

    server.bind((HOST, PORT))
    server.listen(10)

# def out_port():
#     HOST = '192.168.1.111'
#     PORT = 8001
#
#     server.bind((HOST, PORT))
#     server.listen(10)

def Car_in_server():

    while True:

        conn, addr = server.accept()
        clientMessage = str(conn.recv(1024), encoding='utf-8')
        send_id,k=clientMessage.split("_")

        # print('Client message is:', clientMessage)

        serverMessage = r'I got it!'
        conn.sendall(serverMessage.encode())
        conn.close()
        if k == "in":
            sbef = "2021-04-30 09:39"
            bef = dt.strptime(sbef, "%Y-%m-%d %H:%M")
            snow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
            now = dt.strptime(snow, "%Y-%m-%d %H:%M:%S")
            # 此處做圖像辨識  並傳出車牌號碼  後續寫入資料庫
            img_path = in_img_path(r"\\%s\Share_SQL\img\in"%TCP_ip,send_id)
            print(send_id)
            print(img_path)
            number = "330HLJ"
            #ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
            # sql=f"insert into Number where id == {clientMessage} values('{number}') "
            sql = "select * from Car_inn"
            result = ms.ExecQuery(sql)
            for i in result:
                id = str(i[0]).strip()
                if send_id == id:
                    try:
                        dsql = f"UPDATE Car_inn SET Date = '{now}' WHERE id = '{send_id}'"
                        ms.Insert(dsql)
                        print("進入時間寫入成功:",now)
                    except:
                        print("進入時間寫入失敗")
                    try:
                        sql = f"UPDATE Car_inn SET Number = '{number}' WHERE id = '{send_id}'"
                        ms.Insert(sql)
                        print("進入車牌寫入資料庫成功:",number)
                    except:
                        print("進入車牌寫入資料庫失敗:", number)


        elif k== "out":
            img_path = out_img_path(r"\\%s\Share_SQL\img\out"%TCP_ip,send_id)
            print(send_id)
            print(img_path)
            # 此處做圖像辨識  並傳出車牌號碼  後續將
            number = "330HLJ"
            try:
                # sbef = "2021-04-30 09:39"
                # bef = dt.strptime(sbef, "%Y-%m-%d %H:%M")
                snow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
                now = dt.strptime(snow, "%Y-%m-%d %H:%M:%S")

                #ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
                try:
                    sql = f"UPDATE Car_inn SET Out = '{now}' WHERE Number = '{number}'"
                    ms.Insert(sql)
                    print("離開時間寫入資料庫成功:",now)
                except:
                    print("離開時間寫入資料庫失敗")
                id_list = ms.ExecQuery(f"select ID from Car_inn where Number = '{number}'")
                max_nid = max(id_list)[0]
                res = ms.ExecQuery(f"select Date from Car_inn where id = '{max_nid}'")
                date = res[0][0]
                delta=now-date
                print(now)
                print(date)
                print(delta)
                staytime=str(delta).split(":")
                print(f"停車時間為{staytime[-3]}時 {staytime[-2]}分 {staytime[-1]}秒")
                try:
                    sql2 = f"UPDATE Car_inn SET StayTime = '{delta}' WHERE id = '{max_nid}'"
                    ms.Insert(sql2)
                    print("staytime:",staytime)
                except:
                    print("staytime 寫入資料庫失敗")
            except:
                raise Exception






# def Car_out_server():
#     sbef = "2021-04-30 09:39"
#     bef = dt.strptime(sbef, "%Y-%m-%d %H:%M")
#     snow = dt.now().strftime("%Y-%m-%d %H:%M:%S")
#     now = dt.strptime(snow, "%Y-%m-%d %H:%M:%S")
#     while True:
#         conn, addr = server.accept()
#         clientMessage = str(conn.recv(1024), encoding='utf-8')
#         img_path = find_img_path(clientMessage)
#         print('Client message is:', clientMessage)
#         print(img_path)
#
#         serverMessage = r'I got it!'
#         conn.sendall(serverMessage.encode())
#         conn.close()
#
#         # 此處做圖像辨識  並傳出車牌號碼
#
#         number = "330HLJ"
#         ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
#         # sql=f"insert into Number where id == {clientMessage} values('{number}') "
#         sql = "select * from Car_inn"
#         result = ms.ExecQuery(sql)
#         for i in result:
#             id = i.strip()
#             if clientMessage == id:
#                 ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
#                 sql = f"UPDATE Car_inn SET Number = '{number}' WHERE id = '{clientMessage}'"
#                 ms.Insert(sql)

ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
print("Waiting for trigger...")
inport=threading.Thread(target=in_port())
inport.start()
s_in = threading.Thread(target=Car_in_server())
s_in.start()


# ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
# res = ms.ExecQuery(f"select Date from Car_inn where id = 44")
# date = res[0][0]
# delta = now - date
# print(now)
# print(date)
# print(delta)

# number = "330HLJ"
# ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
# res = ms.ExecQuery(f"select Date from Car_inn where Number = '{number}'")
# for i in res:
#     print(i)
# date = res[0][0]
# delta=now-date
# print(res)
# print(date)
# print(delta)