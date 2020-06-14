T = int(input())
for t in range(1, T+1):
    # L: L분 이상
    # U: U분 이하 운동
    # X: X분 만큼 운동
    L, U, X = map(int, input().split())

    if X < L:
        answer = L - X
    elif L <= X <= U:
        answer = 0
    else:
        answer = -1

    print(f'#{t} {answer}')