import cv2
import sqlite3
import requests
import time
from datetime import datetime
#拍照儲存至資料庫
key = "cllFzxC7UVMrzWKk9dfcFohiQKfjdgvz"
secret = "uE6A_aL9hi0D3uOKkb-KVnbRo64yMUce"
conn=sqlite3.connect('member_cloud.sqlite')
cursor=conn.cursor()
now=time.time()
cv2.namedWindow('frame')
cap=cv2.VideoCapture(0)
while cap.isOpened():
    count=5 -int(time.time()-now)
    ret,frame=cap.read()
    if ret:
        imgcopy=frame.copy()
        cv2.putText(imgcopy,str(count),(200,300),cv2.FONT_HERSHEY_PLAIN,15,(200,80,155),15)
        cv2.imshow("frame",imgcopy)
        k=cv2.waitKey(100)
        if k==ord("z") or k==ord("Z"):
            cv2.imwrite("me.jpg",frame)
            break
cap.release()
cv2.destroyWindow('frame')
