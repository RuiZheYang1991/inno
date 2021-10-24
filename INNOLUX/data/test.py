
import pandas as pd
from glob import glob
def combine_cken_ng(path):
    files = glob(path)
    print(files)
    data = pd.concat(
        (pd.read_excel(file,

                     usecols=['Panel Id', 'Explain','Defect'],
                     dtype={'Panel Id': str, 'Explain': str,'Defect':str}) for file in files), ignore_index=True)


    # data = pd.read_csv('Summary0805.txt', sep='\t',
    #                    names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    #                           25, 26, 27])  # , names=['word1', 'word2', 'sim'])
    #
    mask1 = data['Defect'].map(lambda x: x == ("PCM00"))
    mask2 = data['Defect'].map(lambda x: x == ("PCM01"))
    mask3 = data['Defect'].map(lambda x: x == ("PCM04"))
    mask4 = data['Defect'].map(lambda x: x == ("PCM05"))
    mask5 = data['Defect'].map(lambda x: x == ("PCM06"))
    mask6 = data['Defect'].map(lambda x: x == ("PCM09"))
    mask7 = data['Defect'].map(lambda x: x == ("PCM10"))
    mask8 = data['Defect'].map(lambda x: x == ("PCM11"))
    mask9 = data['Defect'].map(lambda x: x == ("PCM12"))
    mask10 = data['Defect'].map(lambda x: x == ("PCM13"))
    mask11 = data['Defect'].map(lambda x: x == ("PCM14"))
    mask12 = data['Defect'].map(lambda x: x == ("PCM16"))
    mask13 = data['Defect'].map(lambda x: x == ("PCM17"))
    mask14 = data['Defect'].map(lambda x: x == ("PCM18"))
    mask15 = data['Defect'].map(lambda x: x == ("PCM19"))
    mask16 = data['Defect'].map(lambda x: x == ("PCM1A"))
    mask17 = data['Defect'].map(lambda x: x == ("PCM20"))
    mask18 = data['Defect'].map(lambda x: x == ("PCM21"))
    mask19 = data['Defect'].map(lambda x: x == ("PCM22"))
    mask20 = data['Defect'].map(lambda x: x == ("PCM24"))
    mask21 = data['Defect'].map(lambda x: x == ("PCM30"))
    mask22 = data['Defect'].map(lambda x: x == ("PCM31"))
    mask23 = data['Defect'].map(lambda x: x == ("PCM32"))
    mask24 = data['Defect'].map(lambda x: x == ("PCM55"))
    mask25 = data['Defect'].map(lambda x: x == ("PCM58"))
    mask26 = data['Defect'].map(lambda x: x == ("PCM59"))
    mask27 = data['Defect'].map(lambda x: x == ("PCM68"))
    mask28 = data['Defect'].map(lambda x: x == ("PCM69"))
    mask29 = data['Defect'].map(lambda x: x == ("PCM70"))
    mask30 = data['Defect'].map(lambda x: x == ("PCM71"))
    mask31 = data['Defect'].map(lambda x: x == ("PCM72"))
    mask32 = data['Defect'].map(lambda x: x == ("PCM73"))
    mask33 = data['Defect'].map(lambda x: x == ("PCM74"))
    mask34 = data['Defect'].map(lambda x: x == ("PCM75"))
    mask35 = data['Defect'].map(lambda x: x == ("PCMA2"))
    mask36 = data['Defect'].map(lambda x: x == ("PCMAC"))
    mask37 = data['Defect'].map(lambda x: x == ("PCMBB"))
    mask38 = data['Defect'].map(lambda x: x == ("PCMBR"))
    mask39 = data['Defect'].map(lambda x: x == ("PCMC1"))
    mask40 = data['Defect'].map(lambda x: x == ("PCMC2"))
    mask41 = data['Defect'].map(lambda x: x == ("PCMC3"))
    mask42 = data['Defect'].map(lambda x: x == ("PCMCD"))
    mask43 = data['Defect'].map(lambda x: x == ("PCMCK"))
    mask44 = data['Defect'].map(lambda x: x == ("PCMCM"))
    mask45 = data['Defect'].map(lambda x: x == ("PCMCP"))
    mask46 = data['Defect'].map(lambda x: x == ("PCMCQ"))
    mask47 = data['Defect'].map(lambda x: x == ("PCMD4"))
    mask48 = data['Defect'].map(lambda x: x == ("PCMD5"))
    mask49 = data['Defect'].map(lambda x: x == ("PCMD8"))
    mask50 = data['Defect'].map(lambda x: x == ("PCMD9"))
    mask51 = data['Defect'].map(lambda x: x == ("PCMF2"))
    mask52 = data['Defect'].map(lambda x: x == ("PCMK2"))
    mask53 = data['Defect'].map(lambda x: x == ("PCMV1"))
    mask54 = data['Defect'].map(lambda x: x == ("PTMC4"))
    ng_data = data[mask1 |mask2|mask3|mask4|mask5|mask6|mask7|mask8|mask9|mask10|mask11|mask14|mask15|mask16|mask17|mask18|mask19|mask20|mask21|mask22|mask23|mask24|mask25|mask26|mask27|mask28|mask29|mask30|mask31|mask32|mask33|mask34|mask35|mask36|mask37|mask38|mask39|mask40|mask41|mask42|mask43|mask44|mask45|mask46|mask47|mask48|mask49|mask50|mask51|mask52|mask53|mask54 ]
    ckenng = ng_data.reset_index(drop=True)
    print('C檢Mura 總數量為:', len(ng_data))
    return ckenng
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
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y_%m%d_%H:%M:%S')
    return df





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
    print(files)
    data = pd.concat(
        (pd.read_csv(file,sep='\t',
                     #names=['Start Time','Chip ID','PassFill', 	'Model'	,'%'	,'Grade',	'$',	'PCM17_Rank',	'PCM17_Value',	'PCM17_X,PCM17_Y',	'PCM17_Area',	'PCM16_Rank'	,'PCM16_Value',	'PCM16_X,PCM16_Y'	,'PCM16_Area'	,'PCMV1_W_Rank'	,'PCMV1_W_Value',	'PCMV1_W_X,1	PCM01_B_Rank',	'PCM01_B_Value'	,'PCM01_W_X,1',	'PCMCM_W_Rank',	'PCMCM_W_Value',	'1,PCMCM_W_Y'	,'PCM19_B_Rank'	,'PCM19_B_Value',	'1,PCM19_B_Y'	,'#'],
                     names=['0', 'Chip ID', 'PassFill', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23', '24',
                            '25', '26', '27'],

                      usecols=['Chip ID', 'PassFill'],
                      dtype={'Chip ID':str, 'PassFill':str}) for file in files), ignore_index=True,)
    #print(df)
    print('側拍總數量為:',len(data))

    # data = pd.read_csv('Summary0805.txt', sep='\t',
    #                    names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
    #                           25, 26, 27])  # , names=['word1', 'word2', 'sim'])
    #
    mask1 = data['PassFill'].map(lambda x: x == ("NG"))
    ng_data = data[mask1]
    side_ng = ng_data.reset_index(drop=True)
    print('側拍NG數量為:', len(ng_data))
    return side_ng


