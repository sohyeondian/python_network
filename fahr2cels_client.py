from socket import *
from tkinter import *
import threading
import struct


def calculate():
    #global temp
    temp = float(entry1.get())
    sock.send(str(temp).encode())


def thread_handler(sock):
    while True:
        try:
            r_msg = sock.recv(1024)
        except:
            print('수신된 데이터 없음')
        else:
            entry2.configure(state=NORMAL)
            entry2.delete(0, END)
            entry2.insert(0, r_msg.decode())
            entry2.configure(state='readonly')
            entry1.delete(0, END)


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 2500))

root = Tk()
message_label = Label(text='Enter a temperature(C)', font=('Verdana', 13))
entry1 = Entry(font=('Verdana', 15), width=5)

recv_label = Label(text='Temperature in F', font=('Verdana', 13))
entry2 = Entry(font=('Verdana', 15), width=5, state='readonly')

calc_button = Button(text='전송', font=('Verdana', 12), command=calculate)

message_label.grid(row=0, column=0, sticky=W)
recv_label.grid(row=1, column=0, sticky=W)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
calc_button.grid(row=0, column=2, padx=10, pady=10)

t = threading.Thread(target=thread_handler, args=(sock,))
t.daemon = True
t.start()

root.mainloop()