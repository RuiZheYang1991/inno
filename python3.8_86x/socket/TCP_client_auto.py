import socket

HOST = '192.168.0.109'
PORT = 5554



def tcp_clienT(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    outdata = input(":")
    print('send: ' + outdata)
    s.send(outdata.encode())
    indata = s.recv(1024)
    print('recv: ' + indata.decode())

tcp_clienT(HOST,PORT)