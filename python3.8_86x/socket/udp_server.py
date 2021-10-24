import socket
import configparser
decodE='utf-8'
uip='192.168.0.109'
uport=5554
def udp_server(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip,port))
    while True:
        try:
            data, addr = s.recvfrom(1024)
            msg = data.decode(decodE)
            print(msg)
        except :
            print("error")
    s.close()
udp_server(ip=uip,port=uport)