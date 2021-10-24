import pandas as pd
import math
# import datetime
# def time_check(setting,buffer):
#     now=datetime.datetime.now()
#     #now=datetime.strftime(now,"YY-mm-dd-hh")
#     datetime_dt = datetime.datetime.today()# 獲得當地時間
#     datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")
#
#     now_dt=datetime.datetime.strptime(datetime_str,"%Y/%m/%d %H:%M:%S")
#     setting=setting
#     setting_10=f"2021/07/11 {setting}:00:00"
#     dt_10=datetime.datetime.strptime(setting_10,"%Y/%m/%d %H:%M:%S")
#     time_buffer=int(buffer)
#     time_delta = datetime.timedelta(hours=time_buffer) #時差
#     dt_limit = dt_10 + time_delta #本地時間加4小時
#
#     print(dt_10)
#     print(now_dt)
#     print(dt_limit)
#     if dt_10<now_dt<dt_limit:
#         return True
#     else:
#         print("非用餐時間")
#         return self.ui.food.appendPlainText("非用餐時間")
#
# print(time_check(11,4))


#now=datetime.strptime(now,"YY-mm-dd-hh")
# df=pd.read_excel(r"科九訂餐資訊.xlsx",sheet_name='午餐Lunch Bưã trưa',usecols='H,I,K,M,J')#usecols=("員工號碼\nEmployee No.","姓名\nName","餐別\nMeal","備註\nA.B.C\n素食"))
# # n="ªn ®³19025431"
# # num=n[-8:]
# num=20025617
# mask=df['員工號碼\nEmployee No.']==num
# print(df[mask].values[0][3][:2])
#print(df)

# print(num in df['員工號碼\nEmployee No.'].values)
# mask=df['員工號碼\nEmployee No.']==num
# idx=df[mask].index[0]
# name=df.loc[idx,"姓名\nName"]
# meal=df.loc[idx,"備註\nA.B.C\n素食"]
# dep=df.loc[idx,"課別"]
# print(df)
# if math.isnan(meal):
#     with open(r'result.txt',mode='a',encoding="utf-8") as f:
#         f.write(str(df[mask].values[0][0])+",")
#         f.write(df[mask].values[0][1]+",")
#         f.write(df[mask].values[0][2].split(" ")[0]+"\n")
#
#
# else:
#     print("SHOW")
# df_data=pd.read_excel(r"科九訂餐資訊.xlsx",sheet_name='人員主檔')
# mask=df_data['＊工號']==20025617
# idx=df_data[mask].index[0]
# name=df_data.loc[idx,"＊姓名"]
# dep=df_data.loc[idx,"課別"]
# print(name,dep)

# print(str(df[mask].values[0][0])+",")
# print(df[mask].values[0][1]+",")
# print(df[mask].values[0][2].split(" ")[0]+"\n")






# import os
# # if not os.path.exists("log"):
# #     os.mkdir('log')
# #     print("資料夾建立")
# # else:
# #     print("資料夾存在")
# try:
#     os.mkdir('log')
# except:
#     print(123)

# with open(r"222.txt",mode='a') as f:
#     f.write()
# barcode=88888888
# try:
#     with open(f"log\OK.txt", mode="a", encoding="UTF-8") as f:
#         f.write()
#
# except:
#     with open(f"log\OK.txt", mode="r", encoding="UTF-8") as f:
#         data = f.readlines()
#         for i in data:
#             if i.split(",")[0] != barcode[-8:]:
#                 continue
# finally:
#     with open(f"log\OK.txt", mode="a", encoding="UTF-8") as f:
#         f.write()

import datetime
def time_check(datetime_dt, bf, lunch, dinner, sup, buffer):
    # bf=4
    # lunch=10
    # dinner=16
    # sup=23
    # now=datetime.strftime(now,"YY-mm-dd-hh")

    datetime_str = datetime_dt.strftime("%H:%M:%S")

    now_dt = datetime.datetime.strptime(datetime_str, "%H:%M:%S")

    dt_4 = datetime.datetime.strptime(f"{bf}:00:00", "%H:%M:%S")
    dt_10 = datetime.datetime.strptime(f"{lunch}:00:00", "%H:%M:%S")
    dt_16 = datetime.datetime.strptime(f"{dinner}:00:00", "%H:%M:%S")
    dt_21 = datetime.datetime.strptime(f"{sup}:00:00", "%H:%M:%S")

    time_buffer = int(buffer)
    time_delta = datetime.timedelta(hours=time_buffer)  # 時差

    dt_limit = dt_10 + time_delta  # 本地時間加4小時

    if dt_10 < now_dt < dt_10 + time_delta:
        #self.ui.food.appendPlainText(f'{dt_10}<{now_dt}<{dt_10 + time_delta}')
        print(dt_10, now_dt, dt_10 + time_delta)
        return "午餐Lunch Bưã trưa"
    elif dt_4 < now_dt < dt_4 + time_delta:
        #self.ui.food.appendPlainText(f'{dt_4}<{now_dt}<{dt_4 + time_delta}')
        return '早餐Breakfast Bữa sáng'
    elif dt_16 < now_dt < dt_16 + time_delta:
        print(dt_16,now_dt,dt_16+time_delta)
        #self.ui.food.appendPlainText(f'{dt_16}<{now_dt}<{dt_16 + time_delta}')
        return '晚餐Dinner Bữa tối'
    elif dt_21 < now_dt < dt_21 + time_delta:
        #self.ui.food.appendPlainText(f'{dt_21}<{now_dt}<{dt_21 + time_delta}')
        return '宵夜supper Bưã đêm '
    else:
        return "非用餐時間"

import configparser
config = configparser.ConfigParser()
config.read('config.ini', encoding="utf-8")
file = config['setting']['file']
bf = config['setting']['早餐']
lunch = config['setting']['午餐']
dinner = config['setting']['晚餐']
sup = config['setting']['宵夜']
buffer =config['setting']['buffer']

datetime_dt = datetime.datetime.today()  # 獲得當地時間
datetime_strr = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")
date_str = datetime_dt.strftime("%Y%m%d")

# print(time_check(datetime_dt=datetime_dt, bf=bf, dinner=dinner, lunch=lunch, sup=sup,
#                                 buffer=buffer))

import os
import os
import sys

iplist = list()
ip = '192.168.0.100'
# ip = '172.24.186.191'
#ip = 'www.baidu.com'
backinfo = os.system('ping -c 1 -w 1 %s'%ip) # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
print (backinfo)
print (type(backinfo))
if backinfo:
    print ('no')
else:
    iplist.append(ip)
    print (iplist)