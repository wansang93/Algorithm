T = int(input())
for t in range(1, T+1):
    N, A, B = map(int, input().split())

    minimum = N * (A+B)
    for R in range(1, N//2+1):
        for C in range(1, int(N//R)+1):
            cal = A * abs(R-C) + B * (N-R*C)
            minimum = min(minimum, cal)

    print(f'#{t} {minimum}')
