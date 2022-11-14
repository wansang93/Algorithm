# Fibonacci

$F_{n} = F_{n-1} + F_{n-2}$

결론 fibo(N)은 logN의 시간복잡도로 구할 수 있다.

## Fibonacci 수 구하기

```python
def fibo(n):
    if n <= 1:
        return n

    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]
    while n:
        if n % 2 == 1:
            ans = multiply_matrix(ans, a)
        a = multiply_matrix(a, a)
        n //= 2
    
    return ans[1][0]


def multiply_matrix(lst1, lst2):
    global MOD
    R, S, C = len(lst1), len(lst2), len(lst2[0])
    res = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(S):
                res[i][j] += lst1[i][k] * lst2[k][j] % MOD
            res[i][j] %= MOD
    
    return res

T = int(input())
MOD = int(10**9)
for tc in range(1, T+1):
    print(f"{tc} {fibo(tc)}")

```

### 1. Recursive Function

```python
# Recursive Function, N<=20; O(2**N)
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

```

### 2. DP(Memoization)

```python
# DP, N<=90; O(N)
def fibo2(n):
    if n <= 1:
        return n

    dp = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

```

### 3. Pisano Period

```python
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
    pisano 주기 구하는 함수
    """
    # pisano 주기는 mod 0, mod 1이 들어갈 수 없다.
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

```

### 4. Matrix products

$$
\begin{pmatrix} F_{n+1}&F_n\\\\F_n&F_{n-1} \end{pmatrix} = \begin{pmatrix} 1&1\\\\1&0 \end{pmatrix} ^ n
$$

```python
# N=10**18; 행렬 곱, O(logN)
# [Fn+2, Fn+1] = [[1, 1], [1, 0]] * [Fn+1, Fn]
# [[Fn+1, Fn], [Fn, Fn-1]] = [[1, 1], [1, 0]] ** n
# n번째 피보나치 수: 행렬 (1 1, 1 0)^n 의 1행 2열 값(단, n>=1 일 때)
def fibo4(n, mod=1_000_000_007):
    if n <= 1:
        return n

    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]
    while n:
        if n % 2 == 1:
            ans = multiply_matrix(ans, a, mod)
        a = multiply_matrix(a, a, mod)
        n //= 2
    
    return ans[0][1]


def multiply_matrix(lst1, lst2, mod):
    R, C, S = len(lst1), len(lst2[0]), len(lst2)
    ans = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(S):
                ans[i][j] += lst1[i][k] * lst2[k][j] % mod
            ans[i][j] %= mod
    
    return ans

```

```python
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
```

## Fibonacci Recurrence Relations

$F_{2n-1} = F_n^2 + F_{n-1}^2$

$F_{2n} = (F_{n-1} + F_{n+1})F_n = (2F_{n-1} + F_n)F_n$

$\sum_{i=1}^{n}{F_i} = F_{n+2} - 1$

$\sum_{i=1}^{n}{F_{2i}} = F_{2n+1} - 1$

$\sum_{i=0}^{n}{F_{2i+1}} = F_{2n}$

$\sum_{i=1}^{n}{F_i^2} = F_nF_{n+1}$

$gcd(F_n,F_m) = F_{gcd(n,m)}$
