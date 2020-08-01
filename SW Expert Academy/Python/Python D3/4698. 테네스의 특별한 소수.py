MAX_NUMBER = 1000000
is_prime = [False, False] + [True] * (MAX_NUMBER - 1)
primes = []
for i in range(2, MAX_NUMBER+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i+i, MAX_NUMBER+1, i):
            is_prime[j] = False

T = int(input())
for t in range(1, T+1):
    D, A, B = map(int, input().split())
    D = str(D)
    answer = 0
    for prime in primes:
        if prime < A:
            continue
        elif B < prime:
            break
        else:
            if D in str(prime):
                answer += 1

    print(f'#{t} {answer}')
