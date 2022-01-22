dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())
for t in range(1, T+1):
    B, W = 0, 0
    N, M = map(int, input().split())

    # print(N, M)
    board = [[0] * N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    # print(board)

    # Othello algorithm
    for _ in range(M):
        nx, ny, nc = map(int, input().split())
        nx = nx - 1
        ny = ny - 1
        board[nx][ny] = nc
        # print('-----')
        for k in range(8):
            lst = []
            nnx = nx + dx[k]
            nny = ny + dy[k]
            # print(nnx, nny)
            while True:
                if 0 <= nnx < N and 0 <= nny < N:
                    if board[nnx][nny] == 0:
                        break
                    elif board[nnx][nny] == nc:
                        # print(lst, nc)
                        # lst의 값들 처리하기
                        for c in lst:
                            cx, cy = c
                            board[cx][cy] = nc
                        break
                    elif board[nnx][nny] != nc:
                        # lst의 값들 넣기
                        lst.append((nnx, nny))
                        pass
                else:
                    break
                nnx += dx[k]
                nny += dy[k]
        # print(board)
        # print(nx, ny, nc)
        # 여기 작성하기

    # print(board)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1

    print(f'#{t} {B} {W}')
