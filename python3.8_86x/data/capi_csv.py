from glob import glob
import pandas as pd
def combine_capi(path):
    files = glob(path)
    df = pd.concat(
        (pd.read_csv(file,
                     usecols=['Chip ID', 'PassFill', 'Model Name', 'Grade'],
                     dtype={'Chip ID': str, 'PassFill': str,  'Model Name': str
                        , 'Grade': str}) for file in files), ignore_index=True)
    # print(df)
    print('正拍總數量為:',len(df))
    re_df=df.rename(columns={"Chip ID": "PannelID", 'PassFill': "Result"})
    return re_df

df=combine_capi(r'C:\Users\yang\python3.8_86x\data\正拍\Summary*.csv')
print(df[["PannelID","Result"]])