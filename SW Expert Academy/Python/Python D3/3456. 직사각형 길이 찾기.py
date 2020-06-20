# 풀이1(Xor 원리를 이용한 풀이)
"""
A xor A = 0
0 xor B = B
따라서 A xor A xor B = B
"""
T = int(input())
for t in range(1, T+1):
    a, b, c = list(map(int, input().split()))
    answer = a ^ b ^ c
    print(f'#{t} {answer}')


# 풀이2(조건문을 이용한 풀이)
T = int(input())
for t in range(1, T+1):
    a, b, c = list(map(int, input().split()))
    if a == b:
        answer = c
    elif a == c:
        answer = b
    else:
        answer = a
    print(f'#{t} {answer}')
