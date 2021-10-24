# import Algorithmia
# import cv2
# input={
#     "image":"data://BBgroup/pic_LCC/facedetect2.jpg",
#     "numResults":7
#
#
# }
#
#
# try:
#     client = Algorithmia.client('simXfBXeH5cxoFSow1q2GRFduBi1')
#     algo = client.algo('algo://Andrazp/EmoticonbasedSentimentAnalysis')
#     emotion=algo.pipe(input).result['results'][0]['emotions']
#     print('表情可能為:'+emotion[0]['label'])
#     print('所有可能性')
#     print('%-10s %-10s' % ('confidence','emotion'))
#     print('================= ================')
#     for i in range(len(emotion)):
#         print('%-10s %-10s' %(emotion[i]['label'],emotion[i]['confidence']))
#
#     img=cv2.imread(r'C:\Users\yang\Algorithms\media\facedetect2.jpg')
#     rect = algo.pipe(input).result['results'][0]['bbox']  # 取得臉部坐標
#     cv2.rectangle(img, (rect['left'], rect['top']), (rect['right'], rect['bottom']), (0, 0, 255), 2)  # 畫出框線
#     cv2.namedWindow("win")
#     cv2.imshow("win", img)  # 顯示圖片
#     cv2.waitKey(0)
#     cv2.destroyWindow("win")
# except:
#     print('沒有偵測到人臉資訊！')


import Algorithmia
import cv2

input = {
    "image": "data://BBgroup/pic_LCC/facedetect2.jpg",
    "numResults": 7  # 傳回的情緒種類數目
}
try:
    client = Algorithmia.client('simXfBXeH5cxoFSow1q2GRFduBi1')
    algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/1.0.1')
    emotion = algo.pipe(input).result['results'][0]['emotions']
    print('此人的表情為 ' + emotion[0]['label'])
    print('所有可能性：')
    print('%-10s %-10s' % ('confidence', 'emotion'))
    print('========== ==========')
    for i in range(len(emotion)):
        print('%-10s %-10s' % (emotion[i]['label'], emotion[i]['confidence']))

    img = cv2.imread('facedetect2.jpg')  # 讀取本機圖片
    rect = algo.pipe(input).result['results'][0]['bbox']  # 取得臉部坐標
    cv2.rectangle(img, (rect['left'], rect['top']), (rect['right'], rect['bottom']), (0, 0, 255), 2)  # 畫出框線
    cv2.namedWindow("win")
    cv2.imshow("win", img)  # 顯示圖片
    cv2.waitKey(0)
    cv2.destroyWindow("win")
except:
    print('沒有偵測到人臉資訊！')
