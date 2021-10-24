import requests
from json import JSONDecoder
import os


def compareimg(img1, img2):
    try:
        http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
        key = "9dUjvrMSxkKkw02tkX6jYLMs4xvo6i5O"
        secret = "B8A5hiK9uvJrHReom4KLSopiHEN75aHS"
        data = {"api_key": key, "api_secret": secret}
        files = {"image_file1": open(img1, "rb"), "image_file2": open(img2, "rb")}
        response = requests.post(http_url, data=data, files=files)
        req_con = response.content.decode("utf-8")
        req_dict = JSONDecoder().decode(req_con)
        confidence = req_dict["confidence"]
        return confidence
    except Exception:
        print("產生錯誤")
        return 0

# def compareimage(filepath1 ,filepath2):  #人臉比對
#     try:
#         http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
#         key = "9dUjvrMSxkKkw02tkX6jYLMs4xvo6i5O"
#         secret = "B8A5hiK9uvJrHReom4KLSopiHEN75aHS"
#         data = {"api_key":key, "api_secret": secret}
#         files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}
#         response = requests.post(http_url, data=data, files=files)  #進行辨識
#         req_con = response.content.decode('utf-8')  #取得結果
#         req_dict = JSONDecoder().decode(req_con)  #將結果轉為字典
#         confidence = req_dict['confidence']  #取得相似度指數
#         return confidence
#     except Exception:
#         print("產生錯誤，無法識別！")
#         return 0

def login(filepath):
#     imglib={
#         "yang1": r"C:\Users\yang\pythonProject\imglib\yang1.jpg",
#         "yang2": r"C:\Users\yang\pythonProject\imglib\yang2.jpg",
#         "ben": r"C:\Users\yang\pythonProject\imglib\ben.jpg",
#         "buy": r"C:\Users\yang\pythonProject\imglib\buy.jpg",
#     }
#     success=False
#     for img in imglib:
#         print(imglib[img])
#         if compareimg(imglib[img],filepath)>=75:
#             print("登入成功:你是%s"%img)
#             success =True
#             break
#         if not success:
#             print("登入失敗!")
#
#
#
    success = False
    img2path=str(input("請輸入img2:"))
    if compareimg(img2path, filepath) >= 75:
        print("驗證通過")
        success = True

    if not success:
        print("驗證失敗")

imgpath=input("請輸入圖img1:")
login(imgpath)
os.system('pause')