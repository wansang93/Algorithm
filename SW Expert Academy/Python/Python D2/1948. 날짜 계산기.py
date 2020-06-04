# 풀이1: 계산하기
T = int(input())
for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = d2 - d1 + 1 + sum(days[m1:m2])

    print(f'#{t} {count}')

# 풀이2: datetime 사용
# [참고] 이 풀이는 datetime을 import 했기 때문에 메모리 문제로 정답이 안된다.
# [참고] 이 문제에서 3월 31일은 3월 1일부터 31일째라고 표현한다. 아래 풀이는 30일이라고 한다.
from datetime import datetime
T = int(input())
for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    first_date = datetime(2000, m1, d1)
    second_date = datetime(2000, m2, d2)
    count_days = (second_date - first_date).days

    print(print(f'#{t} {count_days}'))