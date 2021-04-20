import my_server_module as mt

sock = mt.TCPServer(3388)

print('Waiting for connection...')

data_socket, client_addr = sock.accept()
print('Connection from', client_addr)
msg = data_socket.recv(1024)
print(msg.decode())
file_name = input('File name to send (ex - test.txt) : ')
print(f"Sending '{file_name}'")
plusdir = "D:/PyCharmWorkspace/test/send/" + file_name
fn = plusdir.split('/')

data_socket.sendall(fn[-1].encode())
try:
    with open(plusdir, 'rb') as f:
        data_socket.sendfile(f, 0)
    print('Sending complete')

except:
    print(f'[Error]There is no file named {file_name} in the directory')

data_socket.close()