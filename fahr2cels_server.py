import sys
from socket import *

ECHO_PORT = 2500
BUFSIZE = 1024

# if len(sys.argv) > 1 :
#     port = int(eval(sys.argv[1]))
# else:
#     port = ECHO_PORT

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', 2500))
sock.listen(5)

print('Waiting for connection from client')
data_socket, client_addr = sock.accept()
print('Connected by', client_addr)

while True:
    data = data_socket.recv(BUFSIZE)
    if not data:
        break
    data = float(data.decode())
    data = 9.0 / 5.0 * data + 32.0
    data = f'{data:.1f}'
    data_socket.send(data.encode())

data_socket.close()