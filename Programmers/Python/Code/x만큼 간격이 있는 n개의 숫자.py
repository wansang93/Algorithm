# 풀이1
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append((i+1)*x)
        
    return answer

# 풀이2
def solution(x, n):
    answer = [i for i in range(x, ((n+1)*x), x)]
    return answer