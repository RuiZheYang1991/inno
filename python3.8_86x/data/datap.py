# with open(r'Summary0805.txt',mode='r') as f:
#     data=f.readlines()
#     print(type(data))
#     for d in data:
#         ld=d.split("\t")
#         if ld[4] == ("K0" or "E0"):# or ld[6] or ld[10] or ld[14]
#             print(ld)


import pandas as pd

data = pd.read_csv('Summary0805.txt', sep='\t',names=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])#, names=['word1', 'word2', 'sim'])

mask1=data[4].map(lambda x : x==("K0" or "E0"))
mask2=data[6].map(lambda x : x==("K0" or "E0"))
mask3=data[10].map(lambda x : x==("K0" or "E0"))
mask4=data[14].map(lambda x : x==("K0" or "E0"))
ng_data=data[mask1 | mask2 | mask3 | mask4]
print(ng_data)


#mask = data[data[4] == ("K0" or "E0") or data[6] == ("K0" or "E0")or data[10] == ("K0" or "E0")or data[14] == ("K0" or "E0")]
# for i in range(len(data)):
#     if (data.loc[i][4] == ("K0" or "E0")) or (data.loc[i][6] == ("K0" or "E0")) or (data.loc[i][10] == ("K0" or "E0")) or (data.loc[i][14] == ("K0" or "E0")):
        #print(data.loc[i][0], data.loc[i][1], data.loc[i][2], data.loc[i][4], data.loc[i][6], data.loc[i][10], data.loc[i][14])
        #f.writelines(f'{data.loc[i][0]}\t{data.loc[i][1]}\t{data.loc[i][2]}\t{data.loc[i][4]}\t{data.loc[i][6]}\t{data.loc[i][10]}\t{data.loc[i][14]}\n')



#print(data)
#exit()
# data.to_excel('data.xlsx')
# with open('after.txt',mode='w') as f:
#     for i in range(len(data)):
#         if (data.loc[i][4] == ("K0" or "E0")) or (data.loc[i][6] == ("K0" or "E0")) or (data.loc[i][10] == ("K0" or "E0")) or (data.loc[i][14] == ("K0" or "E0")):
#             print(data.loc[i][0], data.loc[i][1], data.loc[i][2], data.loc[i][4], data.loc[i][6], data.loc[i][10], data.loc[i][14])
#             f.writelines(f'{data.loc[i][0]}\t{data.loc[i][1]}\t{data.loc[i][2]}\t{data.loc[i][4]}\t{data.loc[i][6]}\t{data.loc[i][10]}\t{data.loc[i][14]}\n')