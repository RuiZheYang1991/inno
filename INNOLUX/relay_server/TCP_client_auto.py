import socket
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
UDP_ip = config['socket']['UDP_ip']
UDP_port = int(config['socket']['UDP_port'])
TCP_ip = config['socket']['TCP_ip']
TCP_port = int(config['socket']['TCP_port'])




while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_ip, TCP_port))
    outdata = input(":")
    print('send: ' + outdata)
    s.send(outdata.encode())

    indata = s.recv(1024)
    # if len(indata) == 0:  # connection closed
    #     s.close()
    #     print('server closed connection.')
    #     break
    print('recv: ' + indata.decode())#501,0000719991,I,20025617,楊睿哲