# import pandas as pd
# import math
# # import datetime
# # def time_check(setting,buffer):
# #     now=datetime.datetime.now()
# #     #now=datetime.strftime(now,"YY-mm-dd-hh")
# #     datetime_dt = datetime.datetime.today()# 獲得當地時間
# #     datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")
# #
# #     now_dt=datetime.datetime.strptime(datetime_str,"%Y/%m/%d %H:%M:%S")
# #     setting=setting
# #     setting_10=f"2021/07/11 {setting}:00:00"
# #     dt_10=datetime.datetime.strptime(setting_10,"%Y/%m/%d %H:%M:%S")
# #     time_buffer=int(buffer)
# #     time_delta = datetime.timedelta(hours=time_buffer) #時差
# #     dt_limit = dt_10 + time_delta #本地時間加4小時
# #
# #     print(dt_10)
# #     print(now_dt)
# #     print(dt_limit)
# #     if dt_10<now_dt<dt_limit:
# #         return True
# #     else:
# #         print("非用餐時間")
# #         return self.ui.food.appendPlainText("非用餐時間")
# #
# # print(time_check(11,4))
#
#
# #now=datetime.strptime(now,"YY-mm-dd-hh")
# # df=pd.read_excel(r"科九訂餐資訊.xlsx",sheet_name='午餐Lunch Bưã trưa',usecols='H,I,K,M,J')#usecols=("員工號碼\nEmployee No.","姓名\nName","餐別\nMeal","備註\nA.B.C\n素食"))
# # # n="ªn ®³19025431"
# # # num=n[-8:]
# # num=20025617
# # mask=df['員工號碼\nEmployee No.']==num
# # print(df[mask].values[0][3][:2])
# #print(df)
#
# # print(num in df['員工號碼\nEmployee No.'].values)
# # mask=df['員工號碼\nEmployee No.']==num
# # idx=df[mask].index[0]
# # name=df.loc[idx,"姓名\nName"]
# # meal=df.loc[idx,"備註\nA.B.C\n素食"]
# # dep=df.loc[idx,"課別"]
# # print(df)
# # if math.isnan(meal):
# #     with open(r'result.txt',mode='a',encoding="utf-8") as f:
# #         f.write(str(df[mask].values[0][0])+",")
# #         f.write(df[mask].values[0][1]+",")
# #         f.write(df[mask].values[0][2].split(" ")[0]+"\n")
# #
# #
# # else:
# #     print("SHOW")
# # df_data=pd.read_excel(r"科九訂餐資訊.xlsx",sheet_name='人員主檔')
# # mask=df_data['＊工號']==20025617
# # idx=df_data[mask].index[0]
# # name=df_data.loc[idx,"＊姓名"]
# # dep=df_data.loc[idx,"課別"]
# # print(name,dep)
#
# # print(str(df[mask].values[0][0])+",")
# # print(df[mask].values[0][1]+",")
# # print(df[mask].values[0][2].split(" ")[0]+"\n")
#
#
#
#
#
#
# # import os
# # # if not os.path.exists("log"):
# # #     os.mkdir('log')
# # #     print("資料夾建立")
# # # else:
# # #     print("資料夾存在")
# # try:
# #     os.mkdir('log')
# # except:
# #     print(123)
#
# # with open(r"222.txt",mode='a') as f:
# #     f.write()
# # barcode=88888888
# # try:
# #     with open(f"log\OK.txt", mode="a", encoding="UTF-8") as f:
# #         f.write()
# #
# # except:
# #     with open(f"log\OK.txt", mode="r", encoding="UTF-8") as f:
# #         data = f.readlines()
# #         for i in data:
# #             if i.split(",")[0] != barcode[-8:]:
# #                 continue
# # finally:
# #     with open(f"log\OK.txt", mode="a", encoding="UTF-8") as f:
# #         f.write()
#
# import datetime
# def time_check(datetime_dt, bf, lunch, dinner, sup, buffer):
#     # bf=4
#     # lunch=10
#     # dinner=16
#     # sup=23
#     # now=datetime.strftime(now,"YY-mm-dd-hh")
#
#     datetime_str = datetime_dt.strftime("%H:%M:%S")
#
#     now_dt = datetime.datetime.strptime(datetime_str, "%H:%M:%S")
#
#     dt_4 = datetime.datetime.strptime(f"{bf}:00:00", "%H:%M:%S")
#     dt_10 = datetime.datetime.strptime(f"{lunch}:00:00", "%H:%M:%S")
#     dt_16 = datetime.datetime.strptime(f"{dinner}:00:00", "%H:%M:%S")
#     dt_21 = datetime.datetime.strptime(f"{sup}:00:00", "%H:%M:%S")
#
#     time_buffer = int(buffer)
#     time_delta = datetime.timedelta(hours=time_buffer)  # 時差
#
#     dt_limit = dt_10 + time_delta  # 本地時間加4小時
#
#     if dt_10 < now_dt < dt_10 + time_delta:
#         #self.ui.food.appendPlainText(f'{dt_10}<{now_dt}<{dt_10 + time_delta}')
#         print(dt_10, now_dt, dt_10 + time_delta)
#         return "午餐Lunch Bưã trưa"
#     elif dt_4 < now_dt < dt_4 + time_delta:
#         #self.ui.food.appendPlainText(f'{dt_4}<{now_dt}<{dt_4 + time_delta}')
#         return '早餐Breakfast Bữa sáng'
#     elif dt_16 < now_dt < dt_16 + time_delta:
#         print(dt_16,now_dt,dt_16+time_delta)
#         #self.ui.food.appendPlainText(f'{dt_16}<{now_dt}<{dt_16 + time_delta}')
#         return '晚餐Dinner Bữa tối'
#     elif dt_21 < now_dt < dt_21 + time_delta:
#         #self.ui.food.appendPlainText(f'{dt_21}<{now_dt}<{dt_21 + time_delta}')
#         return '宵夜supper Bưã đêm '
#     else:
#         return "非用餐時間"
# def get_time():
#
#     datetime_dt = datetime.datetime.today()  # 獲得當地時間
#     datetime_strr = datetime_dt.strftime("%m/%d %H:%M:%S")
#     return datetime_strr
#
# from win32con import WM_INPUTLANGCHANGEREQUEST
# import win32gui
# import win32api
#
# # 语言代码
# # https://msdn.microsoft.com/en-us/library/cc233982.aspx
# LID = {0x0804: "Chinese (Simplified) (People's Republic of China)",
#        0x0409: 'English (United States)'}
#
# # 获取前景窗口句柄
# hwnd = win32gui.GetForegroundWindow()
#
# # 获取前景窗口标题
# title = win32gui.GetWindowText(hwnd)
# print('当前窗口：' + title)
#
# # 获取键盘布局列表
# im_list = win32api.GetKeyboardLayoutList()
# im_list = list(map(hex, im_list))
# print(im_list)
#
# # 设置键盘布局为英文
# result = win32api.SendMessage(
#     hwnd,
#     WM_INPUTLANGCHANGEREQUEST,
#     0,
#     0x0409)
# if result == 0:
#     print('设置英文键盘成功！')



import ctypes
import time
import os

# print('5秒后本程序会开始运行，\n请迅速将本程序置于后台，\n然后到文本编辑器之类的软件的输入框切换输入法到需要的状态\n\n')
# time.sleep(5)
#
# user32 = ctypes.WinDLL('user32', use_last_error=True)
# curr_window = user32.GetForegroundWindow()
# thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
# klid = user32.GetKeyboardLayout(thread_id)
# lid = klid & (2**16 - 1)
# lid_hex = hex(lid)
#
# print(lid_hex)
# if lid_hex == '0x409':
#     print('当前的输入法状态是英文输入模式\n\n')
# elif lid_hex == '0x804':
#     print('当前的输入法是搜狗输入法\n\n')
# else:
#     print('当前的输入法既不是英文输入也不是搜狗输入法\n\n')
#
# os.system('cmd')


def get_now():
    from datetime import datetime
    return datetime.today().strftime('%Y%m%d')
get_now()