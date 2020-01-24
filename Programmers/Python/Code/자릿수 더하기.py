# 풀이1
def solution(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])

    return answer

# 풀이2
def solution2(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer

# 풀이3
def solution3(n):
    answer = sum([int(i) for i in str(n)])
    return answer