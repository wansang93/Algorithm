from collections import deque

# 비트연산자로 풀면 될 듯ㅋㅋ
def solution(grid):
    check_grid = int('0011001111001100', 2)
    bit = gird_to_bit(grid)
    if bit == check_grid:
        return 0

    q = deque()
    q.append((0, bit))
    while q:
        cnt, bit = q.popleft()

        # 행 비트 이동
        for i in range(4):
            for j in range(4):
                new_bit = bit ^ (1 << i)
                if new_bit == check_grid:
                    return cnt + 1
                else:
                    q.append((cnt + 1, new_bit))

        # 열 비트 이동
        for i in range(4):
            for j in range(4):
                new_bit = bit ^ (1 << i)

                if new_bit == check_grid:
                    return cnt + 1
                else:
                    q.append((cnt + 1, new_bit))


def gird_to_bit(grid):
    return int(''.join([str(i-1) for s in grid for i in s]), 2)


data = [[1,1,1,1],[2,1,2,2],[2,2,2,1],[1,1,2,2]]
data2 = [[1,1,1,2],[1,1,1,2],[2,2,2,1],[1,2,2,2]]

print(solution(data))
print(solution(data2))
