import matplotlib.pyplot as plt
import cv2
import numpy as np


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
# cap1=Camera(0)
# cap1.show()
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

# img=np.zeros((256,256,3),np.uint8)
# img=cv2.imread(r"圖片\ro.jpg")
# cv2.rectangle(img,(0,0),(50,50),(0,0,255),3)



#
# img=cv2.imread(r"C:\Users\yang\Pictures\000648_OK_yellowSN_T7119983BA04.jpg",0)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()







# np.random.seed(0)  # seed for reproducibility
#
# x1 = np.random.randint(10, size=6)  # 一維 array
# x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
# x3 = np.random.randint(10, size=(3, 4, 8))  # Three-dimensional array
# print(x1,x1.shape,x1.ndim)
# print("____________________________________________")
# print(x2,x2.shape,x2.ndim)
# print("____________________________________________")

# print("____________________________________________")

# print(x3)
# print(x3[0].min(axis=1))

# cap=cv2.VideoCapture(0)
# width=640
# height=320
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# fourcc=cv2.VideoWriter_fourcc(*"XVID")
# out=cv2.VideoWriter(r"C:\Users\yang\out.avi",fourcc,20.0,(width,height))
#
# while (cap.isOpened()):
#     ret,frame=cap.read()
#     if ret == True:
#         out.write(frame)
#         cv2.imshow("frame",frame)
#         if cv2.waitKey(0)& 0xFF==ord('q'):
#             break
#     else:
#         print("open cam faild")
#         break
#
#
#
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()


# import cv2
# cap=cv2.VideoCapture(1)
# while True:
#     ret,frame=cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break
#
#
# cap.release()
# cv2.destroyAllWindows()



#倒計時 存影片
# cap=cv2.VideoCapture(1)
# sz=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# fps=20
#
# fourcc=cv2.VideoWriter_fourcc(*"mp4v")
#
# vout=cv2.VideoWriter()
# vout.open('output.avi',fourcc,fps,sz,True)
# cnt=1
# while cnt <201:
#     _,frame=cap.read()
#     cv2.putText(frame,str(cnt),(10,20),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),1,cv2.LINE_AA)
#     vout.write(frame)
#     cnt+=1
#     cv2.imshow("video",frame)
#     cv2.waitKey(30)
# vout.release()
# cap.release()
# cv2.destroyAllWindows()





# ##抓等高線並存檔
# import cv2
# import numpy as np
#
# # 開啟網路攝影機
# cap = cv2.VideoCapture(1)
# sz=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# fps=20
#
# fourcc=cv2.VideoWriter_fourcc(*"mp4v")
#
# vout=cv2.VideoWriter()
# vout.open('new_output.avi',fourcc,fps,sz,True)
# cnt=1
# # 設定影像尺寸
# width = 960
# height = 780
#
# # 設定擷取影像的尺寸大小
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#
# # 計算畫面面積
# area = width * height
#
# # 初始化平均影像
# ret, frame = cap.read()
# avg = cv2.blur(frame, (4, 4))
# avg_float = np.float32(avg)
#
#
# while cnt < 201:
#     # 讀取一幅影格
#     ret, frame = cap.read()
#     cv2.putText(frame, str(cnt), (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1, cv2.LINE_AA)
#
#     # 若讀取至影片結尾，則跳出
#     if ret == False:
#         break
#
#     # 模糊處理
#     blur = cv2.blur(frame, (4, 4))
#
#     # 計算目前影格與平均影像的差異值
#     diff = cv2.absdiff(avg, blur)
#
#     # 將圖片轉為灰階
#     gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#
#     # 篩選出變動程度大於門檻值的區域
#     ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
#
#     # 使用型態轉換函數去除雜訊
#     # 参数op的取值	含义
#     # cv2.MORPH_OPEN	开运算(open) ,先腐蚀后膨胀的过程。开运算可以用来消除小黑点，在纤细点处分离物体、平滑较大物体的边界的
#     # 同时并不明显改变其面积。
#     # cv2.MORPH_CLOSE	闭运算(close)，先膨胀后腐蚀的过程。闭运算可以用来排除小黑洞。
#     # cv2.MORPH_GRADIENT	形态学梯度(morph-grad)，可以突出团块(blob)的边缘，保留物体的边缘轮廓。
#     # cv2.MORPH_TOPHAT	顶帽(top-hat)，将突出比原轮廓亮的部分。
#     # cv2.MORPH_BLACKHAT	黑帽(black-hat)，将突出比原轮廓暗的部分。
#
#     kernel = np.ones((5, 5), np.uint8)
#     thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
#     thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
#
#     # 產生等高線
#     cntImg, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     for c in cnts:
#         # 忽略太小的區域
#         if cv2.contourArea(c) < 2500:
#             continue
#
#         # 偵測到物體，可以自己加上處理的程式碼在這裡...
#
#         # 計算等高線的外框範圍
#         (x, y, w, h) = cv2.boundingRect(c)
#
#         # 畫出外框
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # 畫出等高線（除錯用）
#     cv2.drawContours(frame, cnts, -1, (0, 255, 255), 2)
#     cnt += 1
#     # 顯示偵測結果影像
#     vout.write(frame)
#     cv2.imshow('frame', frame)
#
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     # 更新平均影像
#     cv2.accumulateWeighted(blur, avg_float, 0.01)
#     avg = cv2.convertScaleAbs(avg_float)
#
# cap.release()
# vout.release()
# cv2.destroyAllWindows()


#人臉辨識
import cv2
import numpy as np
def find_face(src):
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img=cv2.imread(src)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.08,
        minNeighbors=10,
        minSize=(30,30)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    cv2.imshow("img",img)
    cv2.imwrite('result.jpeg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# cap=cv2.VideoCapture(1)
# while True:
#     ret,frame=cap.read()
#     face=find_face(frame)
#     cv2.imshow(face)
#
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
