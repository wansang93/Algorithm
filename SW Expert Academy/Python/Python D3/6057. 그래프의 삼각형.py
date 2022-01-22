
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    # Algorithm
    cnt = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if graph[i][j] and graph[j][k] and graph[k][i]:
                    cnt += 1

    print(f'#{t} {cnt}')
