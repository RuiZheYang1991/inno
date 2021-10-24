import cv2
import sqlite3
import time
import requests
from json import JSONDecoder
import os
from datetime import datetime


if __name__ == '__main__':
    #拍照儲存至資料庫
    def create_account():
        conn=sqlite3.connect('member_local.sqlite')
        cursor=conn.cursor()
        sqlstrr="SELECT * FROM member"
        cursor.execute(sqlstrr)
        row=cursor.fetchall()
        members=[]

        for i in row:
            members.append(i[0])

        while True:
            memberid = input("開始建立帳號\n請輸入帳號名稱:\n[Press Enter to close]")

            if memberid == '':
                break
            elif memberid in members:
                print("此帳號已存在")
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
                            #cap.release()
                            cv2.destroyWindow('frame')
                            break


                sqlstr="INSERT INTO member values('{}','{}')".format(memberid,picname)
                cursor.execute(sqlstr)
                conn.commit()

                print("帳號建立成功")
            break
        conn.close()
    def compareimg(img1,img2):
        try:
            http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
            key = "9dUjvrMSxkKkw02tkX6jYLMs4xvo6i5O"
            secret = "B8A5hiK9uvJrHReom4KLSopiHEN75aHS"
            data = {"api_key": key, "api_secret": secret}
            files = {"image_file1": open(img1, "rb"), "image_file2": open(img2, "rb")}
            response = requests.post(http_url, data=data, files=files)
            req_con = response.content.decode("utf-8")
            req_dict = JSONDecoder().decode(req_con)
            confidence = req_dict["confidence"]
            return confidence
        except Exception:
            print("產生錯誤")
            return 0

    def log_in():
        success=False
        conn = sqlite3.connect('member_local.sqlite')
        cursor = conn.cursor()
        for img in imgdict:
            if compareimg(imgdict[img],"media/temp.jpg")>75:
                success=True
                print("登入成功,你好 %s!"%img)
                savetime=str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
                sqlstr="INSERT INTO login values('%s','%s')"%(img,savetime)
                cursor.execute(sqlstr)
                conn.commit()

            if not success:
                print("登入失敗!!")
        conn.close()
        # return success

    conn=sqlite3.connect('member_local.sqlite')
    cursor=conn.cursor()
    sqlstr="SELECT * FROM member"
    cursor.execute(sqlstr)
    rows=cursor.fetchall()
    imgdict={}
    for row in rows:
        imgdict[row[0]]='memberPic/'+row[1]

    while True:
        key=input("歡迎使用臉部辨識!\n\n建立帳號請輸入:a\n登入請輸入:l\n退出請輸入:q\n")
        if key=="q":
            break
        while key == "a":
            create_account()
            key == ""
            break

        while key == "l":
            now=time.time()
            cv2.namedWindow('Log in')
            cap=cv2.VideoCapture(0)

            while cap.isOpened():
                count=5 -int(time.time()-now)
                ret,frame=cap.read()
                if ret:
                    imgcopy=frame.copy()
                    cv2.putText(imgcopy,str(count),(20,150),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),4)
                    cv2.imshow("Log in",imgcopy)
                    k=cv2.waitKey(100)
                    if k==ord("z") or k==ord("Z") or count==0:
                        cv2.imwrite("media/temp.jpg",frame)
                        break

            cap.release()
            cv2.destroyWindow('Log in')
            log_in()
            key=""
import os
os.system('pause')







