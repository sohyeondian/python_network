frame = []
msg = input('Your message : ')
size = 4

for i in range(0, len(msg), size):
    frame.append(msg[i:i + size])

print('단편화 메시지 :', frame)
print('재조립 메시지 :', ''.join(frame))