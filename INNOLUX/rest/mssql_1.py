import pymssql
import pandas as pd
# server = "LAPTOP-IJV23O75\SQLEXPRESS"
# user = "sa"
# password = 'P@ss1234'
# database = "教學資料庫"
# conn = pymssql.connect(server, user, password, database)
# as_dict = True
#
# cur = conn.cursor()  # 將數據庫連接信息，賦值給cur。
# cursor = conn.cursor(as_dict=True)  # 返回的值以字典輸出  默認的是list
#
#
# # 插入信息
# def InsertData(name, password):
#     sql = "INSERT INTO User_Table(name,password) VALUES (%s,%s)"
#     data = {(name, password)}
#     cursor.executemany(sql, data)
#     conn.commit()
#
#
# # 刪除操作
# def DeleteData(name2):
#     sql = "delete User_Table where name=%s"
#     data = name2
#     cursor.execute(sql, data)
#     conn.commit()
#
#
# # 全局查詢
# def SelectTable(table):
#     table = "select * from CC"
#     cursor.execute(table)
#     row = cursor.fetchall()
#     print(row)
#     return row
#     conn.commit()
#
#
# # 查詢莫一個的值信息
# def SelectTable1(name1):
#     sql = "select name,password from User_Table where name=%s"
#     data = name1
#     cursor.execute(sql, data)
#     row = cursor.fetchall()
#
#     print(row)
#     return row
#     conn.commit()
#
#
# def main():
#     # SelectTable1('python2')
#     # InsertData('python2',5555)
#     # UpdateData('python','5555')
#     SelectTable()
#     conn.close()
#
# SelectTable()

# if __name__ == '__main__':
#     main()
#
#
# from login import SqlDb


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
ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS',user='sa',pwd='P@ss1234',db='CLTestDB')

##insert
# write_sql = f"INSERT INTO Employee (CompanyNO, UserNO,CardNO) VALUES ('{'innolux'}', '{'20025617'}','{'2222334665'}')"
# ms.Insert(write_sql)
#
# num='14098151'
# covs_area=[]
# def str_toDay(sdate):
#     from datetime import datetime as dt
#     Y=sdate[0:4]
#     m=sdate[4:6]
#     d=sdate[6:8]
#     st=f'{Y}-{m}-{d}'
#     #print(st)
#
#     date=dt.strptime(st,'%Y-%m-%d')
#     return date
# def getInOut_time(num):
#     I_time=ms.ExecQuery(f"select Time from OfficeCheckData where UserNo = {num} and IO = 'I'")
#     O_time=ms.ExecQuery(f"select Time from OfficeCheckData where UserNo = {num} and IO = 'O'")
#     timee=ms.ExecQuery(f"select Time,IO from OfficeCheckData where UserNo = {num}")
#     name=ms.ExecQuery(f"select * from OfficeCheckData where UserNo = {num}")
#     seat=ms.ExecQuery(f"select Time,Seat from OfficeCheckData where UserNo = {num} and IO = 'I'")
#     all=ms.ExecQuery(f"select Seat from Employee")
#     print(all)
#     # for i in seat:
#     #     print(i)
#     # for i,y in zip(I_time,O_time):
#     #     print(f'{name[0][0]}  進入時間',str_toDate(i[0]),'  離開時間',str_toDate(y[0]))
#     # for i in timee:
#     #     print(f'{name[0][0]}  {i[1]},{str_toDate(i[0])}')
# getInOut_time(num)
##update
#ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='CLTestDB')
# sql = f"UPDATE Car_inn SET Out = '{now}' WHERE Number = '{number}'"
# ms.Insert(sql)
# res = ms.ExecQuery(f"select Date from Car_inn where Number = '{number}'")
#res = ms.ExecQuery("select * from OfficeCheckData")


res=pymssql.connect(server='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', password='P@ss1234', database='CLTestDB')
df0 = pd.read_sql("select * from OfficeCheckData",res)
df=pd.DataFrame(df0)
no_l=[]
name_l=[]
seat_l = []
io_l=[]
time_l=[]
check_dic={}
def unique_index(L,e):
    return [j for (i,j) in enumerate(L) if i == e]

def get_covid(num):
    for no,name,seat,io,timee in zip(df['UserNo'],df['UserName'],df['Seat'],df['IO'],df['Time']):

        if (len(name_l)==0) and (io=="I"):
            no_l.append(no)
            name_l.append(name)
            seat_l.append(seat)
            io_l.append(io)
            time_l.append(timee)
            check_dic[no]=io
        else:
            #check_dic[no] = io
            # print(check_dic.get(no), io)
            if check_dic.get(no)!=io:  #io == io_l[-1]
                #print(check_dic.get(no),io)
                no_l.append(no)
                name_l.append(name)
                seat_l.append(seat)
                io_l.append(io)
                time_l.append(timee)
                check_dic[no] = io
            else:
                pass
    rname =[]
    rno=[]
    rseat=[]
    rtime=[]
    rio=[]
    for name,io,timee,number,seat in zip(name_l,io_l,time_l,no_l,seat_l):
        if number==num:
            rname.append(name)
            rno.append(number)
            rio.append(io)
            rseat.append(seat)
            rtime.append(timee)
        print (rname,rno,rio,rseat,rtime)
get_covid("20025617")




















##____________________________________________________________________________________________________________________________

# import pymssql
# from datetime import datetime as dt
# import socket
# import threading
# import configparser
# config = configparser.ConfigParser()
# config.read('config.ini')
# TCP_ip = config['socket']['TCP_ip']
# TCP_port = int(config['socket']['TCP_port'])
# host=config['SQL']['host']
# user=config['SQL']['user']
# pwd=config['SQL']['pwd']
# db=config['SQL']['db']
#
# class MSSQL:
#     def __init__(self, host, user, pwd, db):
#         self.host = host
#         self.user = user
#         self.pwd = pwd
#         self.db = db
#
#     def __GetConnect(self):
#         if not self.db:
#             raise (NameError, "沒有設置數據庫信息")
#         self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
#         # self.conn = pymssql.connect(host='localhost',user='sa',password='645713039', database='PythonWebServerDemo',charset="utf8")
#         cur = self.conn.cursor()
#         if not cur:
#             raise (NameError, "連接數據庫失敗")
#         else:
#             print("連接數據庫成功")
#             return cur
#
#     def ExecQuery(self, sql):
#         cur = self.__GetConnect()
#         cur.execute(sql)
#         resList = cur.fetchall()
#
#         # 查询完毕后必须关闭连接
#         self.conn.close()
#         return resList
#
#     def ExecNonQuery(self, sql):
#         cur = self.__GetConnect()
#         cur.execute(sql)
#         self.conn.commit()
#         self.conn.close()
#
#     def Insert(self, sql):
#         cur = self.__GetConnect()
#         cur.execute(sql)
#         self.conn.commit()
#         self.conn.close()
#         print("寫入完成")
#
# number="330HLJ"
# ms = MSSQL(host=host, user=user, pwd=pwd, db=db)
# id_list = ms.ExecQuery(f"select ID from Car_inn where Number = '{number}'")
# max_nid=max(id_list)[0]
# print(max_nid)
