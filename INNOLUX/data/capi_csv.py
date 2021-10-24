from glob import glob
import pandas as pd
def combine_capi(path):
    files = glob(path)
    df = pd.concat(
        (pd.read_csv(file,
                     usecols=['Start Time','Chip ID', 'PassFill', 'Model Name', 'Grade'],
                     dtype={'Start Time':str,'Chip ID': str, 'PassFill': str,  'Model Name': str
                        , 'Grade': str}) for file in files), ignore_index=True)
    # print(df)
    print('正拍總數量為:',len(df))
    #re_df=df.rename(columns={"Chip ID": "PannelID", 'PassFill': "Result"})
    return df

df=combine_capi(r'C:\Users\yang\python3.8_86x\data\正拍\Summary*.csv')
#print(df[["PannelID","Result"]])

df['Start Time']=pd.to_datetime(df['Start Time'],format='%Y_%m%d_%H:%M:%S')
time=df['Start Time']
fill=df['PassFill']
pannelID=df['Chip ID']
mask=df['PassFill']=="NG"
print(df[mask])


# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5,6,7,8]
# y_1 = [1,4,9,16,25,36,49,64]
# y_2 = [1,8,27,64,125,216,343,512]
# plt.plot(x,y_1,x, y_2) #畫線
# plt.tick_params(axis='both', labelsize=24, color='green')
# plt.show() #顯示繪製的圖形