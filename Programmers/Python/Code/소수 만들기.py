from itertools import combinations


def solution(nums):
    # Seive of Eratosthenes
    max = 3000
    sieve = [False, False] + [True] * (max-1)
    ns = int(max ** 0.5)
    for i in range(2, ns + 1):
        if sieve[i]:
            for j in range(i+i, max+1, i):
                sieve[j] = False

    answer = 0
    for i in combinations(nums, 3):
        number = sum(i)
        if sieve[number]:
            answer += 1

    return answer

data = [1,2,3,4]
print(solution(data))
