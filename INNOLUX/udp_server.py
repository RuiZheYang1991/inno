# import socket, traceback
#
# host = '192.168.50.221'
# port = 8888
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind((host, port))
#
# while 1:
#     try:
#         message, address = s.recvfrom(1024)
#         print ('Got data from', address, ':', message)
#         s.sendto(message, address)
#
#     except (KeyboardInterrupt, SystemExit):
#         raise
#     except:
#         traceback.print_exc()


import time
import socket   #python內部模組,直接匯入

#socket(family[,type[,proto]]])  建立一個scoket物件
#family定義IP協議,分為IPv4,IPv6.

#socket.AF_INET IPv4

#socket.AF_INET6 IPv6
from datetime import datetime as dt
#type SOCK_DGRAM UDP   SOCK_STREAM TCP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #建立一個IPv4,UDP連結物件
#bind(('IP',埠),),如果IP是空字元,那麼表示本機任何可用IP,埠自定義,但不要和其他在用或應用程式預設埠重複
s.bind(('192.168.0.101',5554))   #127.0.0.1表示本機IP,定義服務端接收資訊的埠是5000
while True:

#recvfrom接收一個引數,該引數是定義了每次收到的最大位元組數;

#recvfrom返回兩個元素,第一個元素收到的資訊(字串),第二個元素含有兩個字串(或元素)的元組,分別是傳送者的IP,傳送者的埠號

    data,addr = s.recvfrom(1024)
    print(dt.now())
    print('received message:{0}'.format(data.decode()))    #收到的訊息需要decode解碼
    print('The message is from PORT{0},IP{1}.'.format(addr[1],addr[0]))
    if data.decode().lower()=='quit':
        break
s.close()