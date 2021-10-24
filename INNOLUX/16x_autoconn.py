#!/usr/bin/python3

import serial, time
import socket
def UdpClient(str1):
    Host = '192.168.0.24'
    Port = 5555
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #sendto(string,(IP,PORT))    string是要傳送的資訊,IP是目標(server)的IP,PORT目標埠,上面我定義的是5000
    s.sendto(str1.encode(),(Host,Port))   #str1.encode()編碼後傳送,接收端需要decode
    s.close()


def main():
    ser = serial.Serial()
    #ser.port = "/dev/ttyUSB0"
    ser.port = "COM5"
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
            exit()
        
        if ser.isOpen():
            while True:
                try:
                    ser.flushInput()  # flush input buffer
                    ser.flushOutput()  # flush output buffer


                    # read 8 byte data
                    response = ser.read(1024)
                    #print("read 8 byte data:")
                    if len(response) >=5:
                        a = [hex(x) for x in response]
                        index = 0;
                        for x in a:
                            if x == '0x81':
                                #print(index)
                                # if index + 6 >= len(a) - 1:
                                print(a)
                                #print(a)
                                #print(a[index+3],a[index+4])
                                n1=a[index + 3]
                                n2 = a[index + 4]
                                t1=n1.split('x')[1]
                                t2=n2.split('x')[1]
                                thermal_16=t1+t2
                                thermal=int(thermal_16,16)
                                st1=str(int(thermal/100))
                                st2=str(thermal % 100)
                                stt="1,"+st1+"."+st2+",,"
                                UdpClient(stt)
                                print(stt)


                                break
                            index=index+1


                        # b = [x for x in print]
                        # print(b)  # 数值默认以10进制输出
                        # for n in b:
                        #     print("0x{:02x}".format(n))  # 以16进制输出
                        # print(response)
                    time.sleep(0.05)
                except Exception as e1:
                    ser.close()
                    print("communicating error " + str(e1))
        else:
            print("open serial port error")
    
        

if __name__ == "__main__":
    main()
