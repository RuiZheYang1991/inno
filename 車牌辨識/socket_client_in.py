from socket import *
import cv2
import pymssql
from datetime import datetime as dt
import time

sbef="2021-04-30 09:39"
bef=dt.strptime(sbef,"%Y-%m-%d %H:%M")
snow=dt.now().strftime("%Y-%m-%d %H:%M")
now=dt.strptime(snow,"%Y-%m-%d %H:%M")
id_list=[]
print(snow)
def tcp_client_socket(data):
    # 創建socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)#AF_INET

    # 目的信息
    server_ip = "192.168.1.111"
    server_port = 8000

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

    def Insert(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
        print("寫入完成")



ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS',user='sa',pwd='P@ss1234',db='MYDB')
res=ms.ExecQuery("select id from Car_inn")

if res ==[]:
    id_list.append(0)
else:
    for i in res:

        i=int(i[0])
        id_list.append(i)
max_id=max(id_list)
while True:
    max_id += 1
    trigger=int(input("send trigger"))
    if trigger == 0:
        break
    if trigger==1:

        cap1 = Camera(0)
        cap1.get_frame(f"D:\Share_SQL\img\{snow[:11]}_{max_id}.jpg")
        write_sql=f"INSERT INTO Car_inn (id, Date) VALUES ('{max_id}', '{now}')"
        ms.Insert(write_sql)
        # tcp_client_socket(str(max_id))
    maxid=str(max_id)+"_in"
    time.sleep(0.2)
    tcp_client_socket(str(maxid))








