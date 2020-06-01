# 풀이1: for문을 이용
T = int(input())
for i in range(1, T+1):
    N = input()
    is_palindrome = 0
    go_from_l = ''
    go_from_r = ''
    for j in range(len(N)//2):
        go_from_r += N[j]
        go_from_l += N[-(j+1)]
    if go_from_l == go_from_r:
        is_palindrome = 1

    print('#{} {}'.format(i, is_palindrome))

# 풀이2: 풀이1 개선(for문 안에서 탐색중 앞뒤에서 달라지면 바로 중단)
T = int(input())
for i in range(1, T+1):
    N = input()
    is_palindrome = 1
    for j in range(len(N)//2):
        if N[j] != N[-j-1]:
            is_palindrome = 0
            break

    print('#{} {}'.format(i, is_palindrome))

# 풀이3: 리스트로 변환 후 리버스함수 사용
T = int(input())
for i in range(1, T+1):
    N = list(input())
    is_palindrome = 0
    reverse_N = list(reversed(N))
    if N == reverse_N:
        is_palindrome = 1

    print('#{} {}'.format(i, is_palindrome))