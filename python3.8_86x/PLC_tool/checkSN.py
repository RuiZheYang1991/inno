import sys
import os
import numpy as np
import time
# import cv2
import threading
from HslCommunication import MelsecMcNet
from HslCommunication import SoftBasic

# pdID = "NULL"
# PID = "NULL"
# now = time.strftime("%Y_%m_%d",time.localtime())
#
# # Algorithm parameter
# x, y, w, h = (0, 0, 200, 200)
# imgROI_bg = np.zeros((h, w, 3), dtype=np.uint8)

# class camCapture:
#     def __init__(self, number):
#         self.Frame = []
#         self.status = False
#         self.istop = False
#         self.num = number
#
#         self.capture = cv2.VideoCapture(number)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#         #self.capture.set(cv2.CAP_PROP_FPS, 2)
#
#     def start(self):
#         print("camera started cam{}!".format(self.num))
#         threading.Thread(target=self.queryframe, daemon=True, args=()).start()
#
#     def stop(self):
#         self.isstop = True
#         print("camera stopped!")
#
#     def getframe(self):
#         return self.Frame
#
#     def queryframe(self):
#         while(not self.istop):
#             self.status, self.Frame = self.capture.read()
#
#         self.capture.release()
#
# def initEnv():
#     filepath = "/home/pi/Public/{}".format(now)
#     filepath_ori = "/home/pi/Public/{}_ori".format(now)
#     filepath_golden = "/home/pi/Public/Golden"
#     filepath_output = "/home/pi/Public/output"
#     filepath_log = "/home/pi/Public/log"
#
#     if not os.path.exists(filepath):
#         os.makedirs(filepath)
#     if not os.path.exists(filepath_ori):
#         os.makedirs(filepath_ori)
#     if not os.path.exists(filepath_golden):
#         os.makedirs(filepath_golden)
#     if not os.path.exists(filepath_output):
#         os.makedirs(filepath_output)
#     if not os.path.exists(filepath_log):
#         os.makedirs(filepath_log)
#
#     file_GoldenImg = "/home/pi/Public/Golden/GoldenROI.txt"
#     file_GoldenROI = "/home/pi/Public/Golden/GoldenIMG.jpg"
#     if not os.path.exists(file_GoldenImg):
#         f = open(file_GoldenImg, "w")
#         f.close()
#         print("Plase Train Golden Info(image)")
#     if not os.path.exists(file_GoldenROI):
#         f = open(file_GoldenROI, "w")
#         f.close()
#         print("Plase Train Golden Info(ROI location)")
#
# def updateGoldenImg():
#     global imgROI_bg
#     try:
#         img_b = cv2.imread("/home/pi/Public/Golden/GoldenIMG.jpg")
#         imgROI_b = img_b[y : y+h, x:x+w]
#         imgROI_bg = cv2.cvtColor(imgROI_b, cv2.COLOR_BGR2GRAY)
#     except:
#         print("Can't update Golden Info")
#
# def updateROI():
#     global x, y, w, h
#     f = open(r'/home/pi/Public/Golden/GoldenROI.txt')
#     roi_p = f.readlines()
#     f.close()
#     x, y, w, h = (int(roi_p[0]), int(roi_p[1]), int(roi_p[2]), int(roi_p[3]))
#
# def updatePD(file_name):
#     global pdID
#     pdID = file_name.split("_")[0]
#     os.remove("/home/pi/Public/Golden/{}".format(file_name))
#     try:
#         time.sleep(0.3)
#         updateROI()
#         updateGoldenImg()
#     except:
#         print("update PD has error")
#
# def imgFindPattern(cap_img):
#     sect = time.strftime("%H%M%S",time.localtime())
#     logfile.write("{}: image processing\n".format(sect))
#     imgORI = cap_img.copy()
#     img_gray = cv2.cvtColor(cap_img, cv2.COLOR_BGR2GRAY)
#
#     try:
#         res = cv2.matchTemplate(img_gray,imgROI_bg,cv2.TM_CCOEFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         NG = True
#         if max_val > 0.5:
#             cv2.rectangle(cap_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,0), 2)
#             NG = False
#         # else:
#             # if (max_val > 0.25):
#                 # print("PCB have SN but crooked")
#                 # cv2.rectangle(cap_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,0,255), 2)
#
#         sect = time.strftime("%H%M%S",time.localtime())
#         try:
#             if NG:
#                 cv2.imwrite("/home/pi/Public/{}/{}_NG_{}_{}.jpg".format(now, sect, pdID, PID), cap_img)
#                 cv2.imwrite("/home/pi/Public/{}_ori/{}_NG_{}_{}.jpg".format(now, sect, pdID, PID), imgORI)
#                 logfile.write("{}: save NG image\n".format(sect))
#             else:
#                 cv2.imwrite("/home/pi/Public/{}/{}_OK_{}_{}.jpg".format(now, sect, pdID, PID), cap_img)
#                 cv2.imwrite("/home/pi/Public/{}_ori/{}_OK_{}_{}.jpg".format(now, sect, pdID, PID), imgORI)
#                 logfile.write("{}: save OK image\n".format(sect))
#         except:
#             print("PID is null")
#             NG = True
#
#     except:
#         print("Golden ROI is error")
#         NG = True
#
#     sect = time.strftime("%H%M%S",time.localtime())
#     logfile.write("{}: image processed\n".format(sect))
#
#     return NG


