def solution(grid):
    answer = []

    lst = [[j for j in i] for i in grid]
    N = len(grid)
    M = len(grid[0])
    # 아래0, 위1, 오른쪽2, 왼쪽3
    ddx = [1, -1, 0, 0]
    ddy = [0, 0, 1, -1]
    ddd = {(1, 0): 0, (-1, 0): 1, (0, 1): 2, (0, -1): 3}
    # 사이클 중복 판별
    check = [[[0, 0, 0, 0] for _ in i] for i in grid]

    for i in range(4):
        temp = 0
        x, y = 0, 0
        dx, dy = ddx[i], ddy[i]
        dirc = i
        while True:
            # print(f'x: {x}, y: {y}, dirc: {dirc}')

            if check[x][y][dirc] != 0:
                answer.append(temp)
                print(x, y, dirc, check)
                break
            temp += 1
            check[x][y][dirc] = temp

            x += ddx[dirc]
            if x >= N:
                x = 0
            elif x < 0:
                x = N-1

            y += ddy[dirc]
            if y >= M:
                y = 0
            elif y < 0:
                y = M-1

            if lst[x][y] == 'R':
                if dy != 0:
                    dx, dy = dy, dx
                else:
                    dx, dy = dy, -dx
            elif lst[x][y] == 'L':
                if dx != 0:
                    dx, dy = dy, dx
                else:
                    dx, dy = dy, -dx

            dirc = ddd[(dx, dy)]

    return answer

data1 = ["SL","LR"]  # [16]
data2 = ["S"]  # [1, 1, 1, 1]
data3 = ["R","R"]  # [4, 4]
data4 = ["SR", "RS"]

print(solution(data1))
print(solution(data2))
print(solution(data3))
print(solution(data4))
