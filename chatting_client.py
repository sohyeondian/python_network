import socket
import _thread


def thread_handler(data_socket, dummy):
    while True:
        msg = data_socket.recv(1024).decode()
        if not msg:
            break
        print(msg)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('10.10.11.57', 2500))

    _thread.start_new_thread(thread_handler, (sock, 0))

    # create thread for print recv msg
    while True:
        msg = input('')
        if msg == 'end chat':
            break
        msg = '[SOPHIE] ' + msg
        sock.send(msg.encode())
