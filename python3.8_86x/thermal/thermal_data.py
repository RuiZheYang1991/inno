from glob import glob

import pandas as pd
def sTodate(sdate):
    from datetime import datetime
    date=datetime.strptime(sdate,"%Y-%m-%d")
    return date
def single(path,idx=3):
    l=glob(path)

    pid_l=[]
    pcb_l=[]
    pannel_l=[]
    grade_l=[]
    date_l=[]
    for i in l:
        if len(i.split(';')) == 2:
            file_name=i.split('\\')[idx]
            pid=file_name.split('_')[1]
            grade=file_name.split('_')[3]
            pcb=file_name.split('_')[4].split(';')[0].split(',')[0]
            pcb_thermal=file_name.split(',')[1]
            pannel_thermal = file_name.split(',')[3]
            sdate = file_name.split('_')[0]
            date=sTodate(sdate)
            pid_l.append(pid)
            pcb_l.append(pcb_thermal)
            pannel_l.append(pannel_thermal)
            grade_l.append(grade)
            date_l.append(date)
            #print(pcb_thermal)

            #print(date)
    data = {'PID': pid_l, 'PCB1': pcb_l,'Pannel1':pannel_l,'Grade':grade_l,"Date":date_l}

    df = pd.DataFrame(data)
    mask=df['Grade']=="NG"
    # print("-----------------------------NG--------------------------")
    # print(df[mask])
    # print("-----------------------------NG--------------------------")
    return df

#df=single(r'thermal\1\*')
# df=single(r'D:\熱感應\20210825\*')
# print(df)

# #df.to_excel('singal.xlsx')
# mask=df['Grade']=="NG"
# df[mask].to_excel('singal.xlsx')

def double(path,idx=5):
    l = glob(path)
    pid_l = []
    pcb1_l = []
    pannel1_l = []
    pcb2_l = []
    pannel2_l = []
    grade_l = []
    date_l = []
    for i in l :
        if len(i.split(';')) == 4 :

            file_name = i.split('\\')[idx]
            #print(len(file_name.split(';')))
            pid = file_name.split('_')[1]
            grade = file_name.split('_')[3]
            pcb = file_name.split('_')[4].split(';')[0].split(',')[0]
            pcb_thermal1 = file_name.split(',')[1]
            pannel_thermal1 = file_name.split(',')[3]
            pcb_thermal2 = file_name.split(',')[5]

            pannel_thermal2 = file_name.split(',')[7]
            sdate = file_name.split('_')[0]
            date = sTodate(sdate)
            pid_l.append(pid)
            pcb1_l.append(pcb_thermal1)
            pannel1_l.append(pannel_thermal1)
            pcb2_l.append(pcb_thermal2)
            pannel2_l.append(pannel_thermal2)
            grade_l.append(grade)
            date_l.append(date)


        # print(pcb_thermal1)
        # print(pannel_thermal1)
    data = {'PID': pid_l, 'PCB1': pcb1_l, 'Pannel1': pannel1_l, 'PCB2': pcb2_l, 'Pannel2': pannel2_l, 'Grade': grade_l, "Date": date_l}

    df = pd.DataFrame(data)
    mask = df['Grade'] == "NG"
    # print("--------------------NG-------------------------")
    # print(df[mask])
    return df
df=double(r'D:\熱感應\20210828\*')



def combine_single(path,key=0,idx=3):
    import pandas as pd
    from glob import glob
    path_l=glob(path)
    df=pd.DataFrame()
    for path in path_l:

        #print(f'{path}\\*')
        df1=single(f'{path}\\*',idx)

        df=df.append([df1])

    mask = df["Grade"] == "NG"
    if key == ("ng" or "NG"):
        return df[mask].reset_index(drop=True)
    else:
        return df.reset_index(drop=True)


def combine_double(path,key=0,idx=3):
    import pandas as pd
    from glob import glob
    path_l=glob(path)
    df=pd.DataFrame()

    #print(path_l)
    for pathh in path_l:

        #print(pathh)
        #print(f'{path}\\*')
        df1=double(f'{pathh}\\*',idx)
        #print(df1)

        df=df.append([df1])

    mask=df["Grade"]=="NG"
    if key == ("ng" or "NG"):
        return df[mask].reset_index(drop=True)
    else:
        return df.reset_index(drop=True)


ddf=combine_double(r'D:\熱感應\*')
print(ddf)

#print(glob(r'D:\熱感應\*'))
#print(glob(r'D:\熱感應\*'))