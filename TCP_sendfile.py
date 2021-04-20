import my_server_module as mt

sock = mt.TCPServer(3388)

print('Waiting for connection...')

data_socket, client_addr = sock.accept()
print('Connection from', client_addr)
msg = data_socket.recv(1024)
print(msg.decode())
file_name = input('File name to send (ex - D:/PyCharmWorkspace/test.txt) : ')
print(f"Sending '{file_name}'")
fn = file_name.split('/')

data_socket.sendall(fn[-1].encode())
try:
    with open(file_name, 'rb') as f:
        data_socket.sendfile(f, 0)
    print('Sending complete')

except:
    print(f'[Error]There is no file named {file_name} in the directory')

data_socket.close()