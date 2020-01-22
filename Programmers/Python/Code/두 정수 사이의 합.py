# 풀이1
def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        for i in range(a, b+1, 1):
            answer += i
    else:
        for i in range(b, a+1, 1):
            answer += i
    return answer

# 풀이2
def solution2(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        answer += i
    return answer

# 풀이3
def solution3(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    answer = sum(range(a, b+1))
    return answer