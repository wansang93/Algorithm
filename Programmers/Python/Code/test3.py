def solution(v):
    global check_list, n, answer
    n = len(v)
    answer = [0, 0, 0]

    for y in range(n):
        for x in range(n):
            check_list = []
            temp = v[y][x]
            if temp == 0:
                answer[0] += 1
            elif temp == 1:
                answer[1] += 1
            elif temp == 2:
                answer[2] += 1
            else:
                continue
            

    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))  # [2,1,2]
print(solution([[0,0,1],[2,2,1],[0,0,0]]))  # [2,1,1]