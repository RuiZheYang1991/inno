# from os import listdir
# from os.path import *
#
# path = r"C:\Users\yang\python3.8_86x\data\正拍"
#
# # 取得所有檔案與子目錄名稱
# files = listdir(path)
#
# # 以迴圈處理
# for f in files:
#   # 產生檔案的絕對路徑
#   fullpath = join(path, f)
#   # 判斷 fullpath 是檔案還是資料夾
#   if isfile(fullpath):
#     print("檔案：", f)
#   elif isdir(fullpath):
#     print("資料夾：", f)

# 那如果要多個布林邏輯的運算呢？例如要取得身高在 172.5 以上，但在 182.5 以下的學生有那些。
# 這個時候就要使用 numpy 的 logical_and 函式了。
# import numpy as np
# condition = np.logical_and(df['height']>=172.5, df['height']<=182.5) ## 找出那些 row 符合 >=172.5 且 <= 182.5 的條件
# condition

# logical_and
# logical_or
# logical_not
# logical_xor

import pandas as pd
from glob import glob

def combine_side(path):
    files = glob(path)

    data = pd.concat(
        (pd.read_csv(file,sep='\t',
                    names=['0', '1', 'result', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26','27'],
                     usecols=['0', '1', 'result', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26','27'],
                     dtype={0:str, 1:str, 'result':str, 3:str, 4:str, 5:str, 6:str, 7:str, 8:str, 9:str, 10:str, 11:str, 12:str, 13:str, 14:str, 15:str, 16:str, 17:str, 18:str, 19:str, 20:str, 21:str, 22:str, 23:str, 24:str,
                              25:str, 26:str,27:str}) for file in files), ignore_index=True)
    return data
    print('側拍總數量為:',len(data))

def combine_capi(path):
    files = glob(path)
    df = pd.concat(
        (pd.read_csv(file,
                     usecols=['Start Time', 'Chip ID', 'PassFill', 'Defect Code', 'Model Name', 'Tact Time', 'Grade'],
                     dtype={'Start Time': str, 'Chip ID': str, 'PassFill': str, 'Defect Code': str, 'Model Name': str,
                            'Tact Time': str, 'Grade': str}) for file in files), ignore_index=True)
    # print(df)
    print('正拍總數量為:',len(df))
    return df



print('0804-0810數據統計')

def filter_NGcapi(path):
    files = glob(path)
    df = pd.concat(
        (pd.read_csv(file,

                     usecols=['Start Time', 'Chip ID', 'PassFill', 'Defect Code', 'Model Name', 'Tact Time', 'Grade'],
                     dtype={'Start Time': str, 'Chip ID': str, 'PassFill': str, 'Defect Code': str, 'Model Name': str,
                            'Tact Time': str, 'Grade': str}) for file in files), ignore_index=True)

    # print(df)
    df = df.rename(columns={"Chip ID": "PannelID", 'PassFill': "Result"})

    print('正拍總數量為:',len(df))
    after_capi = df.loc[df['Result'] == 'NG']
    capi_ng = after_capi.reset_index(drop=True)
    print("正拍NG數量為:",len(after_capi))
    return capi_ng

# ng_capi=filter_NGcapi(r'C:\Users\yang\python3.8_86x\data\正拍\Summary*.csv')


import pandas as pd
def side_ng_old(path):
    files = glob(path)

    data = pd.concat(
        (pd.read_csv(file,sep='\t',
                    names=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26'],
                     usecols=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26'],
                     dtype={0:str, 1:str, 2:str, 3:str, 4:str, 5:str, 6:str, 7:str, 8:str, 9:str, 10:str, 11:str, 12:str, 13:str, 14:str, 15:str, 16:str, 17:str, 18:str, 19:str, 20:str, 21:str, 22:str, 23:str, 24:str,
                              25:str, 26:str}) for file in files), ignore_index=True)
    #print(df)
    print('側拍總數量為:',len(data))

    # data = pd.read_csv('Summary0805.txt', sep='\t',
    #                    names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    #                           25, 26, 27])  # , names=['word1', 'word2', 'sim'])
    #
    mask1 = data['4'].map(lambda x: x == ("K0" or "E0"))
    mask2 = data['6'].map(lambda x: x == ("K0" or "E0"))
    mask3 = data['10'].map(lambda x: x == ("K0" or "E0"))
    mask4 = data['14'].map(lambda x: x == ("K0" or "E0"))
    mask5 = data['1'].map(lambda x: x == ("K0" or "E0"))
    ng_data = data[mask1 | mask2 | mask3 | mask4]

    print('側拍NG數量為:', len(ng_data))
    return ng_data




def side_ng(path):
    files = glob(path)

    data = pd.concat(
        (pd.read_csv(file,sep='\t',
                    # names=['0', 'PannelID', 'result', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                    #           '25', '26','27'],
                    #  usecols=['0', 'PannelID', 'result', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                    #           '25', '26','27'],
                    #  dtype={0:str, 1:str, 'result':str, 3:str, 4:str, 5:str, 6:str, 7:str, 8:str, 9:str, 10:str, 11:str, 12:str, 13:str, 14:str, 15:str, 16:str, 17:str, 18:str, 19:str, 20:str, 21:str, 22:str, 23:str, 24:str,
                    #           25:str, 26:str,27:str}) for file in files), ignore_index=True)


                      usecols=['PannelID', 'Result'],
                      dtype={'PannelID':str, 'Result':str}) for file in files), ignore_index=True)
    #print(df)
    print('側拍總數量為:',len(data))

    # data = pd.read_csv('Summary0805.txt', sep='\t',
    #                    names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    #                           25, 26, 27])  # , names=['word1', 'word2', 'sim'])
    #
    mask1 = data['Result'].map(lambda x: x == ("NG"))
    ng_data = data[mask1]
    side_ng = ng_data.reset_index(drop=True)
    print('側拍NG數量為:', len(ng_data))
    return side_ng







capi_ng=filter_NGcapi(r'C:\Users\yang\python3.8_86x\data\正拍\Summary*.csv')
side_ng=side_ng(r'C:\Users\yang\python3.8_86x\data\側拍\Summary*.txt')


side_l=set(i for i in side_ng)
capi_l=set(i for i in capi_ng)

print('交集數量為:',len(side_l.intersection(capi_l)))
for side in side_l:
    if side in capi_l:
        print(side)


# for i in glob(r'C:\Users\yang\python3.8_86x\data\data\側拍\Summary*.txt'):
#     print(i)

#print(glob(r'C:\Users\yang\python3.8_86x\data\側拍\Summary*.txt'))