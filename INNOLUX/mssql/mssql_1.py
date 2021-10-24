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



ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS',user='sa',pwd='P@ss1234',db='CLTestDB')

#insert
write_sql = f"INSERT INTO OfficeCheckData (UserName, UserNo,IO,Seat,Time) VALUES ('楊睿哲', '20025617','I','TOC5F','20210628180000')"
ms.Insert(write_sql)



##update
# ms = MSSQL(host='LAPTOP-IJV23O75\SQLEXPRESS', user='sa', pwd='P@ss1234', db='MYDB')
# sql = f"UPDATE Car_inn SET Out = '{now}' WHERE Number = '{number}'"
# ms.Insert(sql)
# res = ms.ExecQuery(f"select Date from Car_inn where Number = '{number}'")




















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
