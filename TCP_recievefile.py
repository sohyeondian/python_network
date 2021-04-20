import socket

sock = socket.socket()
host = "127.0.0.1"
port = 3388

sock.connect((host,port))
sock.send("I am ready.".encode())
fn = sock.recv(1024).decode()

with open('D:/PyCharmWorkspace/test/receive/'+fn, 'wb') as f:
    print('File opened')
    print('Receiving file...')

    while True:
        data = sock.recv(8192)
        if not data:
            break
        f.write(data)

    print('Download Complete')

sock.close()
print('Connection closed')