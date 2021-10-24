#!/usr/bin/python3

import serial, time
import socket
import configparser



# def doConnect(host,port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try :
#         sock.connect((host,port))
#     except :
#         pass
#     return sock

class UdpClient():
    def __init__(self,Host,Port):
        self.Host = Host
        self.Port = Port
        #self.Head = Head
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.Com=Com


    def doConnect(self):
        sock = self.s
        try:

            sock.connect((self.Host, self.Port))

            print("UPD連線成功")
        except:
            print("UDP連接失敗")
        return sock
    def Sent_msg(self,str1):

        # sendto(string,(IP,PORT))    string是要傳送的資訊,IP是目標(server)的IP,PORT目標埠,上面我定義的是5000
        self.s.sendto(str1.encode(), (self.Host, self.Port))  # str1.encode()編碼後傳送,接收端需要decode
        #self.s.close()


def main(Com,Head):
    ser = serial.Serial()
    # ser.port = "/dev/ttyUSB0"
    ser.port = Com
    # 115200,N,8,1
    ser.baudrate = 9600
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
        except Exception as ex:
            print("open serial port error " + str(ex))

        if ser.isOpen():
            while True:
                try:
                    ser.flushInput()  # flush input buffer
                    ser.flushOutput()  # flush output buffer

                    # read 8 byte data
                    response = ser.read(1024)
                    # print("read 8 byte data:")
                    if len(response) >= 5:
                        a = [hex(x) for x in response]
                        index = 0;
                        for x in a:
                            if x == '0x81':
                                # print(index)
                                # if index + 6 >= len(a) - 1:
                                #print(a)
                                # print(a)
                                # print(a[index+3],a[index+4])
                                n1 = a[index + 3]
                                n2 = a[index + 4]
                                t1 = n1.split('x')[1]
                                t2 = n2.split('x')[1]
                                thermal_16 = t1 + t2
                                thermal = int(thermal_16, 16)
                                st1 = str(int(thermal / 100))
                                st2 = str(thermal % 100)
                                stt = Head+"," + st1 + "." + st2 + ",,"
                                conn.Sent_msg(stt)
                                print(stt)



                                break
                            index = index + 1

                        # b = [x for x in print]
                        # print(b)  # 数值默认以10进制输出
                        # for n in b:
                        #     print("0x{:02x}".format(n))  # 以16进制输出
                        # print(response)
                    time.sleep(0.05)
                except Exception as e1:
                    ser.close()
                    print("communicating error " + str(e1))
                    conn.doConnect()
                    time.sleep(1)
                    try:
                        ser.open()
                    except:
                        pass

        else:
            print("open serial port error")



if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config['udp']['host']
    port = int(config['udp']['port'])
    head = config['udp']['head']
    com = config['udp']['com']
    conn=UdpClient(Host=host,Port=port)
    conn.doConnect()
    main(Com=com,Head=head)
    #main(Com="COM5",Head='1')

