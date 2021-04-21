from socket import *
from threading import *

class MultiChatServer:
    clients =[]
    def __init__(self):
        self.message = ''

        # socket
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.ip = ''
        self.port = 2500
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        # listen
        print("Waiting for clients")
        self.sock.listen(100)
        # accept_client()
        self.accept_client()

    def accept_client(self):
        while True:
            # 연결 수락
            client = data_socket, client_addr = self.sock.accept()
            # 연결 소켓 추가
            if client not in self.clients:
                self.clients.append(client)
            print('connected with',client_addr)
            # MSG 수신 스레드 생성/ 실행(receive_message())
            t = Thread(target=self.receive_message, args=(data_socket, client_addr))
            t.start()

    def receive_message(self, data_socket, addr):
        while True:
            try:
                # 메시지 수신
                msg = data_socket.recv(256)
                if not msg:
                    break
            except:
                continue
            else:
                # send_all_clients()
                self.message = msg.decode()
                self.send_all_clients(data_socket)
        data_socket.close()


    def send_all_clients(self, data_socket):
        # 발신자를 제외한 모든 연결 소켓으로 메시지 전송
        for client in self.clients:
            d_socket, addr = client
            if d_socket != data_socket:
                try:
                    d_socket.sendall(self.message.encode())
                except:
                    self.clients.remove(client)
                    print('Disconnected with', addr)


if __name__=='__main__':
    MultiChatServer()