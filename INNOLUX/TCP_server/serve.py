'''
Python socket TCP多執行緒伺服器 by 鄭瑞國
1、建立網路套接字s
2、繫結地址
3、監聽
4、接受客戶端連線
5、多執行緒處理客戶端訊息
'''
import socket
import threading

s = socket.socket()  # 1、建立網路套接字s
s.bind(('192.168.1.114', 2222))  # 2、繫結地址
s.listen(5)  # 3、監聽


def handle(client, addr):
    while True:
        try:
            text = client.recv(1024)
            if not text:
                client.close()
            print(text,type(text))
            client.send(text)
            print(addr[0], addr[1], '>>', text.decode())
        except:
            print(addr[0], addr[1], '>>say goodby')
            break


while True:
    client, addr = s.accept()  # 4、接受客戶端連線
    threading._start_new_thread(handle, (client, addr))  # 5、多執行緒處理客戶端訊息