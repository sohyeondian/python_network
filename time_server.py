import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 소켓 생성
address = ('', 5000)
sock.bind(address)
sock.listen(5) # 서버환경마다 다르게 설정

while True:
    data_socket, client_addr = sock.accept() # 연결허용, 클라이언트 소켓과 주소 반환
    print('Connection requested from', client_addr)
    data_socket.send(time.ctime(time.time()).encode()) # encode() -> byte 형 메시지
    data_socket.close()