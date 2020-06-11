T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    answer = 0

    # 가로 탐색
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
            elif puzzle[i][j] == 0:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1

    # 세로 탐색
    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                count += 1
            elif puzzle[i][j] == 0:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1    

    print(f'#{t} {answer}')