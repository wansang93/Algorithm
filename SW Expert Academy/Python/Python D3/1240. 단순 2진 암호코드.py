T = int(input())
decryption = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    password = []
    for i in range(N):
        password.append(list(input()))

    # 패스워드에서 key를 뒤에서부터 찾는다.
    key = ''
    for i in range(N):
        for j in range(M-1, 54, -1):
            if password[i][j] == '1':
                break
        if password[i][j] == '1':
            key = password[i][j-55:j+1]
            break

    # 키를 해독한다.
    decrypted_key = []
    for i in range(0, 7*8, 7):
        temp = decryption[''.join(key[i:i+7])]
        decrypted_key.append(temp)

    # 키가 정상인지 확인한다.
    answer = 0
    if (sum(decrypted_key[0::2])*3 + sum(decrypted_key[1::2])) % 10 == 0:
        answer = sum(decrypted_key)

    print(f'#{t} {answer}')