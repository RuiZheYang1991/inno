import socket

HOST = '192.168.0.117'
PORT = 2222



def tcp_clienT(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    outdata = input(":")
    print('send: ' + outdata)
    s.send(outdata.encode())

    indata = s.recv(1024)
    # if len(indata) == 0:  # connection closed
    #     s.close()
    #     print('server closed connection.')
    #     break
    print('recv: ' + indata.decode())