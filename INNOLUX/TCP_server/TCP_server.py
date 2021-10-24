import socket
import threading

bind_ip = "192.168.0.117"
bind_port = 5554
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
    request = str(client_socket.recv(1024),encoding='utf-8')
    print("[*] 我收到: %s" % request)
    client_socket.send("666666666".encode())
    client_socket.close()
while True:
    client, addr = server.accept()
    print("[*] Acepted connection from: %s:%d" % (addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()


# import sys
# import socket
# import multiprocessing as mp
#
# def serverTCP():
#     serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     serversocket.bind(('192.168.1.114', 5554))
#     serversocket.listen(5)
#     return serversocket
#
# def handleEachClient(client):
#     read_buff = ''
#     while True:
#         read_a_char = client.recv(1).decode('utf-8')
#         if read_a_char != '\n':
#             read_buff += read_a_char
#         else:
#             print(read_buff)
#             client.sendall(('server echo ' + read_buff + '\n').encode('utf-8'))
#             read_buff = ''
#
# def main():
#     server = serverTCP()
#     while True:
#         client, addr = server.accept()
#         ip,port = addr
#         print('get a client from:',ip,':',port)
#         p = mp.Process(target=handleEachClient,args=(client,))
#         p.start()
#         client.close()
#
# if __name__ == '__main__':
#     main()