def solution(n):
    answer = []
    snail_list = [[0] * i for i in range(1, n+1)]
    x, y = 0, 0
    direction = 0

    for i in range(1, (n*(n+1)//2) + 1):
        snail_list[x][y] = i
        if direction == 0:
            x += 1
            if x == n or snail_list[x][y] != 0:
                x -= 1
                y += 1
                direction = 1
        elif direction == 1:
            y += 1
            if y == n or snail_list[x][y] != 0:
                x -= 1
                y -= 2
                direction = 2
        elif direction == 2:
            x -= 1
            y -= 1
            if snail_list[x][y] != 0:
                x += 2
                y += 1
                direction = 0

    for i in snail_list:
        for j in i:
            answer.append(j)
            
    return answer

print(solution(5))