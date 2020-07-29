# define primes list
MAX_NUM = 1000
is_prime = [False, False] + [True] * (MAX_NUM-2)
primes = []
for i in range(2, MAX_NUM):
    if is_prime[i] == True:
        primes.append(i)
        for j in range(i*2, MAX_NUM, i):
            is_prime[j] = False

# 풀이 1
T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    cases = 0
    for x in primes:
        if N <= x:
            break
        for y in primes:
            if N <= y:
                break
            if y < x:
                continue
            z = N - x - y
            if is_prime[z] and x <= z and y <= z:
                cases += 1

    print(f'#{t} {cases}')

# 풀이 2 나중에 업데이트 바람