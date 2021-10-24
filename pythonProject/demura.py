import os
import shutil
from json import JSONDecoder
with open(r"C:\Users\yang\Desktop\側拍\20210319_Summary.txt") as f:
    okl=[]
    ngl=[]
    f=f.readlines()
    for i in f:
        i = i.split("\t")
        if i[1]!='DemuraTest':
            if i[4] =="A0" or "C0":
                okl.append()

            print(i)

