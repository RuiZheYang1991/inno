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
    print(outdata.encode('unicode_escape'),"unicode")
    print(outdata.encode('utf8'), "utf8")

    s.send(outdata.encode('unicode_escape'))

    indata = s.recv(1024)
    # if len(indata) == 0:  # connection closed
    #     s.close()
    #     print('server closed connection.')
    #     break
    print(indata)
    print('recv: ' + indata.decode('unicode_escape'))#501,0000719991,I,20025617,楊睿哲