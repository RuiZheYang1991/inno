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
df=pd.read_excel(r"科九訂餐資訊.xlsx",sheet_name='晚餐Dinner Bữa tối')#usecols=("員工號碼\nEmployee No.","姓名\nName","餐別\nMeal","備註\nA.B.C\n素食"))
# n="ªn ®³19025431"
# num=n[-8:]
# num=32003616
#
# print(num in df['員工號碼\nEmployee No.'].values)
# mask=df['員工號碼\nEmployee No.']==num
# idx=df[mask].index[0]
# name=df.loc[idx,"姓名\nName"]
# meal=df.loc[idx,"備註\nA.B.C\n素食"]
# if math.isnan(meal):
#     with open(r'result.txt',mode='a',encoding="utf-8") as f:
#         f.write(str(df[mask].values[0][0])+",")
#         f.write(df[mask].values[0][1]+",")
#         f.write(df[mask].values[0][2].split(" ")[0]+"\n")
#
#
# else:
#     print("SHOW")
print(df.loc[[0,3][7,8]])

# print(str(df[mask].values[0][0])+",")
# print(df[mask].values[0][1]+",")
# print(df[mask].values[0][2].split(" ")[0]+"\n")














