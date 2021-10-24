import cv2
import sqlite3
import requests
from json import JSONDecoder
import time
from datetime import datetime
import numpy.core._dtype_ctypes

conn = sqlite3.connect('member_local.sqlite')  # 連接資料庫
cursor = conn.cursor()
sqlstr = 'SELECT * FROM member'  # 讀取會員資料表
cursor.execute(sqlstr)
rows = cursor.fetchall()  # 取得會員資料
member = []
for row in rows:  # 儲存所有會員帳號
    member.append(row[0])

while True:
    a = input("建立帳號:c\nLOGIN請輸入: l\n查詢登入時間請輸入: t\n離開請輸入: q\n")


    def compareimage(filepath1, filepath2):  # 人臉比對
        try:
            http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
            key = "bFyIq4Jmm9_IUqzY3zK_xCgu3JQrLaqr"
            secret = "0Za8gDtlObGoL_p6E3ZIOU4jLFZxOULT"
            data = {"api_key": key, "api_secret": secret}
            files = {"image_file1": open(filepath1, "rb"), "image_file2": open(filepath2, "rb")}
            response = requests.post(http_url, data=data, files=files)  # 進行辨識
            req_con = response.content.decode('utf-8')  # 取得結果
            req_dict = JSONDecoder().decode(req_con)  # 將結果轉為字典
            confidence = req_dict['confidence']  # 取得相似度指數
            return confidence
        except Exception:
            print("產生錯誤，無法識別！")
            return 0


    while a == "c":
        memberid = input('請輸入帳號(直接按「Enter」結束)：')
        if memberid == '':  # 未輸入帳號就結束
            a = ''
            break
        elif memberid in member:  # 帳號已存在
            print('此帳號已存在，不可重複！')
        else:  # 建立帳號
            picfile = memberid + '.jpg'  # 會員圖片檔名稱
            member.append(memberid)
            cv2.namedWindow('frame')
            cap = cv2.VideoCapture(0)  # 開啟cam
            # 設定影像尺寸
            width = 426
            height = 480

            # 設定擷取影像的尺寸大小
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
            while (cap.isOpened()):  # 如果cam開啟
                ret, img = cap.read()
                if ret == True:
                    cv2.imshow('frame', img)  # 顯示影像
                    k = cv2.waitKey(100)  # 0.1秒檢查一次按鍵
                    if k == ord('z') or k == ord('Z'):
                        cv2.imwrite('memberPic/' + picfile, img)  # 儲存影像
                        break
            cap.release()  # 關閉cam
            cv2.destroyWindow('frame', )
            sqlstr = 'INSERT INTO member values("{}","{}")'.format(memberid, picfile)  # 將帳號及影像檔名稱寫入資料表
            cursor.execute(sqlstr)
            conn.commit()
            print('帳號建立成功！')

    while a == "l":
        conn = sqlite3.connect('member_local.sqlite')  # 連接資料庫
        cursor = conn.cursor()
        sqlstr = 'SELECT * FROM member'  # 讀取會員資料表
        cursor.execute(sqlstr)
        rows = cursor.fetchall()  # 取得會員資料
        imagedict = {}  # 會員帳號、檔名字典
        for row in rows:
            imagedict[row[0]] = 'memberPic/' + row[1]

        timenow = time.time()  # 取得現在時間數值
        cv2.namedWindow('frame')
        cap = cv2.VideoCapture(0)  # 開啟cam
        while (cap.isOpened()):  # cam開啟成功
            count = 5 - int(time.time() - timenow)  # 倒數計時5秒
            ret, img = cap.read()
            if ret == True:
                imgcopy = img.copy()  # 複製影像
                cv2.putText(imgcopy, str(count), (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 15, (0, 0, 255),
                            35)  # 在複製影像上畫倒數秒數
                cv2.imshow('frame', imgcopy)  # 顯示複製影像
                k = cv2.waitKey(100)  # 0.1秒讀鍵盤一次
                if k == ord('z') or k == ord('Z') or count == 0:  # 按「Z」鍵或倒數計時結束
                    cv2.imwrite('media/test.jpg', img)  # 將影像存檔
                    break

        cap.release()  # 關閉cam
        cv2.destroyWindow('frame')

        success = False  # 紀錄登入是否成功
        for img in imagedict:
            if compareimage(imagedict[img], 'media/test.jpg') > 75:  # 相似度大於75
                print('登入成功！歡迎' + img + '！')
                success = True
                savetime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 目前時刻字串
                sqlstr = 'INSERT INTO login values("{}","{}")'.format(img, savetime)  # 將帳號及現在時刻寫入資料表
                cursor.execute(sqlstr)
                conn.commit()
                break
            if not success:  # 登入失敗
                print('登入失敗！您不是會員！')
        a = ''

    conn.close()
    if a == 'q':
        break
import os

os.system('pause')