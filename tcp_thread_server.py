from socket import *
import _thread

BUFFERSIZE = 1024
host_addr = '127.0.0.1'
port = 2500


def thread_handler(data_socket, addr):
    while True:
        msg = data_socket.recv(BUFFERSIZE).decode()
        if not msg:
            break
        print('msg :', msg)
        data_socket.send(('서버 응답 메시지 : ' + msg).encode())
    data_socket.close()
    print('closed :', addr)


if __name__ == '__main__':
    addr = (host_addr, port)
    serv_addr = socket(AF_INET, SOCK_STREAM)
    serv_addr.bind(addr)
    serv_addr.listen(5)

    while True:
        print('Waiting...')
        data_socket, client_addr = serv_addr.accept()
        print('... connection from :', client_addr)
        # create thread for client
        _thread.start_new_thread(thread_handler, (data_socket, client_addr))

    serv_addr.close()
