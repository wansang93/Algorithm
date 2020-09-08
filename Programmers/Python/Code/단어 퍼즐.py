# 효율성 test 통과 못함
def solution(strs, t):
    dp = {}
    len_t = len(t)

    for i in range(len_t):
        dp[i] = float('inf')

    for i in range(1, len_t+1):
        # TODO: j의 범위를 수정바람
        for j in range(i):
            substring = t[j:i]
            if substring in strs:
                # TODO: 이부분도 수정 해야 함
                if j == 0:
                    dp[i-1] = 1
                    break
                if dp[j-1] != float('inf'):
                    dp[i-1] = min(dp.get(i-1), dp.get(j-1) + 1)

    return dp.get(len_t-1) if dp.get(len_t-1) != float('inf') else -1


# 뒤에서 부터 실행하면 효율성을 통과함
def solution2(strs, t):
    dp = {}
    for i in range(len(t)):
        dp[i] = float('inf')

    for i in range(len(t)-1, -1, -1):
        for k in range(1,6):
            if t[i:i+k] in strs:
                dp[i] = min(dp.get(i), dp.get(i+k, 0)+1)
    return dp.get(0) if dp.get(0) != float('inf') else -1


print(solution(['ba', 'na', 'n', 'a'], 'banana'))