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

# 1. matrix 배열 생성(0으로 채운 row행 columns열로 2차원 생성)
# 2. matrix에 1 ~ row*columns으로 채워 넣은 배열 완성
# 3. 쿼리문의 쿼리들을 하나씩 꺼냄
    # 3-1. 꺼낸 쿼리(x1, y1, x2, y2)에 1씩 빼줌(우리는 컴공이라 시작이 0)
    # 3-2. min_value(최솟값 변수 생성)
    # 3-3. 방향을 설정(오른쪽, 아래쪽, 왼쪽, 윗쪽 순)
    # 3-4. 현재 x행 y열과 그 해당 값인 matrix[x][y]를 각각 nowx, nowy, nowvalue
    # 3-5. 방향을 하나씩 꺼내옴(순서: 오른쪽, 아래쪽, 왼쪽, 윗쪽 순)
        # 1. 다음 인덱스 = 현재 인덱스 + 방향인덱스
        # 1. 예외면(해당 방향이 out of index면)
            # 1. 다음 인덱스가 해당 모서리를 벗어날 경우 방향을 바꿔야 함
        # 1. 예외가 아니면(해당 방향으로 계속)
            # nowvalue의 값과 다음 값을 바꿔주기
            # 최솟값이면 최솟값 갱신
