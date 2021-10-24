import pandas as pd
from glob import glob
#df=pd.read_excel('0819.xlsx')


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
    print('C檢Mura 數量為:', len(ng_data))
    return  ckenng

df=combine_cken_ng(r'C:\Users\yang\INNOLUX\data\cken\*.xlsx')
print(df)
df.to_excel('ckenng.xlsx')