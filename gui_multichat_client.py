import socket
from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *

class ChatClient:
#    sock = None

    def __init__(self, ip, port):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((ip, port))
        self.initialize_gui()
        self.receiving_thread()

    def initialize_gui(self):
        # widget 배치 및 초기화
        self.root = Tk()
        fr = []
        for i in range(0, 5):
            fr.append(Frame(self.root))
            fr[i].pack(fill=BOTH)

        self.name_label = Label(fr[0], text='사용자 이름')
        self.recv_label = Label(fr[1], text='수신 메시지 : ')
        self.send_label = Label(fr[3], text='송신 메시지 : ')
        self.send_btn = Button(fr[3], text='전송', command=self.send_chat)
        self.quit_btn = Button(fr[3], text='종료', command=self.root.quit)
        self.chat_transcript_area = ScrolledText(fr[2], height=20, width=60)
        self.enter_text_widget = ScrolledText(fr[4], height=5, width=60)
        self.name_widget = Entry(fr[0], width=15)


        self.name_label.pack(side=LEFT)
        self.name_widget.pack(side=LEFT)
        self.recv_label.pack(side=LEFT)
        self.send_btn.pack(side=RIGHT, padx=40)
        self.quit_btn.pack(side=RIGHT, padx=20)
        self.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)
        self.send_label.pack(side=LEFT)
        self.enter_text_widget.pack(side=LEFT, padx=2, pady=2)


    def send_chat(self):
        # 메세지 전송하는 콜백함수
        sender_name = self.name_widget.get().strip() + ':'
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (sender_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.sock.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def receiving_thread(self):
        # 데이터 수신 Thread 생성, 시작
        t = Thread(target=self.receive_message, args=(self.sock,))
        t.start()

    def receive_message(self, sock):
        while True:
            buf = sock.recv(256)
            if not buf:
                break
            self.chat_transcript_area.insert('end', buf.decode('utf-8') + '\n')
            self.chat_transcript_area.yview(END)
        socket.close()


if __name__=='__main__':
    ip = input('server IP addr : ')
    if ip == '':
        ip = '127.0.0.1'
    port = 2500
    ChatClient(ip, port)
    mainloop()