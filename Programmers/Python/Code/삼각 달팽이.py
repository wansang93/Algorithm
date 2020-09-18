def solution(n):
    answer = []
    snail_list = [[0]*i for i in range(1, n+1)]
    
    x, y = 0, 0
    direction = 0
    
    for i in range(1, ((n+1)*n//2)+1):
        snail_list[y][x] = i
        if direction == 0:
            y += 1
            if y == n or snail_list[y][x] != 0:
                y -= 1
                x += 1
                direction = 1
        elif direction == 1:
            x += 1
            if x == n or snail_list[y][x] != 0:
                y -= 1
                x -= 2
                direction = 2
        elif direction == 2:
            x -= 1
            y -= 1
            if snail_list[y][x] != 0:
                y += 2
                x += 1
                direction = 0

    for i in snail_list:
        for j in i:
            answer.append(j)

    return answer


# 다른 사람 풀이
def solution2(n):
    ans = [[0]*(i+1) for i in range(n)]
    N, p, d, c = n, 0, 0, 1

    while N:
        for i in range(N):
            if d == 0:
                ans[i+2*p][p] = c
            elif d == 1:
                ans[n-p-1][i+p+1] = c
            elif d == 2:
                ans[N-i+2*p][-p-1] = c                
            c += 1
        p += 1 if d == 2 else 0
        d = (d+1)%3 
        N -= 1

    return sum(ans, [])