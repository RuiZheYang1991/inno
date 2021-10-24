import os
import shutil
ls=os.listdir("D:\ForeignIMG")
fcoutnt=0
NG_count=0
OK_count=0
for ln in ls:
    inpath=os.path.join("D:\ForeignIMG",ln)
    inner=os.listdir(inpath)

    for i in inner:
        if i != "Thumbs.db":
            if not os.path.isdir(os.path.join(inpath,inner[0])):
                print("沒有資料夾")
            else:
                fcoutnt+=1
                print("第%d個資料夾"%fcoutnt)
                oripath=os.path.join(inpath,i)
                dest = os.path.join(r"D:\\", i)
                opath=os.listdir(oripath)

                for y in opath:
                    im_path=os.path.join(oripath,y)
                    dest_impath=os.path.join(dest,y)

                    if os.path.exists(os.path.join(dest,y)):
                        print("檔案重複,跳過")
                        continue
                    else:
                        shutil.move(im_path,dest)

                    # if os.path.isdir(dest_impath):
                    #     print(dest_impath)
                    # else:
                    #     print(123)



