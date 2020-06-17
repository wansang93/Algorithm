# 베이스 인코딩 설명(사진 참고)
# http://edentechnology.blogspot.com/2010/04/ascii-to-base64.html

# 풀이1
from base64 import b64decode

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {b64decode(input()).decode("UTF-8")}')

# 풀이2
# ~~~~~~~~풀이중~~~~~~~~~~
def base_decoding(string):
    '''
    input: Basic encoded string(string)
    output: string
    string to bit
    bit to string
    'A' 00    print(ord('A'))  # 65
    'Z' 25    print(ord('Z'))  # 90
    'a' 26    print(ord('a'))  # 97
    'z' 51    print(ord('z'))  # 122
    '+' 62    print(ord('+'))  # 43
    '/' 63    print(ord('/'))  # 47
    '''
    bit = ''
    text = ''
    # check_number and then number to char

### 숫자를 만날경우 에러 발생함ㅜㅜ원리를 이해 못함
### An error occurred here!!! Because I excepted finding number.

    # Basic encoded string -> bit
    for c in string:
        if ord('A') <= ord(c) <= ord('Z'):
            bit += bin(ord(c)-65)[2:].zfill(6)
        elif ord('a') <= ord(c) <= ord('z'):
            bit += bin(ord(c)-97+26)[2:].zfill(6)
        elif c == '+':
            bit += bin(62)[2:].zfill(6)
        elif c == '/':
            bit += bin(63)[2:].zfill(6)

    # bit -> decoded string
    for i in range(len(bit)//8):
        text += chr(int(bit[8*i:8*(i+1)], 2))

    return text

T = int(input())
for t in range(1, T+1):
    text = base_decoding(input())
    print('#{} {}'.format(t, text))