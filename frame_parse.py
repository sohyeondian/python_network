import socket
import encapsulation

SIZE = 5

sock = socket.socket()
sock.connect(('127.0.0.1', 2500))

HEAD = 0x05
addr = 1
seqNo = 1
frame_seq = ''
msg = 'HELLO WORLD :) HIHI'
print('전송 메시지 :', msg)
for i in range(0, len(msg), SIZE):
    start = i
    frame_seq += encapsulation.frame(HEAD, addr, seqNo, msg[start:start+SIZE])
    seqNo += 1

sock.send(frame_seq.encode())
msg = sock.recv(2048).decode()
print('수신 프레임 :', msg)
r_frame = msg.split(chr(0x05))
del r_frame[0]

p_msg = ''
for fr in r_frame:
    p_msg += fr[10:(11+int(fr[6:10]))]
print('복원 메시지 :', p_msg)
sock.close()