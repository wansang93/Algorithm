N = 1000000

# 0 ~ 1,000,000 까지의 소수 체크
prime_check = [False, False] + [True] * (N-1)
prime_numbers = []

for i in range(2, N+1):
    if prime_check[i]:
        prime_numbers.append(i)
        for j in range(i, N+1, i):
            prime_check[j] = False

for i in prime_numbers:
    print(f'{i}', end=' ')