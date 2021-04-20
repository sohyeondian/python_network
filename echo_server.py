from socket import *

port = 4000 # 포트 번호(2byte, 0~6---) 0~1023:reserved
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    print('Waiting for clients...')
    data_socket, client_addr = sock.accept()
    print('connected by', client_addr)

    msg = data_socket.recv(BUFSIZE).decode()
    if msg:
        print('Received message :', msg)
        data_socket.send(msg.encode())
    data_socket.close()