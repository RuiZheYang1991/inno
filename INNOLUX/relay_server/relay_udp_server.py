import configparser
import threading
import socket


def is_float(s):
    s = str(s)
    if s.count('.')==1:#判斷小數點個數
        sl = s.split('.')#按照小數點進行分割
        left = sl[0]#小數點前面的
        right = sl[1]#小數點後面的
        if left.isdigit() and right.isdigit():
            return True
    return False


def udp_server(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip,port))

    while True:
        print("UDP server up!")
        dic = dict()
        data,addr = s.recvfrom(1024)

        try:
            msg = data.decode().split(',')
            tem = str(round(float(msg[1]), 1))
            aisle=msg[0]

            if is_float(tem) & aisle.isdigit():
                dic[aisle] = tem
                temp_dict.update(dic)
                print(temp_dict)
        except :
            print("資料格式錯誤")
    s.close()


def handle(client, addr):
    while True:
        try:
            key=False
            text = client.recv(1024)
            # if not text:
            #     client.close()
            # recive = "501,0000719991,I,20025617,楊睿哲"
            # ttext = "502,0000719991,I,P,34.6"
            ptext=text.decode()
            ptext_list=ptext.split(",")
            loc_num=ptext.split(",")[0][-1]#走道號碼
            ttext_str=temp_dict.get(loc_num)#取str溫度
            ttext_float=float(ttext_str)#溫度 to float
            if (ttext_float>low) and (ttext_float < high):
                key=True
            if not key:
                tttext=ptext_list[0]+","+ptext_list[1]+",I,F,"+ttext_str
                client.send(tttext.encode())
                print(addr[0], addr[1], '>>', tttext)
            else:
                tttext=ptext_list[0]+","+ptext_list[1]+",I,P,"+ttext_str
                client.send(tttext.encode())
                print(addr[0], addr[1], '>>', tttext)

            temp_dict[ptext]=None
            #client.send(text)
            #print(addr[0], addr[1], '>>', ttext)
        except:
            client.send('xx'.encode())
            #print(addr[0], addr[1], '沒有收到溫度')
            client.close()
            break


if __name__=='__main__':
    temp_dict = dict()
    temp_value = []
    config = configparser.ConfigParser()
    config.read('config.ini')
    UDP_ip = config['socket']['UDP_ip']
    UDP_port = int(config['socket']['UDP_port'])
    TCP_ip = config['socket']['TCP_ip']
    TCP_port = int(config['socket']['TCP_port'])
    high = float(config['socket']['high'])
    low = float(config['socket']['low'])
    print("TCP server up")

    udp = threading.Thread(target=udp_server, args=(UDP_ip, UDP_port,))
    udp.start()

    # temp_dict={'3':'34.5'}

    ts = socket.socket()  # 1、建立網路套接字s
    ts.bind((TCP_ip, TCP_port))  # 2、繫結地址
    ts.listen(5)  # 3、監聽

    while True:
        client, addr = ts.accept()  # 4、接受客戶端連線
        tcpp=threading._start_new_thread(handle, (client, addr))  # 5、多執行緒處理客戶端訊息












