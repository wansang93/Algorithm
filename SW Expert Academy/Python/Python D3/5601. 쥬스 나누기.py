# 풀이1(분수를 문자열로 표현해서 풀기)
T = int(input())
for t in range(1, T+1):
    N = int(input())

    print(f'#{t}', end=' ')
    for i in range(1, N+1):
        print(f'1/{N}', end=' ')
    print()

# 풀이2(분수를 프린트해서 풀기)
from fractions import Fraction

T = int(input())
for t in range(1, T+1):
    N = int(input())

    print(f'#{t}', end=' ')
    for i in range(1, N+1):
        print(Fraction(1, N), end=' ')
    print()
