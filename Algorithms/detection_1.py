import Algorithmia
from PIL import Image

input={
    "image":"data://BBgroup/pic_LCC/object1.jpg"
    ,"output":"data://.algo/deeplearning/ObjectDetectionCOCO/temp/output.png"
    ,"min_score":"0.5"
    ,"model":"ssd_mobilenet_v1"
}

# try:
client=Algorithmia.client('simXfBXeH5cxoFSow1q2GRFduBi1')
algo = client.algo('deeplearning/ObjectDetectionCOCO/0.2.1')
result=algo.pipe(input).result['boxes']
cropobj = 'dog'
objfile = r'C:\Users\yang\Downloads\object1.jpg'
objlist=[]
for i in range(len(result)):
    if result[i]['label'] ==cropobj:
        objlist.append(i)
if len(objlist)>0:
    img1 = Image.open(objfile)
    for i in range(len(objlist)):
        n= objlist[i]
        coord = result[n]['coordinates']
        img2= img1.crop((coord['x0'],coord['y0'],coord['x1'],coord['y1']))
        img2.save(r'C:\Users\yang\Downloads\aa.jpg')

else:
    print('此途沒有要擷取的物件')

# except:
#     print('圖片檔案讀取錯誤')