# DP, 브루탈, 규칙, 탐색 등 경우에 따라 어떤 것이 최고일지 생각 후 풀기

# 일반 풀이
def solution(n):
    times = 0
    while n:
        times += n % 2
        n //= 2

    return times

# 베스트 풀이
def solution(n):
    return bin(n).count('1')


data = 5000
print(solution(data))


# 시간 초과 내 풀이
def solution(n):
    ans = 0
    dp = [0] * (n+1)        
    dp[1] = 1
    dp[2] = 1
    if n <= 2:
        return dp[n]

    for i in range(3, n+1):
        if i % 2 == 0:
            dp[i] = dp[i//2]
        else:
            dp[i] = dp[i-1] + 1

    return dp[n]

data = 5000
print(solution(data))