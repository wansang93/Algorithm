# Python Competitive Programming Team Notes

- This repository is a python library for PS(Problem-Solving) Competition.
- When you need an implementation of a specific algorithm, please let me know.
- 알고리즘 대회를 위한 **파이썬 (Python) 소스코드 저장소**입니다.
- **동빈나** 님의 사이트를 참고해서 만들었습니다. -> [동빈나님 Team Notes](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/README.md)
- 이 문서는 누구나 자유롭게 수정, 복제가 가능합니다.

# Contents

# 잡기술(Technical skills)

## 단어 중복 체크, 연속된 단어는 허용

백준 1316번 그룹 단어 체커

```python
cnt += list(word) == sorted(word, key=word.find)
```

내 코드

```python
temp = []
now_chr = ' '
for c in s:
    if now_chr != c:
        if c in temp:
            break
        temp.append(c)
        now_chr = c
else:
    cnt += 1
```

## 특정 문자를 지정 문자로 바꿔서 처리하면 편함

백준 2941번 크로아티아 알파벳

```python
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cr in croatian:
    s = s.replace(cr, '!')
```

## 알파벳 찾기, find와 index의 차이 익히기

백준 10809번 알파벳 찾기

```python
# A~Z까지 다 찾기
lst = list(range(ord('a'), ord('z')+1))
for i in lst:
    print(S.find(chr(i)), end=' ')
```

```python
# 단어를 찾아 index 바꾸기
lst = [-1] * 26
for i, v in enumerate(S):
    if lst[ord(v) - ord('a')] == -1:
        lst[ord(v) - ord('a')] = i

for i in lst:
    print(i, end=' ')
```

# 수론(Number Theory)

## 최대 공약수(GCD(Greatest Common Divisor))
## 최소 공배수(LCM(Least Common Multiple))
## 모든 약수 찾기(Find All Divisors)

```python
def find_all_divisors_of_a_number(x):
    result = []
    for i in range(1, int(x**1/2) + 1):
        if x % i == 0:
            result.append(i)
            if i * i != x:
                result.append(x // i)
    return result

print(find_all_divisors_of_a_number(12)) # [1, 12, 2, 6, 3, 4]
```

## 소수(Check Prime Number)

```python
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(7))  # True
```

## 가장 큰 소인수(Largest Prime Factor)

## 소인수분해(Prime Factorization)

non-function

```python
n = 9991
i = 2
factors = []
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        factors.append(i)
if n > 1:
    factors.append(n)

print(factors)  # [97, 103]
```

function

```python
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(9991))  # [97, 103]
```

동빈나 코드

```python
def prime_factorization(x):
    result = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            count = 0
            while x % i == 0:
                count += 1
                x //= i
            result.append((i, count))
    if x > 1:
        result.append((x, 1))
    return result

# Note: 1 is neither a prime number (소수) nor a composite number (합성수).
print(prime_factorization(75)) # [(3, 1), (5, 2)]  # 3이 1번, 5가 2번
```

## 에라토스테네스의 체(Sieve of Eratosthenes)

non-function(from 0 to n)

```python
num = 53
sieve = [False, False] + [True] * (num-1)
ns = int(num ** 0.5)
for i in range(2, ns + 1):
    if sieve[i]:
        for j in range(i+i, num+1, i):
            sieve[j] = False

print([i for i in range(num+1) if sieve[i]])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
```

function(from 0 to n)

``` python
def prime_list(n):
    sieve = [False, False] + [True] * (n-1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i]]

print(prime_list(53))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
```

function(from 2 to less than n)

```python
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]

print(prime_list(53))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

# 탐색(Sorting)

## 버블 정렬(Bobble Sort)
## 선택 정렬(Selection Sort)
## 삽입 정렬(Insertion Sort)
## 병합 정렬(Merge Sort)
## 힙 정렬(Heap Sort)
## 퀵 정렬(Quick Sort)
## 계수 정렬(Counting Sort)
## 파이썬 정렬 라이브러리(Python Sort Library)

```python
n = 5

''' Python Sort Library (Basic) '''
data = [8, 5, 4, 7, 2]
data.sort()

for x in data:
    print(x, end=' ')

''' Python Sort Library (Based on a key) '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: x[0]) # Stable Sort (When using a key)

for x in data:
    print(x, end=' ')

''' Python Sort Library '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort() # Non-stable Sort (When not using a key)

for x in data:
    print(x, end=' ')
```

# Searching

## 이진 탐색(Binary Search)
## 파이썬 탐색 라이브러리(Python Binary Search Library)
### [Count the number of frequencies of elements whose value is between \[left, right\] in a sorted array]
## DFS
## BFS
## [DFS & BFS Examples 1]

# Graph

- [Dijkstra Shortest Path]
- [Minimum Spanning Tree (MST)]
- [Topology Sort]
- Floyd–Warshall algorithm
- Bipartite Matching

# Data Structure

- [Disjoint-Set (Union-Find)]
- Tree
- Line
- Plane

# String

- Rabin-Karp
- KMP
- Trie

# Dynamic Programming

- Tiling Problem
- 0-1 Knapsack Problem
- LIS (Longest Increasing Subsequence)
- LCS (Longest Common Subsequence)
- Matrix Chain Multiplication

# Geometry

- [Number of intersection points of two lines in 1 dimension]
- CCW
- Convex Hull
- Polygon

# Probability Theory

```python
mylist = ['1', '2', 'b', 'a']

from itertools import permutations  # 순열
from itertools import combinations  # 조합
from itertools import product  # 중복순열
from itertools import combinations_with_replacement  # 중복조합

print(list(permutations(mylist, 2)))
print(list(combinations(mylist, 2)))
print(list(product(mylist, repeat=2)))
print(list(combinations_with_replacement(mylist, 2)))
```

## 순열(Permutation)
## 조합(Combination)

# Signal Processing

- FFT

# Miscellaneous

- Two Pointers
    - [Number of intervals whose sum is M]
- Interval Sum
    - [Prefix Sum]
    - [Fenwick Tree (Binary Indexed Tree)]
- [Matrix Rotation]
- Handling Recursion Limit