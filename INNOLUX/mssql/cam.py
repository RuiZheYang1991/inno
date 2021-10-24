class Camera():
    def __init__(self,num):
        self.cap=cv2.VideoCapture(num)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    def show(self):
        while True:
            ret,frame=self.cap.read()
            cv2.imshow("frame",frame)
            if cv2.waitKey(1)==0xFF & ord('q'):
                break
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


    # def get_frame(self):
    #     if not self.cap.isOpened():
    #         self.cap.open()
    #     img=cv2.imread("watchimg",cv2.IMREAD_GRAYSCALE)
    #     cv2.imshow('image', img)
    #     cv2.waitKey()
    #     cv2.destroyAllWindows()

    def get_frame(self,save_path):
        from datetime import datetime
        while self.cap.isOpened():

            ret, frame = self.cap.read()
            if ret:
                imgcopy = frame.copy()

                cv2.imshow("Get Picture", imgcopy)
                k = cv2.waitKey(100)
                if k == ord("z") or k == ord("Z"):
                    cv2.imwrite(save_path, frame)
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break