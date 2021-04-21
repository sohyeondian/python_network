import socket
import threading

clients = []


def thread_handler(data_socket, clients_addr):
    global clients
    while True:
        data = data_socket.recv(1024)

        if not data:
            clients.remove(data_socket)
            data_socket.close()
            print('disconnected with :', clients_addr)
            break

        for client in clients:
            # 내가 보낸 건 input 기록이 남아서 없애봄
            if client != data_socket:
                client.send(bytes(data))



if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 2500))
    sock.listen(5)

    while True:
        data_socket, clients_addr = sock.accept()
        clients.append(data_socket)
        t = threading.Thread(target = thread_handler, args = (data_socket, clients_addr))
        t.start()
        print('connected with :', clients_addr)