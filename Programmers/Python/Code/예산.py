# 풀이1
def solution(d, budget):
    d = sorted(d)
    answer = 0
    sum_d = 0
    for i in d:
        if sum_d+i > budget:
            break
        sum_d += i
        answer += 1
    return answer

# 풀이2
def solution2(d, budget):
    answer = 0
    for i in sorted(d):
        if budget - i < 0:
            break
        budget -= i
        answer += 1
    return answer

# 풀이3
def solution3(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

