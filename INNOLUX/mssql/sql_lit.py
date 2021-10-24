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