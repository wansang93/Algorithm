# 풀이1
def solution(n):
    answer = []
    strn = str(n)
    for val in strn:
        answer.append(int(val))
    answer = answer[::-1]
    return answer

# 풀이2
def solution2(n):
    answer = [int(i) for i in str(n)[::-1]]
    return answer