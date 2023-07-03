MOD = 1_234_567_891
SIZE = 1_000_000
fact = [1 for _ in range(SIZE+1)]
for i in range(2, SIZE+1):
    fact[i] = fact[i-1] * i % MOD

def power(N, K):
    if K == 0:
        return 1
    if K == 1:
        return N
    
    x = power(N, K//2)
    if K % 2:
        return x * x * N % MOD
    else:
        return x * x % MOD

T = int(input())
for test_case in range(1, T+1):
    N, R = map(int, input().split())
    NUMERATOR = fact[N]
    DENOMINATOR = fact[N-R] * fact[R] % MOD
    ans = NUMERATOR * power(DENOMINATOR, MOD-2) % MOD
    print(f'#{test_case} {ans}')
