import matplotlib.pyplot as plt
import cv2
import numpy as np
print(123)

#
# class Camera():
#     def __init__(self,num):
#         self.cap=cv2.VideoCapture(num)
#         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
#     def show(self):
#         while True:
#             ret,frame=self.cap.read()
#             cv2.imshow("frame",frame)
#             if cv2.waitKey(1)==0xFF & ord('q'):
#                 break
#         self.cap.release()
#         cv2.destroyWindow()
#
#     def show_gray(self):
#         while True:
#             ret,frame=self.cap.read()
#             gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#             cv2.imshow("frame",gray)
#             if cv2.waitKey(1)==0xFF & ord('q'):
#                 break
#         self.cap.release()
#         cv2.destroyWindow()
#
#
#     def get_frame(self):
#         # if not self.cap.isOpened():
#         #     self.cap.open()
#         ret, frame = self.cap.read()
#         # img=cv2.imread(frame,cv2.IMREAD_GRAYSCALE)
#         cv2.imshow('image', frame)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
# img = cv2.imread(r'D:\2020forieign\OK\000000_OK_60S_T609P3W1BJ01.jpg',cv2.IMREAD_GRAYSCALE)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.plot([0,500,100,20],[100,200,300,40],'c', linewidth=5)
# plt.show()



# img=cv2.imread(r"C:\Users\yang\Desktop\側拍\20210226-113225-cam0.bmp")
# cv2.imshow("sss",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#img=np.zeros((256,256,3),np.uint8)
#img=cv2.imread(r"圖片\ro.jpg")
#cv2.rectangle(img,(0,0),(50,50),(0,0,255),3)
# img=cv2.imread(r"C:\Users\yang\Desktop\側拍\20210226-113225-cam1.bmp")
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

def Scan_imgname():
    import os

    # 指定要查詢的路徑
    yourPath = r"D:\Share_SQL\img\out"
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
        else:
            print('OH MY GOD !!')

    # 與listdir不同的是，listdir只是將指定路徑底下的目錄和檔案列出來
    # walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
    allList = os.walk(yourPath)
    # 列出所有子目錄與子目錄底下所有的檔案
    l=[]
    for root, dirs, files in allList:
        #   列出目前讀取到的路徑
        #print("path：", root)
        #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
        #print("directory：", dirs)
        #   列出在這個路徑下讀取到的所有檔案

        for i in files:
            sid=i.split("_")[1].split(".")[0]
            intid=int(sid)
            l.append(intid)
    if len(l) == 0 :
        return 1
    else:
        max_id = max(l)

        return max_id+1






from datetime import datetime as dt
sbef="2021-04-30 09:39:25"
date=dt.strptime(sbef,"%Y-%m-%d %H:%M:%S")
snow=dt.now().strftime("%Y-%m-%d %H:%M:%S")
now=dt.strptime(snow,"%Y-%m-%d %H:%M:%S")



delta=now-date
print(now)
print(date)
print(delta)
staytime=str(delta).split(":")
print(f"停車時間為{staytime[-3]}時 {staytime[-2]}分 {staytime[-1]}秒")
