class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)

    def __del__(self):
        self.sock.close()

    def accept(self):
        self.data_socket, self.client_addr = self.sock.accept()
        return self.data_socket, self.client_addr

if __name__ == '__main__':
    sock = TCPServer(2500)
    data_socket, client_addr = sock.accept()
    print('수신 메세지 :', data_socket.recv(1024).decode())
    msg = 'Hello Client'
    data_socket.send(msg.encode())
    data_socket.close()