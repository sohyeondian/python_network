def frame(start_ch, addr, seq_no, msg):
    addr = str(addr).zfill(2)
    seq_no = str(seq_no).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch) + addr + seq_no + length + msg


if __name__ == '__main__':
    start_ch = 0x05  # 시작문자
    addr = 2  # 주소
    seq_no = 1  # 순서 번호

    msg = input('your message : ')
    capsule = frame(start_ch, addr, seq_no, msg)
    print(capsule)