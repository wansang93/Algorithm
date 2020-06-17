T = int(input())
for t in range(1, T+1):
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]

    # 커서 개념으로 접근하기
    x, y = 0, 0
    d_num = 0  # 오른쪽(0) -> 아랫쪽(1) -> 왼쪽(2) -> 윗쪽 반복(3)
    # 커서가 처음엔 오른쪽으로 벽에 붙이치거나(out of index) 또는
    # 갈곳이 없으면(달팽이 리스트의 0이 아닌걸 만나면) 아랫쪽으로 아랫쪽, 그 다음 왼쪽, 윗쪽 반복한다.
    # while 문으로 작성시: 다음 커서가 더 이상 갈곳이 없으면 끝
    # for 문으로 작성시: N**2만큼 실행하고 끝
    for i in range(1, N**2+1):
        snail[x][y] = i
        if d_num == 0:  # 오른쪽으로 이동
            y += 1
            if y == N or snail[x][y] != 0:  # 오른쪽으로 가다가 막힌경우
                x += 1
                y -= 1
                d_num = 1
        elif d_num == 1:  # 아랫쪽으로 이동
            x += 1
            if x == N or snail[x][y] != 0:  # 아랫쪽으로 가다가 막힌경우
                x -= 1
                y -= 1
                d_num = 2
        elif d_num == 2:  # 왼쪽으로 이동
            y -= 1
            if y < 0 or snail[x][y] != 0:  # 왼쪽으로 가다가 막힌경우
                x -= 1
                y += 1
                d_num = 3
        elif d_num == 3:  # 윗쪽으로 이동
            x -= 1
            if snail[x][y] != 0:  # 윗쪽으로 가다가 막힌경우
                x += 1
                y += 1
                d_num = 0
                
    print(f'#{t}')
    for i in range(len(snail)):
        for j in range(len(snail[i])):
            print(snail[i][j], end=' ')
        print()