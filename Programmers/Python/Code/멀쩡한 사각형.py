# 풀이1
import math
def solution(w,h):
    answer = w * h - (w+h-math.gcd(w, h))
    return answer


# 풀이 2
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w,h):
    whole = w * h
    broken = w + h - gcd(w, h)
    answer = whole - broken
    return answer
