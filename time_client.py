import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.10.11.21', 5000) # 127.0.0.1 loop-back = 컴퓨터 자신
sock.connect(server_address)
msg = sock.recv(1024).decode()  # 다시 문자열로 바꾸는 작업
print('recev :', msg)
sock.close()