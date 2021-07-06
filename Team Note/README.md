# Python Competitive Programming Team Notes

- This repository is a python library for PS(Problem-Solving) Competition.
- When you need an implementation of a specific algorithm, please let me know.
- 알고리즘 대회를 위한 **파이썬 (Python) 소스코드 저장소**입니다.
- **동빈나** 님의 사이트를 참고해서 만들었습니다. -> [동빈나님 Team Notes](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/README.md)
- 이 문서는 누구나 자유롭게 수정, 복제가 가능합니다.

# Contents

[수론](#수론number-theory), [정렬](#정렬sorting), [탐색](#탐색searching), [그래프](#그래프graph), [자료구조](#자료구조data-structure), [문자열](#문자열string), [동적 프로그래밍(DP)](#동적-프로그래밍dynamic-programming), [기하](#기하geometry), [통계](), [확률이론](#확률이론probability-theory), [신호 처리](#신호-처리signal-processing), [잡기술](#잡기술miscellaneous)

# 수론(Number Theory)

목차: 최대 공약수, 최소 공배수, 모든 약수 찾기, 소수, 가장 큰 소인수, 소인수분해, 에라토스테네스의 체

## 최대 공약수(GCD(Greatest Common Divisor))

gcd 모듈 없는 버전

```python
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(gcd(1071, 1029))  # 21
```

```python
from math import gcd
print(gcd(1071, 1029))
```

## 최소 공배수(LCM(Least Common Multiple))

```python
from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(1071, 1029))  # 52479
```

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

```python
def max_prime_factor(n):
   # number must be even
   while n % 2 == 0:
      max_prime = 2
      n /= 1
   # number must be odd
   for i in range(3, int(n**(1/2)) + 1, 2):
      while n % i == 0:
         max_prime = i
         n = n / i
   # prime number greator than two
   if n > 2:
      max_prime = n
   return int(max_prime)
# Driver code to test above function
n = 15
print(max_prime_factor(n))
```

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

# 정렬(Sorting)

목차: 버블, 선택, 삽입, 퀵, 병합, 힙, 계수, 정렬 라이브러리

## 버블 정렬(Bobble Sort)

```python
# Bubble Sort
N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(N):
    print(lst[i])
```

## 선택 정렬(Selection Sort)

```python
# Selection Sort
N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = int(input())

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if lst[j] < lst[min_idx]:
            min_idx = j
    if min_idx != i:
        lst[min_idx], lst[i] = lst[i], lst[min_idx]

for i in range(N):
    print(lst[i])
```

## 삽입 정렬(Insertion Sort)

```python
# Insertion Sort
N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = int(input())

for i in range(1, N):
    # # 1. For loop
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
        else:
            break

    # # 2. While loop
    # key = lst[i]
    # j = i-1
    # while j >=0 and key < lst[j]:
    #         lst[j+1] = lst[j]
    #         j -= 1
    # lst[j+1] = key

for i in range(N):
    print(lst[i])
```

## 퀵 정렬(Quick Sort)

간단한 방식

```python
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))
```

알고리즘 기반 로직

```python
def partition(lst, start, end):
    pivot = lst[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and pivot <= lst[right]:
            right -= 1
        if right < left:
            done = True
        else:
            lst[left], lst[right] = lst[right], lst[left]
    lst[start], lst[right] = lst[right], lst[start]
    return right


def quick_sort(lst, start, end):
    if start < end:
        pivot = partition(lst, start, end)
        quick_sort(lst, start, pivot - 1)
        quick_sort(lst, pivot + 1, end)
    return lst


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array, 0, len(array)-1))
```

## 병합 정렬(Merge Sort)

```python

```

## 힙 정렬(Heap Sort)

```python

```

## 계수 정렬(Counting Sort)

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

# 출력1
print(count)  # [2, 2, 2, 1, 1, 2, 1, 1, 1, 2]
# 출력2
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

## 파이썬 정렬 라이브러리(Python Sort Library)

```python
n = 5

''' Python Sort Library (Basic) '''
data = [8, 5, 4, 7, 2]
data.sort()

for x in data:
    print(x, end=' ')
# 2 4 5 7 8

''' Python Sort Library (Based on a key) '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort(key=lambda x: x[0]) # Stable Sort (When using a key)

for x in data:
    print(x, end=' ')
# (20, 'Kim') (20, 'Ahn') (23, 'Seo') (25, 'Na') (28, 'Park')

''' Python Sort Library '''
data = [(25, 'Na'), (20, 'Kim'), (23, 'Seo'), (28, 'Park'), (20, 'Ahn')]
data.sort() # Non-stable Sort (When not using a key)

for x in data:
    print(x, end=' ')
# (20, 'Ahn') (20, 'Kim') (23, 'Seo') (25, 'Na') (28, 'Park')
```

# 탐색(Searching)

목차: 이진 탐색, 탐색 라이브러리, DFS, BFS

## 이진 탐색(Binary Search)

재귀 호출 방법

```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid+1, end)
```

반복문 방법

```python
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
```

```python
# 데이터 예시
n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n-1)
result = binary_search2(array, target, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)  # 3
```

## 파이썬 탐색 라이브러리(Python Binary Search Library)

### Count the number of frequencies of elements whose value is between \[left, right\] in a sorted array

```python
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = 7, 2
array = [1, 1, 2, 2, 2, 2, 3]

count = count_by_range(array, x, x)
if count == 0:
    print(-1)
else:
    print(count)  # 4
```

## DFS

```python
''' Depth First Search (DFS) '''
def dfs(x):
    # print(x, end=' ')
    visited[x] = True
    for y in graph[x]:
        if not(visited[y]):
            dfs(y)
```

## BFS

```python
from collections import deque

''' Breadth First Search (BFS) '''
def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        x = q.popleft()
        # print(x, end=' ')
        for y in graph[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = True
```

## DFS & BFS Examples 1

```python
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(start)
print()
visited = [False] * (n + 1)
bfs(start)

'''
[Input Example 1]
4 5 1
1 2
1 3
1 4
2 4
3 4
[Output Example 1]
1 2 4 3 
1 2 3 4

graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
dfs 경로 -> 1 2 4 3
bfs 경로 -> 1 2 3 4
'''
```

# 그래프(Graph)

목차: 다익스트라, 최소 신장 트리, 위상 정렬, 플로이드 와샬 알고리즘, 이분 매칭

## 다익스트라(Dijkstra Shortest Path)

```python

```

## 최소 신장 트리(Minimum Spanning Tree (MST))

```python

```

## 위상 정렬(Topology Sort)

```python

```

## 플로이드 와샬 알고리즘(Floyd–Warshall algorithm)

```python

```

## 이분 매칭(Bipartite Matching)

```python

```

# 자료구조(Data Structure)

## 서로소 집합(Disjoint-Set (Union-Find))

```python

```

## 트리(Tree)

```python

```

## Line
## Plane

# 문자열(String)

목차: Rabin-Karp, KMP, Trie

## Rabin-Karp

```python

```

## KMP

```python

```

## Trie

```python

```

# 동적 프로그래밍(Dynamic Programming)

## Tiling Problem

```python

```

## 0-1 Knapsack Problem

```python

```

## LIS(Longest Increasing Subsequence)

```python

```

## LCS(Longest Common Subsequence)

```python

```

## Matrix Chain Multiplication

```python

```

# 기하(Geometry)

## Number of intersection points of two lines in 1 dimension

```python

```

## CCW

```python

```

## Convex Hull

```python

```

## Polygon

```python

```

# 통계(Statistics)

목차: 최빈값

## 최빈값

Collection Counter 모듈 없는 버전

```python
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_mode(dic):
    most = max(dic.values())
    most_keys = [k for k, v in dic.items() if v == most]
    # 추가할 사항 넣기
    return most_keys

lst = [1, 1, 2, 3, 4, 5, 5]
print(get_mode(get_counts(lst)))  # [1, 5]
```

```python
from collections import Counter

lst = [1, 1, 2, 3, 4, 5, 5]
mode_dict = Counter(lst).most_common()
print(mode_dict)  # [(1, 2), (5, 2), (2, 1), (3, 1), (4, 1)]
```

# 확률이론(Probability Theory)

## 순열, 조합, 중복순열, 중복조합 라이브러리들

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

```python

```

## 조합(Combination)

```python

```

# 신호 처리(Signal Processing)

## 고속 푸리에 변환(FFT(Fast Fourier Transform))

```python

```

# 잡기술(Miscellaneous)

## 투 포인터(Two Pointers)

### Number of intervals whose sum is M

구간 합이 M인 갯수

```python
def two_pointer(lst, m):
    n = len(lst)
    count = 0
    end = 0
    interval_sum = 0

    # move 'start' pointer to the right.
    for start in range(n):
        # move 'end' pointer to the right.
        while interval_sum < m and end < n:
            interval_sum += lst[end]
            end += 1
        # If the sum of interval is 'm', count the number.
        if interval_sum == m:
            count += 1
        interval_sum -= lst[start]

    return count

print(two_pointer([1, 2, 3, 2, 5], 5))  # 3
```

## 구간 합(Interval Sum)

### Prefix Sum

```python
def interval_sum(lst, query):
    p = [0] * (len(lst) + 1)
    result = [0] * len(query)

    for i, v in enumerate(lst):
        p[i+1] = p[i] + v
    # print(p)  # [0, 10, 30, 60, 100, 150]

    for i, v in enumerate(query):
        result[i] = p[v[1]] - p[v[0]-1]

    return result

print(interval_sum([10, 20, 30, 40, 50], [(3, 4), (2, 3), (1, 4)]))
# [70, 50, 100]
```

### Fenwick Tree(Binary Indexed Tree)

```python

```

## 회전 행렬(Rotation Matrix)


```python
def rotate(m, d):
    """
    input
    m: 회전하고자 하는 2차원 배열. 입력이 정방형 행렬이라고 가정
    d: 90도씩의 회전 단위. -1: -90도, 1: 90도, 2: 180도, ...
    """
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret

# 출처: https://deepwelloper.tistory.com/117 [DEVLOG]
```

## 재귀 제한하기(Handling Recursion Limit)

```python

```

## 행렬 뒤집기

```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))

'''
print(mylist)
print(new_list)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''
```

## 실전에서 느낀 것(What I felt in practice)

## 딕셔너리 빠르게 선언하기(.get 활용)

```python

test_dict = {}
keys = [0, 1, 2, 3]
values = ['10', '20', '30', '40']
# .get 활용
for key, value in zip(keys, values):
    #.get(key값, 기본 타입) + 기본 타입에 추가할 값
    test_dict[key] = test_dict.get(key, 0) + int(value)

# 기존
for key, value in zip(keys, values):
    #.get(key값, 기본 타입) + 기본 타입에 추가할 값
    if key not in test_dict:
        test_dict[key] = key
    else:
        test_dict[key] += key
```

### 1의자리 숫자를 N개만큼의 수 만들기(int형만 사용해서)

```python
n = 1
cnt = 8

for i in range(n, 9):
    s = (i * 10**cnt) // 9
    print(s)
print(10 ** cnt - 1)

# 11111111
# 22222222
# 33333333
# 44444444
# 55555555
# 66666666
# 77777777
# 88888888
# 99999999
```

### 문자열 자리수마다 끊기

```python
# SPLIT STRING INTO N-SIZE
string='12312312312312'
length=3
[string[i:i+length] for i in range(0, len(string), length)]

# result
# ['123', '123', '123', '123', '12']
```

### 정렬 2번째 요소도 고려

백준 11650번 좌표 정렬하기

```python
lst.sort(key=lambda x: (x[0], x[1]))
```

### 정렬 문자로 된 숫자

백준 1427번 소트 인사이드

[sorted docs](https://docs.python.org/3/howto/sorting.html)

```python
sorted(N)[::-1]  # sorted는 아스키 기준으로 정렬하는거 같음
```

### 단어 중복 체크, 연속된 단어는 허용

백준 1316번 그룹 단어 체커

짧은 코드

```python
cnt += list(word) == sorted(word, key=word.find)
```

긴 코드

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

### 특정 문자를 지정 문자로 바꿔서 처리하면 편함

백준 2941번 크로아티아 알파벳

```python
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cr in croatian:
    s = s.replace(cr, '!')
```

### 알파벳 찾기, find와 index의 차이 익히기

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
