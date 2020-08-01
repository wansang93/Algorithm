# 베이스 인코딩 설명(사진 참고)
# http://edentechnology.blogspot.com/2010/04/ascii-to-base64.html

# 풀이1
from base64 import b64decode

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {b64decode(input()).decode("UTF-8")}')

# 풀이2
value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base_dic = {val: idx for idx, val in enumerate(value)}

def base_decoding(string):
    bit = ''
    text = ''
    for i in string:
        num = bin(base_dic[i])[2:].zfill(6)
        bit += num

    for i in range(0, len(bit), 8):
        text += chr(int(bit[i:i+8], 2))

    return text

T = int(input())
for t in range(1, T+1):
    text = base_decoding(input())
    print(f'#{t} {text}')