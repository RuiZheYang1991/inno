from glob import glob
import pandas as pd

def side_ng_old(path):
    files = glob(path)

    #try:
    data = pd.concat(
        (pd.read_csv(file,sep='\t',
                    names=['0', 'Chip ID', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26'],
                     usecols=['0', 'Chip ID', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                              '25', '26'],
                     dtype={0:str, 'Chip ID':str, 2:str, 3:str, 4:str, 5:str, 6:str, 7:str, 8:str, 9:str, 10:str, 11:str, 12:str, 13:str, 14:str, 15:str, 16:str, 17:str, 18:str, 19:str, 20:str, 21:str, 22:str, 23:str, 24:str,
                              25:str, 26:str}) for file in files), ignore_index=True)
    # except:
    #     data=pd.read_csv(files[0],sep='\t',
    #                     names=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
    #                               '25', '26'],
    #                      usecols=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
    #                               '25', '26'],
    #                      dtype={0:str, 1:str, 2:str, 3:str, 4:str, 5:str, 6:str, 7:str, 8:str, 9:str, 10:str, 11:str, 12:str, 13:str, 14:str, 15:str, 16:str, 17:str, 18:str, 19:str, 20:str, 21:str, 22:str, 23:str, 24:str,
    #                               25:str, 26:str})
    #print(df)
    print('側拍總數量為:',len(data))

    # data = pd.read_csv('Summary0805.txt', sep='\t',
    #                    names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    #                           25, 26, 27])  # , names=['word1', 'word2', 'sim'])
    #
    mask1 = data['2'].map(lambda x: x == ("NG"))

    ng_data = data[mask1].reset_index(drop=True)

    print('側拍NG數量為:', len(ng_data))
    return ng_data

def filter_NGcapi(path):
    files = glob(path)
    df = pd.concat(
        (pd.read_csv(file,

                     usecols=['Start Time', 'Chip ID', 'PassFill', 'Defect Code', 'Model Name', 'Tact Time', 'Grade'],
                     dtype={'Start Time': str, 'Chip ID': str, 'PassFill': str, 'Defect Code': str, 'Model Name': str,
                            'Tact Time': str, 'Grade': str}) for file in files), ignore_index=True)

    # print(df)
    #df = df.rename(columns={"Chip ID": "PannelID", 'PassFill': "Result"})

    print('正拍總數量為:',len(df))
    after_capi = df.loc[df['PassFill'] == 'NG']
    capi_ng = after_capi.reset_index(drop=True)
    print("正拍NG數量為:",len(after_capi))
    return capi_ng



print('8月19日')
ng=side_ng_old(r'C:\Users\yang\INNOLUX\data\側拍\Summary*.txt')
caping=filter_NGcapi(r'C:\Users\yang\INNOLUX\data\正拍\Summary*.csv')
#print(caping['Chip ID'])

capid=caping['Chip ID']
side_pid=ng['Chip ID']


# with open('pid.txt',mode='w') as f:
#     for i in pid:
#         f.write(f'{i}\n')

side_l=set(i for i in side_pid)
#capi_l=set(i for i in capid)

#print('側拍與capi判NG交集數量 :',len(side_l.intersection(capi_l)))
# for side in side_l:
#     if side in capi_l:
#         print(side)

print('C檢判定屬Mura NG 數量: 4')
print('側拍與C檢人員判NG交集數量: 0')