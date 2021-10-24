from socket import *
import cv2
import pymssql
from datetime import datetime as dt
import time
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
TCP_ip = config['socket']['TCP_ip']
TCP_port = int(config['socket']['TCP_port'])
host=config['SQL']['host']
user=config['SQL']['user']
pwd=config['SQL']['pwd']
db=config['SQL']['db']


sbef="2021-04-30 09:39"
bef=dt.strptime(sbef,"%Y-%m-%d %H:%M")
snow=dt.now().strftime("%Y-%m-%d %H:%M:%S")
now=dt.strptime(snow,"%Y-%m-%d %H:%M:%S")
id_list=[]
print(snow)
def tcp_client_socket(data):
    # 創建socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)#AF_INET

    # 目的信息
    server_ip = TCP_ip
    server_port = TCP_port

    # 鏈接服務器
    tcp_client_socket.connect((server_ip, server_port))

    # 提示用户輸入數據
    send_data = data

    tcp_client_socket.send(send_data.encode("gbk"))

    # 接收對方發送過來的數據，最大接收1024個字節
    recvData = tcp_client_socket.recv(1024)
    print('接收到的數據為:', recvData.decode('gbk'))

    # 關閉套接字
    tcp_client_socket.close()
def get_outid(path):
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

        for i in files:
            sid = i.split("_")[1].split(".")[0]
            intid = int(sid)
            l.append(intid)
    if len(l) == 0:
        return 1
    else:
        mid = max(l)
        return mid + 1
class Camera():
    def __init__(self,num):
        self.cap=cv2.VideoCapture(num)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    def show(self):
        while True:
            ret,frame=self.cap.read()
            cv2.imshow("frame",frame)
            if cv2.waitKey(1)==0xFF & ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def show_gray(self):
        while True:
            ret,frame=self.cap.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("frame",gray)
            if cv2.waitKey(1)==0xFF & ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()


    # def get_frame(self):
    #     if not self.cap.isOpened():
    #         self.cap.open()
    #     img=cv2.imread("watchimg",cv2.IMREAD_GRAYSCALE)
    #     cv2.imshow('image', img)
    #     cv2.waitKey()
    #     cv2.destroyAllWindows()

    def get_frame(self,save_path):
        from datetime import datetime
        while self.cap.isOpened():

            ret, frame = self.cap.read()
            if ret:
                imgcopy = frame.copy()

                cv2.imshow("Get Picture", imgcopy)
                k = cv2.waitKey(100)
                if k == ord("z") or k == ord("Z"):
                    cv2.imwrite(save_path, frame)
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break
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

    def Insert(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
        print("寫入完成")


#計算資料庫內最大ID
ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
res=ms.ExecQuery("select id from Car_inn")
print(res)
if len(res) != 0:
    for i in res:
        id_list.append(i[0])
else:

        id_list.append(0)
max_id=max(id_list)

#主程式
while True:

    trigger=int(input("send trigger"))

    if trigger == 0:
        break
    if trigger==1:
        try:
            max_id += 1
            cap1 = Camera(0)
            cap1.get_frame(f"D:\Share_SQL\img\in\{snow[:11]}_{max_id}.jpg")
            write_sql = f"INSERT INTO Car_inn (id, Date) VALUES ('{max_id}', '{now}')"
            ms.Insert(write_sql)

            # tcp_client_socket(str(max_id))
            maxid=str(max_id)+"_in"
            time.sleep(1)
            try:
                tcp_client_socket(str(maxid))
            except:
                print("TCP server連接失敗")
        except :
            raise error
            break
    if trigger == 2:
        # number = "330HLJ"
        # ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
        # res = ms.ExecQuery(f"select id from Car_inn where Number = '{number}'")
        # out_id = str(max(res)[0]).strip()
        try:
            out_id=get_outid("D:\Share_SQL\img\out")
            print("離開車輛ID=%s"%out_id)
        except:
            print("OUT_ID 取得失敗")

            # max_id += 1

        cap1 = Camera(0)
        cap1.get_frame(f"D:\Share_SQL\img\out\{snow[:11]}_{out_id}.jpg")

            # write_sql=f"INSERT INTO Car_inn (id, Date) VALUES ('{max_id}', '{dt.now()}')"
            # ms.Insert(write_sql)

        maxid = str(out_id) + "_out"
        print(maxid)
        time.sleep(0.2)
        try:
            tcp_client_socket(str(maxid))
        except:
            print("TCP server 連接失敗")







