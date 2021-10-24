import requests
from json import JSONDecoder as jd
def compareimg(img1,img2):
    try:
        http_url="https://faceplusplus.com/facepp/v3/compare"
        key = "cllFzxC7UVMrzWKk9dfcFohiQKfjdgvz"
        secret = "uE6A_aL9hi0D3uOKkb-KVnbRo64yMUce"
        data={"api_key":key,"api_secret":secret}
        files={"img1":open(img1,"rb"),"img2":open(img2,"rb")}

        response=requests.post(http_url,data=data,files=files)
        
        req_con=response.content.decode("utf-8")
        req_dict=jd.decode(req_con)

        confidence=req_dict["confidence"]
        return confidence
    except Exception:
        print("產生錯誤")
        return 0

def show_compare(img1,img2):
    result=compareimg(img1,img2)
    print("相似度指數為:",str(result))
    if result>=75:
        print(img1,"和",img2,"為同一人")
    else:

        print(img1, "和", img2, "為不同人")

show_compare("1.jpg","2.jpg")
