import Algorithmia

input={
r'C:\Users\yang\Algorithms\media\facedetect2.jpg'



}

try:
    client=Algorithmia.client('')
    algo=client.algo('')
    print(algo.pipe(input).result)
except:
    print('圖檔錯誤')