if __name__ == "__main__":
    #initEnv()
    # logfile = open("/home/pi/Public/log/log_{}.txt".format(now), "a")
    # sect = time.strftime("%H%M%S",time.localtime())
    # logfile.write("{}: start program\n".format(sect))
    # print("Setup")
    #
    # cap = camCapture(0)
    # cap.start()
    # time.sleep(2)
    # initEnv()
    #
    #
    # free_run = False
    # trigger = False
    # PLC_conected = False
    # init_first = False
    # train_first = False
    # change_first = False
    
    plc_ip =  "192.168.3.39"
    plc_port = 1027
    melsecNet = MelsecMcNet(plc_ip, plc_port)
    if melsecNet.ConnectServer().IsSuccess == True:
        PLC_conected = True
        print("connect to PLC by {}:{} success!".format(plc_ip, plc_port))
        
    while(not cap.istop):
            # check if date update
            if now != time.strftime("%Y_%m_%d",time.localtime()):
                now = time.strftime("%Y_%m_%d",time.localtime())
                initEnv()
                logfile.close()
                logfile = open("/home/pi/Public/log/log_{}.txt".format(now), "a")
                
            # check if product update
            if len(os.listdir("/home/pi/Public/Golden")) > 2:
                # 1.GoldenIMG.jpg
                # 2.GoldenROI.txt
                for file_name in os.listdir("/home/pi/Public/Golden"):
                    if file_name == "MultROI.jpg":
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                    elif file_name == "Para":
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                    elif file_name == "Testtrigger":
                        trigger = True
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                    elif file_name == "train":
                        init_first = True
                        train_first = True
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                        if os.path.exists("/home/pi/Public/output/ori.jpg"):
                            os.remove("/home/pi/Public/output/ori.jpg")
                        sect = time.strftime("%H%M%S",time.localtime())
                        logfile.write("{}: New product training\n".format(sect))
                        print("New product training")
                        break
                    elif file_name == "StartFreeRun":
                        free_run = True
                        train_first = False
                        change_first = False
                        print("Free run start")
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                        break
                    elif file_name == "StopFreeRun":
                        free_run = False
                        change_first = True
                        print("Free run stop")
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                        break
                    elif file_name == "PLC":
                        time.sleep(0.3)
                        PLC_conected = True
                        file = open("/home/pi/Public/Golden/PLC", "r")
                        plc_inf_ = file.readline().split(":", 1)
                        plc_ip_ = plc_inf_[0]
                        plc_port_ = int(plc_inf_[1])
                        print("try to change PLC to {}:{}".format(plc_ip_, plc_port_))
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                        if plc_ip_ != plc_ip:
                            melsecNet = MelsecMcNet(plc_ip_, plc_port_)
                            if melsecNet.ConnectServer().IsSuccess == False:
                                sect = time.strftime("%H%M%S",time.localtime())
                                logfile.write("{}: connect PLC falied\n".format(sect))
                                print("connect PLC falied!")
                                PLC_conected = False
                            break
                        else:
                            if plc_port_ != plc_port:
                                melsecNet = MelsecMcNet(plc_ip_, plc_port_)
                                if melsecNet.ConnectServer().IsSuccess == False:
                                    sect = time.strftime("%H%M%S",time.localtime())
                                    logfile.write("{}: connect PLC falied\n".format(sect))
                                    print("connect PLC falied!")
                                    PLC_conected = False
                                break
                        if PLC_conected: 
                            sect = time.strftime("%H%M%S",time.localtime())
                            logfile.write("{}: connect PLC by {}:{} success\n".format(sect, plc_ip, plc_port))
                            print("connect PLC by {}:{} success!".format(plc_ip_, plc_port_))
                    elif file_name == "Time":
                        time.sleep(0.3)
                        file = open("/home/pi/Public/Golden/Time", "r")
                        win_time = file.readline()
                        os.system("sudo date --s=\"{}\"".format(win_time))
                        os.remove("/home/pi/Public/Golden/{}".format(file_name))
                        sect = time.strftime("%H%M%S",time.localtime())
                        logfile.write("{}: update system time\n".format(sect))
                    elif file_name.find("_") > 0:
                        init_first = True
                        change_first = True
                        updatePD(file_name)
                        sect = time.strftime("%H%M%S",time.localtime())
                        logfile.write("{}: Product change to {}\n".format(sect, pdID))
                        print("change to {}".format(pdID))
                        break
                    
            if trigger:
                PID = "TEST"
                frame = cap.getframe()
                cv2.imwrite("/home/pi/Public/output/test.jpg", frame)
                if imgFindPattern(frame):
                    print("TEST is NG")
                else:
                    print("TEST is OK")
                trigger = False
                
            elif free_run:
                if not os.path.exists("/home/pi/Public/output/freerunimage.jpg"):
                    frame = cap.getframe()
                    cv2.imwrite("/home/pi/Public/output/freerunimage.jpg", frame)
                    time.sleep(0.2) 
                    
            elif PLC_conected:
                if init_first:
                    # tell PLC Ready
                    melsecNet.WriteInt16("D1900", 1)
                    sect = time.strftime("%H%M%S",time.localtime())
                    logfile.write("{}: tell PLC Raspi ready\n".format(sect))
                    
                    # PLC send trigger signal                
                    if melsecNet.ReadInt16("D1810").Content == 1:
                        # get PID from PLC & Change odd char with even char
                        #sect = time.strftime("%H%M%S",time.localtime())
                        #logfile.write("{}: trigger\n".format(sect))
                        PID = melsecNet.ReadString("D1811",6).Content
                        sect = time.strftime("%H%M%S",time.localtime())
                        logfile.write("{}: get PID is {}\n".format(sect, PID))
                        #print(PID)
                        frame = cap.getframe()
                        
                        if train_first:
                            pdID = "TRAIN"
                            cv2.imwrite('/home/pi/Public/output/ori.jpg', frame)
                            train_first = False
                            
                            sect = time.strftime("%H%M%S",time.localtime())
                            cv2.imwrite("/home/pi/Public/{}/{}_OK_{}_{}_bypass.jpg".format(now, sect, pdID, PID), frame)
                            logfile.write("{}: save {} OK image by pass\n".format(sect, PID))
                            print("{} is by pass for train".format(PID))
                            # tell PLC OK by pass
                            melsecNet.WriteInt16("D1906", 1)
                                
                        elif change_first:
                            change_first = False
                            sect = time.strftime("%H%M%S",time.localtime())
                            cv2.imwrite("/home/pi/Public/{}/{}_OK_{}_{}_bypass.jpg".format(now, sect, pdID, PID), frame)
                            logfile.write("{}: save {} OK image by pass\n".format(sect, PID))
                            print("{} is by pass for changing PD".format(PID))
                            # tell PLC OK by pass
                            melsecNet.WriteInt16("D1906", 1)
                            
                        else:
                            if imgFindPattern(frame):
                                # tell PLC NG
                                melsecNet.WriteInt16("D1906", 2)
                                sect = time.strftime("%H%M%S",time.localtime())
                                logfile.write("{}: tell PLC {} is NG\n".format(sect, PID))
                                print("{} is NG".format(PID))
                            else:
                                # tell PLC OK
                                melsecNet.WriteInt16("D1906", 1)
                                sect = time.strftime("%H%M%S",time.localtime())
                                logfile.write("{}: tell PLC {} is OK\n".format(sect, PID))
                                print("{} is OK".format(PID))
                                
                        # close PLC trigger
                        melsecNet.WriteInt16("D1810", 0)
                        # tell PLC finish
                        melsecNet.WriteInt16("D1905", 1)
    if PLC_conected:        
        # tell PLC Not Ready
        melsecNet.WriteInt16("D1900", 0)
        sect = time.strftime("%H%M%S",time.localtime())
        logfile.write("{}: tell PLC Raspi lost\n".format(sect))

    # Release Camera
    cap.stop()
    cap.queryframe()    

        


        
                
