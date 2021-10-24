import requests
from json import JSONDecoder

def compareimage(filepath1 ,filepath2):  #人臉比對
    try:
        http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
        key = "9dUjvrMSxkKkw02tkX6jYLMs4xvo6i5O"
        secret = "B8A5hiK9uvJrHReom4KLSopiHEN75aHS"
        data = {"api_key":key, "api_secret": secret}
        files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}
        response = requests.post(http_url, data=data, files=files)  #進行辨識
        req_con = response.content.decode('utf-8')  #取得結果
        req_dict = JSONDecoder().decode(req_con)  #將結果轉為字典
        confidence = req_dict['confidence']  #取得相似度指數
        return confidence
    except Exception:
        print("產生錯誤，無法識別！")
        return 0

def login(filepath):
    success = False
    for img in imagelibrary:  #逐一比對
        print(imagelibrary[img])  #顯示比對對象
        if compareimage(imagelibrary[img], filepath) >= 75:
            print('登入成功！你是：', img)
            success = True
            break
    if not success:  #如果全部比對失敗
        print('登入失敗！')
    print('=======================')

#會員集字典
imagelibrary ={"Cynthia": "imglib/ben.jpg",
               "David": "imglib/buy.jpg",
               "jeng": "imglib/yang1.jpg",
               "Lily": "imglib/yang2.jpg"}

login('jhe.jpg')