# df=pd.read_csv('側拍/Summary0907.txt',sep='\t')
# print(df['PCM17_Rank'])
def count_ac():
    df=side_ng(r'C:\Users\yang\INNOLUX\data\側拍\Summary*.txt')
    mask=df["PassFill"]=='NG'
    sideng=df[mask]['Chip ID'].values
    print(sideng)
    return df[mask]['Chip ID']
side=count_ac()
print("side NG:  _______________________________________\n",side)


df=combine_cken_ng(path=r'C:\Users\yang\INNOLUX\data\cken\*.xlsx')
dfr=df.rename({'Panel Id': "Chip ID"},axis="columns")["Chip ID"]
print("Cken NG:  _______________________________________\n",dfr)
print("------------------------------------------------------------")
intersected_df = pd.merge(dfr, side, how='inner')

print("交集數量為",len(intersected_df))



# capi_ng=filter_NGcapi(r'C:\Users\yang\python3.8_86x\data\正拍\Summary*.csv')
# side_ngg=side_ng(r'C:\Users\yang\python3.8_86x\data\側拍\Summary*.txt')
#
#
# side_l=set(i for i in side_ngg)
# capi_l=set(i for i in capi_ng)
#
# print('交集數量為:',len(side_l.intersection(capi_l)))
# for side in side_l:
#     if side in capi_l:
#         print(side)


