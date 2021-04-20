import my_server_module as mt
import sys

port = 2500
sock = mt.TCPServer(port)


while True:
    data_socket, client_addr = sock.accept()
    print('Conected by', client_addr)
    data = data_socket.recv(1024)
    if data:
        msg = data.decode()
        if msg == 'quit server': break
        print('Received message :', msg)
        data_socket.send(data)
    data_socket.close()

data_socket.close()