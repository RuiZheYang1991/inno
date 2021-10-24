#!/usr/bin/python3

import serial, time
import socket
def UdpClient(str1):
    #Host = '192.168.0.101'
    Host = '192.168.0.101'
    Port = 5555
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #input使用者自定義訊息


    #sendto(string,(IP,PORT))    string是要傳送的資訊,IP是目標(server)的IP,PORT目標埠,上面我定義的是5000
    s.sendto(str1.encode(),(Host,Port))   #str1.encode()編碼後傳送,接收端需要decode
    s.close()

def is_float(s):
    s = str(s)
    if s.count('.')==1:#判斷小數點個數
        sl = s.split('.')#按照小數點進行分割
        left = sl[0]#小數點前面的
        right = sl[1]#小數點後面的
        if left.isdigit() and right.isdigit():
            return True

    return False

def main():
    ser = serial.Serial()
    # ser.port = "/dev/ttyUSB0"
    ser.port = "COM5"

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
        except Exception as ex:
            print("open serial port error " + str(ex))
            exit()

        strtotal=""

        if ser.isOpen():
            while True:
                try:
                    # ser.flushInput()  # flush input buffer
                    # ser.flushOutput()  # flush output buffer

                    # read 8 byte data
                    response = ser.read(1024)
                    if response!= b'':

                        # response = (response.decode('utf-8', errors='ignore').replace('\n', ' ').replace('\r', ' '))
                        response1 = (response.decode('utf-8', errors='ignore').split("\r\n"))
                        for x in response1:
                            if x.find("weak low") >= 0 and x.find("T body") >= 0:
                                for b in x.split(" "):
                                    if is_float(b):
                                        msg="6,"+b+",,"
                                        UdpClient(str1=msg)
                                        print(msg)



                                    # if b.isdigit() == True:
                                    #     print(b)

                            # print(x.find("T body"))
                        # print(response)
                        # if response.index("ambience compensate  T body ="):
                        #     print("123")
                        # if len(response) > 0:
                        #     print("TTTT " + response.decode("ascii"))

                    time.sleep(0.05)
                except Exception as e1:
                    ser.close()
                    print("communicating error " + str(e1))
        else:
            print("open serial port error")
    
        

if __name__ == "__main__":
    main()
