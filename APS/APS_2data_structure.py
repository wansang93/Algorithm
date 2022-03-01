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
