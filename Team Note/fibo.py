"""\
Fibonacci
"""

# Recursive Fuction, N<=20; O(2**N)
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


# DP, N<=90; O(N)
def fibo2(n):
    if n <= 1:
        return n

    dp = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# N=10**18; Pisano Period, O(N)
# 피보나치 수를 M으로 나눈 나머지는 항상 주기를 가짐
# fibo[N] % M = fibo[N%P] % M (주기가 P)
def fibo3(n, mod=1_000_000):
    if n <= 1:
        return n

    p = pisano(mod)
    if p == -1:
        return -1
    dp = [0, 1] + [0] * (p-1)
    for i in range(2, p):
        dp[i] = (dp[i-1] + dp[i-2]) % mod

    return dp[n%p]


def pisano(num):
    """
    0 1 1 2 3 5 8 13 ...
    (f(n-2) % m + f(n-1) % m) % m = f(n) % m
    """
    if num <= 1:
        return -1

    ans = 0
    mod1, mod2 = 0, 1
    while True:
        ans += 1
        mod1, mod2 = mod2, (mod1 + mod2) % num

        if mod1 % num == 0 and mod2 % num == 1:
            break

    return ans


# N=10**18; 행렬 곱, O(logN)
# [Fn+2, Fn+1] = [[1, 1], [1, 0]] * [Fn+1, Fn]
# [[Fn+1, Fn], [Fn, Fn-1]] = [[1, 1], [1, 0]] ** n
# n번째 피보나치 수: 행렬 (1 1, 1 0)^n 의 1행 2열 값(단, n>=1 일 때)
def fibo4(n, mod=1_000_000_007):
    if n <= 1:
        return n
    
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]
    while True:
        if n <= 0:
            break
        if n % 2 == 1:
            ans = multifly_matrix(ans, a, mod)
        a = multifly_matrix(a, a, mod)
        n //= 2
    
    return ans[0][1]


def multifly_matrix(lst1, lst2, mod=1):
    ans = []
    for i in range(0, len(lst1)):
        temp = []
        for j in range(0, len(lst2[0])):
            s = 0
            for k in range(0, len(lst1[0])):
                s += lst1[i][k] * lst2[k][j]
            temp.append(s % mod)
        ans.append(temp)

    return ans


K = 20
print("재귀로 풀기")
for n in range(K):
    print(fibo(n), end=" ")
print()
print("DP로 풀기")
for n in range(K):
    print(fibo2(n), end=" ")
print()
print("행렬 곱으로 풀기")
for n in range(K):
    print(fibo4(n), end=" ")
print()
print("피사노 주기로 풀기")
for n in range(K):
    print(fibo3(n), end=" ")
print()
