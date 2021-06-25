def solution(rows, columns, queries):
    answer = []

    matrix = [[0] * columns for i in range(rows)]

    idx = 1
    for x in range(rows):
        for y in range(columns):
            matrix[x][y] = idx
            idx += 1

    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x-1, query)

        min_value = 10001
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        nowx = x1
        nowy = y1
        nowvalue = matrix[nowx][nowy]

        for i in range(4):
            dy, dx = direction[i]
            while True:
                nexty = nowy + dy
                nextx = nowx + dx
                # 예외 처리
                if nextx < x1 or nextx > x2 or nexty < y1 or nexty > y2:
                    break
                # 예외가 아니면
                else:
                    # nowvalue의 값과 다음 값을 바꿔주기
                    nowvalue, matrix[nextx][nexty] = matrix[nextx][nexty], nowvalue
                    nowy = nexty
                    nowx = nextx
                    min_value = min(min_value, nowvalue)

        answer.append(min_value)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# [8, 10, 25]
