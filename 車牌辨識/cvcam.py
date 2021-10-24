# import cv2
# cap=cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#
#     # 顯示圖片
#     cv2.imshow('frame', frame)
#
#     # 若按下 q 鍵則離開迴圈
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # 釋放攝影機
# cap.release()
#
# # 關閉所有 OpenCV 視窗
# cv2.destroyAllWindows()


import cv2
import cv2
import numpy as np
#from matplotlib import pyplot as plt


class Camera():
    def __init__(self,num):
        self.cap=cv2.VideoCapture(num)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
        self.sz= (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    def show(self):
        i=0
        while True:
            ret,frame=self.cap.read()
            cv2.imshow("frame",frame)
            if cv2.waitKey(1)==0xFF & ord('q'):
                break
            elif cv2.waitKey(1)==0xFF & ord('s'):
                cv2.imwrite(f'{i}.jpg',frame)
            i+=1
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



    def record(self):
        sz = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # 為儲存視訊做準備
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = 25
        out = cv2.VideoWriter('output2.avi', fourcc, fps, sz)
        while True:
            # 一幀一幀的獲取影象
            ret, frame = self.cap.read()
            if ret == True:
                frame = cv2.flip(frame, 1)
                # 在幀上進行操作
                # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                # 開始儲存視訊
                out.write(frame)
                # 顯示結果幀
                cv2.imshow("frame", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        # 釋放攝像頭資源
        self.cap.release()
        out.release()
        cv2.destroyAllWindows()


cap1=Camera(0)
cap1.show()
#cap1.record()



