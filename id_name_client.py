from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 3333))

id = input('The ID to find name : ')
sock.send(id.encode())
recv_msg = sock.recv(1024).decode()
print(recv_msg)

sock.close()