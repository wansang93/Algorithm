# 풀이1
def primes(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return num

import itertools

def solution(numbers):
    answer = 0
    mylist = []
    for i in range(1, len(numbers)+1):
        mylist.extend(list(map(''.join, itertools.permutations(numbers, i))))
    
    mylist = list(set(map(int, mylist)))
    largest = max(mylist)

    primes_list = primes(largest)
    for i in mylist:
        if i in primes_list:
            answer += 1
    return answer


print(solution('011'))

# 풀이2
from itertools import permutations
def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map(''.join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
