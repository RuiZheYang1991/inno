import cv2 as cv
import matplotlib.pyplot as plt

# 讀取彩色的圖片
img = cv.imread(r"C:\Users\yang\Downloads\car.jpeg")
plt.imshow(img)
plt.show()
# 轉換為灰度圖
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(img1)
plt.show()
# 用Sobel進行邊緣檢測
# # 高斯模糊
img2 = cv.GaussianBlur(img1,(5,5),10)
plt.imshow(img2)
plt.show()
# Laplacian進行邊緣檢測
img3 = cv.Sobel(img2,cv.CV_8U,1,0,ksize=1)
plt.imshow(img3)
plt.show()
img4 = cv.Canny(img3,250,100)
plt.imshow(img4)
plt.show()
# 進行二值化處理
i,img5 = cv.threshold(img4,0,255,cv.THRESH_BINARY)
plt.imshow(img5)
plt.show()
# 可以侵蝕和擴張
kernel = cv.getStructuringElement(cv.MORPH_RECT,(43,33))
img6 = cv.dilate(img5,kernel)
plt.imshow(img6)
plt.show()
# # 迴圈找到所有的輪廓
i,j = cv.findContours(img6,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
result = None
for i1 in i:
    x,y,w,h = cv.boundingRect(i1)
    if w>2*h:
        print(1)
        plt.imshow(img[y:y+h,x:x+w])
        plt.show()
        result = img[y:y+h,x:x+w]