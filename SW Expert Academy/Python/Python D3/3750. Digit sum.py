T = int(input())
ans = []
for test_case in range(1, T+1):
    N = int(input())
    while N // 10:
        tmp = 0
        while N:
            tmp += N % 10
            N //= 10
        N = tmp
    ans.append(N)

for i, v in enumerate(ans, 1):
    print(f'#{i} {v}')

