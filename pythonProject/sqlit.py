import sqlite3
import csv
# con=sqlite3.connect("myDB.db")

#con.cursor()
#建立資料表的查詢指令
# createStr = 'CREATE TABLE Employeee\
#        (ID INT PRIMARY KEY     NOT NULL,\
#        NAME           TEXT    NOT NULL,\
#        BIRTHYEAR      INT     NOT NULL,\
#        ADDRESS        CHAR(50),\
#        SALARY         INT);'
#con.execute(createStr)
#con.execute("INSERT INTO Employeee (ID,NAME,BIRTHYEAR,ADDRESS,SALARY) \
#            VALUES (1,'小陳',1991,'台南市',20000)")
# con.execute("INSERT INTO Employeee (ID,NAME,BIRTHYEAR,ADDRESS,SALARY) \
#             VALUES (2,'小楊',1996,'南投縣',50000)")
# con.execute("INSERT INTO Employeee (ID,NAME,BIRTHYEAR,ADDRESS,SALARY) \
#             VALUES (3,'小朱',1997,'台中市',40000)")
# con.execute("INSERT INTO Employeee (ID,NAME,BIRTHYEAR,ADDRESS,SALARY) \
#             VALUES (4,'小雲',1994,'台北市',70000)")
# con.commit()

# cursor=con.execute("SELECT * FROM Employeee")
# for i in cursor:
#     print(i)
# con.close()









con2=sqlite3.connect("myDB2.db")
#con2.cursor()

# #建立groups資料表的查詢指令
# create_groups = 'CREATE TABLE if not exists groupss ( \
#  group_id int primary key not null, \
#  group_name char(50) not null \
# );'
# con2.execute(create_groups)
#
# #建立students資料表的查詢指令
# create_students = 'CREATE TABLE if not exists students ( \
#  student_id int primary key not null, \
#  student_name char(50) not null, \
#  group_id int not null, \
#  FOREIGN KEY (group_id) REFERENCES groups (group_id) \
#  ON DELETE NO ACTION ON UPDATE NO ACTION \
# );'
# con2.execute(create_students)



# cursor=con2.execute("SELECT * FROM students")
# for i in cursor:
#     print(i)
#
# cursor.close()


# con2.execute("INSERT INTO groupss('group_id','group_name') VALUES(1,'青色之馬')")
# con2.execute("INSERT INTO groupss('group_id','group_name') VALUES(2,'夢幻之都')")
# con2.execute("INSERT INTO groupss('group_id','group_name') VALUES(3,'新不了城')")
# con2.commit()

# students=[]
# with open("students.csv",encoding="UTF-8") as f:
#     students=list(csv.reader(f,delimiter=','))
#     for student in students[1:]:
#         con2.execute("INSERT INTO students(student_id,student_name,group_id)\
#                      VALUES(%d,'%s',%d)"%(eval(student[0]),student[1],eval(student[2])))
#         con2.commit()


import cv2
import sqlite3
conn=sqlite3.connect('member_local.sqlite')
cursor=conn.cursor()
sqlstr="SELECT * FROM member"
cursor.execute(sqlstr)
row=cursor.fetchall()
members=[]
for i in row:
    members.append(i[0])

while True:
    memberid=input("請輸入帳號:")
    if memberid == '':
        print('輸入錯誤')
        break
    elif memberid in members:
        print("此帳號已存在")
        break
    else:
        members.append(memberid)
        picname="%s.jpg"%memberid
        cv2.namedWindow("frame")
        cap=cv2.VideoCapture(0)
        weight=960
        height=780
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,weight)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
        while cap.isOpened():
            ret,frame=cap.read()
            if ret:
                cv2.imshow('frame',frame)
                k=cv2.waitKey(100)
                if k ==ord("z") or k ==ord("Z"):
                    cv2.imwrite('memberPic/'+picname,frame)
                    break
        cap.release()
        cv2.destroyAllWindows()
        sqlstr="INSERT INTO member values('{}','{}')".format(memberid,picname)
        cursor.execute(sqlstr)
        conn.commit()
        print("帳號建立成功")




