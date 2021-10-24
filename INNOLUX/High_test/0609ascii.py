#!/usr/bin/python3

import serial, time
import socket
import configparser
from datetime import datetime as dt
config = configparser.ConfigParser()
config.read('config.ini')
host = config['udp']['host']
port = int(config['udp']['port'])
head = config['udp']['head']
com = config['udp']['com']

class UdpClient():
    def __init__(self,Host,Port):
        self.Host = Host
        self.Port = Port
        #self.Head = Head
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.Com=Com


    def disConnect(self):
        sock=self.s
        sock.close()
        print('關閉UDP連線')
        return sock

    def doConnect(self):
        sock = self.s

        time.sleep(1)
        try:

            sock.connect((self.Host, self.Port))

            print("建立UPD連線")
        except:
            print("UDP連接失敗")
        return sock
    def Sent_msg(self,str1):

        # sendto(string,(IP,PORT))    string是要傳送的資訊,IP是目標(server)的IP,PORT目標埠,上面我定義的是5000
        self.s.sendto(str1.encode(), (self.Host, self.Port))  # str1.encode()編碼後傳送,接收端需要decode
        #self.s.close()

def is_float(s):
    s = str(s)
    if s.count('.')==1:#判斷小數點個數
        sl = s.split('.')#按照小數點進行分割
        left = sl[0]#小數點前面的
        right = sl[1]#小數點後面的
        if left.isdigit() and right.isdigit():
            return True

    return False

def main(Com,Head):
    ser = serial.Serial()
    # ser.port = "/dev/ttyUSB0"
    ser.port = Com

    # 115200,N,8,1
    ser.baudrate = 115200
    ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
    ser.parity = serial.PARITY_NONE  # set parity check
    ser.stopbits = serial.STOPBITS_ONE  # number of stop bits

    ser.timeout = 0.5  # non-block read 0.5s
    ser.writeTimeout = 0.5  # timeout for write 0.5s
    ser.xonxoff = False  # disable software flow control
    ser.rtscts = False  # disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
    
    while True:
        try:
            ser.open()
            print('體溫計連接成功')
        except Exception as ex:
            time.sleep(1)
            print("open serial port error " + str(ex))
        strtotal=""
        if ser.isOpen():
            while True:
                try:
                    # ser.flushInput()  # flush input buffer
                    # ser.flushOutput()  # flush output buffer

                    # read 8 byte data
                    response = ser.read(1024)

                    if response!= b'':
                        print(response)


                        # response = (response.decode('utf-8', errors='ignore').replace('\n', ' ').replace('\r', ' '))
                        response1 = (response.decode('utf-8', errors='ignore').split("\r\n"))
                        #print(response1[16])
                        for x in response1:

                            if x.find("weak low") >= 0 and x.find("T body") >= 0:
                                for b in x.split(" "):
                                    if is_float(b):
                                        msg=Head+","+b+",,"
                                        #print(dt.now())
                                        conn.Sent_msg(msg)
                                        print(msg)
                                        break
                    time.sleep(0.05)
                except Exception as e1:
                    ser.close()
                    print("communicating error " + str(e1))
                    print('關閉Serial')
                    time.sleep(0.5)
                    try:
                        ser.open()
                        conn.doConnect()
                        print('重連Serial成功')
                    except:
                        print('重連Serial失敗')
        else:
            print("open serial port error")
if __name__ == "__main__":

    conn = UdpClient(Host=host, Port=port)
    conn.doConnect()
    #
    # dis=conn.disConnect()
    main(Com=com,Head=head)
    #main(Com="COM5",Head='1')
