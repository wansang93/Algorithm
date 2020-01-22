# 풀이 1
def solution(n):
    answer = n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
    return answer

# 풀이 2
def solution2(n):
    answer = 0
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            answer += i
            if i != n//i:
                answer += n//i

    return answer

print(solution2(12))