T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    dp = [[0] * (K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        v, c = map(int, input().split())
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j]
            if j >= v:
                dp[i][j] = max(dp[i][j], dp[i-1][j-v] + c)
    
    ans = dp[N][K]
    print(f'#{test_case} {ans}')
