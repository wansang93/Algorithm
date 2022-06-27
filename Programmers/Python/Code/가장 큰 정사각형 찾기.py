def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue
            dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
            answer = max(answer, dp[i+1][j+1])

    return answer ** 2

data1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
data2 = [[0,0,1,1],[1,1,1,1]]

print(solution(data1))
print(solution(data2))
