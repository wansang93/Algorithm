# 풀이 중

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    answer = 0

    for i in range(N):
        for j in range(N):
            if K > len(puzzle[i]) - j:
                break
            if puzzle[i][j] == 1:
                pass
