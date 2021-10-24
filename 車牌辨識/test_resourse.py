import cv2
import time

videoIn = cv2.VideoCapture(1)
print("capture device is open: " + str(videoIn.isOpened()))
flag = 0
start = time.time()
success,frame = videoIn.read()
size = frame.shape
print(size)
while success:
	#cv2.imshow('Test camera',frame)
	success,frame = videoIn.read()
	flag += 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	if flag == 3000:
		end = time.time()
		print("3000 frames use time is (s)")
		print(end - start)
		break
videoIn.release()
