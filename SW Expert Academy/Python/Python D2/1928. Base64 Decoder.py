# 베이스 인코딩 설명(사진 참고)
# http://edentechnology.blogspot.com/2010/04/ascii-to-base64.html

# ~~~~~~~~풀이중~~~~~~~~~~
def base_decoding(string):
    '''
    Basic incoding
    'A' 00    print(ord('A'))  # 65
    'Z' 25    print(ord('Z'))  # 90
    'a' 26    print(ord('a'))  # 97
    'z' 51    print(ord('z'))  # 122
    '+' 62    print(ord('+'))  # 43
    '/' 63    print(ord('/'))  # 47
    '''
    bit = ''
    for c in string:
        if ord('A') <= ord(c) <= ord('Z'):
            bit += (bin(ord(c) - 65)[2:]).zfill(6)
        elif ord('a') <= ord(c) <= ord('z'):
            bit += (bin(ord(c) - 97 + 26)[2:]).zfill(6)
        elif c == '+':
            bit += (bin(62)[2:]).zfill(6)
        elif c == '/':
            bit += (bin(63)[2:]).zfill(6)

    return bit

T = int(input())
for t in range(1, T+1):
    text_by_base = input()
    text = ''

    for i in range(len(text_by_base)//4):
        bit = base_decoding(text_by_base[4*i:4*(i+1)])
        
        text += chr(int(bit[:8], 2))
        text += chr(int(bit[8:16], 2))
        text += chr(int(bit[16:], 2))
        
    print('#{} {}'.format(t, text))

