# 풀이2
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i // n,i % n) + 1)
    return answer

# 내 풀이
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = i // n, i % n
        v = col + 1 if row < col else row + 1
        answer.append(v)
    return answer
