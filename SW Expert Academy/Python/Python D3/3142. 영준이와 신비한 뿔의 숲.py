# 유니콘 수(x), 트윈혼 수(y)
# x + y = m(짐승 수)
# x + 2y = n(뿔 갯수)

# 풀이1
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    y = n - m
    x = m - y

    print(f'#{t} {x} {y}')


# 풀이2(Solve in matrix on numpy)
# 웹에서는 메모리 초과로 풀리지 않음
import numpy as np

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())

    a = np.array([[1, 1], [1, 2]])
    b = np.array([m, n])

    # 옵션 주기(dtype='i1' or dtype=np.int8)
    x = np.linalg.solve(a, b).astype('i1')

    print(f'#{t} {x[0]} {x[1]}')