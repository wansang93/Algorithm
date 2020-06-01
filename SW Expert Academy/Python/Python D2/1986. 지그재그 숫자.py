T = int(input())
for i in range(1, T+1):
    N = int(input())
    answer = 0
    if N % 2 == 0:
        answer += -N//2
    else:
        answer += N//2 + 1
    print('#{} {}'.format(i, answer))
