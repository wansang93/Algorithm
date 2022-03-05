# C언어 Python으로 연습하기

# stack
"""
stack은 리스트, 배열 아무거나 구현 가능
stack은 규칙임, 자료구조x
stack은 3가지만 알면 됨
위에서 넣기: push
위에서 읽기: top
위에서 빼기: pop
"""

from mimetypes import init


lst = [0] * 10
sp = -1

def push(a):
    global sp
    sp += 1
    lst[sp] = a


def top():
    return lst[sp]


def pop():
    global sp
    temp = lst[sp]
    lst[sp] = 0
    sp -= 1
    return temp

push(1)
push(2)
push(3)
push(5)
push(7)
print(top())
print(pop())
print(top())
print(pop())
push(4)
print(top())
print(lst)

####################################################################################################

# 문자열은 이상하게 안했네?ㅋㅋ 파이썬이랑 다른점
"""
arr = "1234" 넣으면 5개가 들어감 (1234 + null)
생각해보니까 옛날에 배웠네ㅋㅋ
"""

####################################################################################################

lst = [[0] * 3 for _ in range(3)]
t = 1
for i in range(2, -1, -1):
    for j in range(2, -1, -1):
        lst[i][j] = t
        t += 1

for i in lst:
    print(*i, end=" ")
print()


lst = [[0] * 3 for _ in range(3)]
t = 1
for y in range(2, -1, -1):
    for x in range(y, 3):
        lst[y][x] = t
        t += 1

for i in lst:
    print(*i, end="")
print()

lst = [[0] * 3 for _ in range(3)]
t = 1
for y in range(2, -1, -1):
    for x in range(2-y):
        lst[y][x] = t
        t += 1

for i in lst:
    print(*i, end=" ")
print()


"""
코테에서 Linbrary 쓸때는
Library를 안쓰면 구현이 너무 지겨울 때부터
그래야 실력이 늠
"""

