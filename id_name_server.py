from socket import *

table = {'20150001': '홍길동', '20150002': '심순애', '20150003': '박문수'}

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 3333))
sock.listen(5)

while True:

    print('Waiting...')
    data_socket, client_addr = sock.accept()
    print('Connection from', client_addr)

    id = data_socket.recv(1024).decode()
    try:
        resp = table[id]
    except:
        data_socket.send('There is not the ID'.encode())
    else:
        msg = 'The name for id({}) : {}'.format(id, resp)
        data_socket.send(msg.encode())

    data_socket.close()