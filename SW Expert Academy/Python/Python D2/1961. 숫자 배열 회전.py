# 문제 이해가 전혀 안되요ㅜㅜ
T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    # 알고리즘을 작성해 주세요.

    print(f'#{t}')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()