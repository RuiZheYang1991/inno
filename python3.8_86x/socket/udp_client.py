# import socket
# address = ('127.0.0.1', 10141)
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# while True:
#     message = raw_input()
#     if not message:
#         break
#     s.sendto(message, address)
#     s.close()

# import os, sys, time
# import socket
#
#
# def doConnect(host, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         sock.connect((host, port))
#     except:
#         pass
#     return sock
#
#
# def main():
#     host, port = "127.0.0.1", 8888
#     print(host, port)
#
#     sockLocal = doConnect(host, port)
#
#     while True:
#         try:
#             msg = str(time.time())
#             sockLocal.send(msg)
#             print("send msg ok : ", msg)
#
#             print("recv data :", sockLocal.recv(1024))
#
#         except socket.error:
#             print("\r\nsocket error,do reconnect ")
#
#             time.sleep(3)
#             sockLocal = doConnect(host, port)
#         except:
#             print('\r\nother error occur ')
#
#             time.sleep(3)
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     main()
uip = '192.168.0.109'
uport = 5554
encodE='utf-8'
import socket
def UdpClient(ip,port):

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #input使用者自定義訊息

    str1=input("ssss")
    #sendto(string,(IP,PORT))    string是要傳送的資訊,IP是目標(server)的IP,PORT目標埠,上面我定義的是5000
    s.sendto(str1.encode(encodE),(ip,port))   #str1.encode()編碼後傳送,接收端需要decode
    s.close()


while True:
    str1 = UdpClient(ip=uip,port=uport)
    if str1 =='quit':
        break