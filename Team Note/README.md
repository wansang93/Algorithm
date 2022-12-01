# Python Competitive Programming Team Note

- This repository is a python library for PS(Problem-Solving) Competition.
- When you need an implementation of a specific algorithm, please let me know.
- 알고리즘 대회를 위한 **파이썬 (Python) 소스코드 저장소**입니다.
- **동빈나** 님의 사이트를 참고해서 만들었습니다. -> [동빈나님 Team Notes](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/README.md)
- 이 문서는 누구나 자유롭게 수정, 복제가 가능합니다.

## Contents

[기본](#파이썬-기본-문법), [자료구조](#자료구조data-structure), [수론](#수론number-theory), [정렬](#정렬sorting), [탐색](#탐색searching), [그래프](#그래프graph), [문자열](#문자열string), [동적 프로그래밍(DP)](#동적-프로그래밍dynamic-programming), [기하](#기하geometry), [통계](#통계statistics), [확률이론](#확률이론probability-theory), [신호 처리](#신호-처리signal-processing), [잡기술](#잡기술miscellaneous)

# 파이썬 기본 문법

## Row * Col 의 리스트 초기화

```python
row, col = 3, 5
mylist = [[0] * col for _ in range(row)]
```

## 그래프 빠르게 그리기

```python
import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] * V for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))


INF = int(1e9)
distance = [INF] * (V+1)
distance[K] = 0
heap = []
```

## 리스트 평평하게 하기(List flatten)

```python
lst = [[1, 2, 3], [4, 5, 6]]

# 방법 1
flatten_lst = [i for s in lst for i in s]

# 방법 2(itertools 활용)
import itertools
flatten_lst = list(itertools.chain(*lst))

# 방법 3(함수형)
def flatten(t):
    return [item for sublist in t for item in sublist]
flatten_lst = flatten(lst)

print(lst)  # [[1, 2, 3], [4, 5, 6]]
print(flatten_lst)  # [1, 2, 3, 4, 5, 6]
```

## 전치행렬(Transpose 2d list)

```python
# 열탐색 할 때 좋음
lst = list(map(list, zip(*l)))
lst = [list(x) for x in zip(*lst)]
```

## 딕셔너리 빠르게 선언하기(.get 활용)

```python
test_dict = {}
test_dict2 = {}
keys = [0, 1, 2, 3, 3]
values = ['10', '20', '30', '40', '40']
# .get 활용
for key, value in zip(keys, values):
    #.get(key값, 기본 타입) + 기본 타입에 추가할 값
    test_dict[key] = test_dict.get(key, 0) + int(value)
    test_dict2[key] = test_dict2.get(key, []) + [int(value)]

print(test_dict)  # {0: 10, 1: 20, 2: 30, 3: 80}
print(test_dict2)  # {0: [10], 1: [20], 2: [30], 3: [40, 40]}

# 기존
for key, value in zip(keys, values):
    if key not in test_dict:
        test_dict[key] = key
    else:
        test_dict[key] += key
```

## 파이썬 정렬 라이브러리(Python Sort Library)

```python
# 딕셔너리 정렬
dicts = {}
new_dict = sorted(dicts.items(), key=lambda x: x[0]))  # key로 정렬
new_dict = sorted(dicts.items(), key=lambda x: x[1]))  # value로 정렬
# value[1], value[0] 순으로 정렬
new_dict = sorted(dicts.items(), key=lambda x: (x[1][1], x[1][0]))

''' Python Sort Library (Basic) '''
n = 5
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

## 라이브러리들

```python
import itertools  # 순열과 조합
import heapq  # 힙 자료구조
import bisect  # 이진 탐색
import collections  # 덱, 카운터
import math  # 수학

# 1. 표준 라이브러리
eval('(3+5)*7')  # 56

# 2. Count
from collections import Counter
counter = Counter(['a', 'a', 'b', 'b', 'a', 'c', 'd', 'c'])
print(counter['a'])  # 3
print(dict(counter))  # {'a': 3, 'b': 2, 'c': 2, 'd': 1}
```

# 자료구조(Data Structure)

## [List, Set, Dictionary] Time Complexity -> <https://wiki.python.org/moin/TimeComplexity>

## 서로소 집합(Disjoint-Set (Union-Find))

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모를 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# # 입력 받은 두 원소를 유니온 하기
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# 사이클을 판별하면서 union 연산 수행
cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
    union_parent(parent, a, b)

print(cycle)
# 각 원소 집합 출력하기
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력하기
for i in range(1, v+1):
    print(f'{i} -> {parent[i]}')

```

동빈나 코드

```python
# Find the root node of x recursively.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union the two sets.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# Process union operations.
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('Root nodes for all nodes: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('Parent Table: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
[Input Example 1]
6 4
1 4
2 3
2 4
5 6
[Output Example 1]
Root nodes for all nodes: 1 1 1 1 5 5 
Parent Table: 1 1 1 1 5 5
'''
```

# 수론(Number Theory)

목차: N진법 변환, 최대 공약수, 최소 공배수, 모든 약수 찾기, 소수, 가장 큰 소인수, 소인수분해, 에라토스테네스의 체, 나머지 분배법칙, 피보나치 수

## N(2~16)진법 변환(Convert an integer to a string in any base)

```python
# 방법 1: while문
num, base = map(int, input().split())
answer = []
dic = list('0123456789ABCDEF')

if num == 0:
    answer.append('0')
while num:
    answer.append(dic[num % base])
    num //= base

print(''.join(answer)[::-1])

# 방법 2: Recursion
# WARNING: maximum recursion depth
def baseN(num, b, numerals="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return ((num == 0) and numerals[0]) or \
        (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

# 2, 8, 16진수는 빠르게 변환 가능
n = 100
bin(n)[2:]; f"{n:b}" # bin: 1100100
oct(n)[2:]; f"{n:x}" # hex: 64
hex(n)[2:]; f"{n:o}" # oct: 144

# 문자열 N진법을 int로 바꾸는 법
# str_num은 0~9, A~Z까지 base는 2 ~ 36까지 가능
str_num, b = "2Z", 36
a = int(str_num, b)
print(a)  # 107(72+35)
```

## 최대 공약수(GCD(Greatest Common Divisor))

```python
from math import gcd
print(gcd(1071, 1029))  # 21
```

```python
# gcd 모듈 없는 버전
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(gcd(1071, 1029))  # 21
```

## 최소 공배수(LCM(Least Common Multiple))

```python
from math import lcm
print(lcm(1071, 1029))  # 52479
```

```python
# lcm 모듈 없는 버전
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(1071, 1029))  # 52479
```

## 모든 약수 찾기(Find All Divisors)

```python
def find_all_divisors_of_a_number(x):
    result = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            result |= {i, x // i}

    return list(sorted(result))

print(find_all_divisors_of_a_number(12))
# [1, 2, 3, 4, 6, 12]
```

## 소수(Check Prime Number)

```python
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime(7))
# True
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
# 5
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

print(factors)
# [97, 103]
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

n = 9991
print(prime_factors(n))
# [97, 103]
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

print(prime_factorization(75))
# [(3, 1), (5, 2)]  # 3이 1번, 5가 2번
# Note: 1 is neither a prime number (소수) nor a composite number (합성수).
```

## 에라토스테네스의 체(Sieve of Eratosthenes)

```python
# non-function(from 0 to n)
N = 53
sieve = [False, False] + [True] * (N-1)
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        for j in range(i+i, N+1, i):
            sieve[j] = False

print([i for i in range(N+1) if sieve[i]])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
```

``` python
# function(from 0 to n)
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

## 나머지 분배법칙

```python
# 큰 두 수
x = 11e20
y = 11e20
m = 20

# plus, minus, multifly
print((x + y) % m == (x % m) + (y % m))
print((x - y) % m == ((x % m) - (y % m) + m) % m)
print((x * y) % m == ((x % m) * (y % m)) % m)
```

## [팩토리얼(Factorial)과 이항 계수(Binomial Coefficient)](./facto.md)

## [피보나치 수(Fibonacci)](./fibo.md)

# 정렬(Sorting)

목차: 버블, 선택, 삽입, 퀵, 병합, 힙, 계수 정렬

> 좋은 강의: [Sorting Algorithms Visualizations](https://www.youtube.com/playlist?list=PL2aHrV9pFqNS79ZKnGLw-RG5gH01bcjRZ)

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

메모리 복제 방식(메모리 효율 저하)

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```

메모리 효율 최적화(인덱스 탐색)

```python
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
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

## 빈도 정렬(Frequency Sort)

```python
lst = [11, 33, 11, 77, 54, 11, 25, 25, 33]
st = sorted(lst, key=lambda x: (-lst.count(x), lst.index(x)))

print(*st)  # 11 11 11 33 33 25 25 77 54
```

# 탐색(Searching)

목차: 이진 탐색, 탐색 라이브러리, DFS, BFS, 분할정복을 이용한 거듭제곱

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

## 분할정복을 이용한 거듭제곱(Power with divide and conquer)

```python
# A ** B % C
pow(2, 3, 5)  # 3  
```

Time complex: log(N)

Use recursive function

```python
def fpow(base, exponent, divide=1):
    if exponent == 1:
        return base % divide
    else:
        x = fpow(base, exponent//2, divide)
        if exponent % 2 == 0:
            return x * x % divide
        else:
            return x * x * base % divide
```

Use while loop

```python
def fpow(base, exponent):
    res = 1
    while exponent:
        # if exponent is odd, Do
        if exponent & 1:
            res *= base
        base *= base
        # same as exponent = exponent//2
        exponent >>= 1

    return res
```

## 파이썬 탐색 라이브러리(Python Binary Search Library)

### Count the number of frequencies of elements whose value is between [left, right] in a sorted array

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

Without Recursion

```python
def dfs(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph[node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited

print (dfs(graph1, 'A'))
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

# dfs 풀이
visited = [False] * (n + 1)
dfs(start)

print()

# bfs 풀이
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

BEAKJOON Code Example(함수형)

```python
import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

for __ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

for e in edge:
    e.sort(reverse=True)

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
    return d_visit


def bfs():
    b_visit = []
    queue = [V]
    b_check = [0 for _ in range(N+1)]
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue
    return b_visit

print(*dfs())
print(*bfs())
```

# 그래프(Graph)

목차: 다익스트라, 최소 신장 트리, 위상 정렬, 플로이드 와샬 알고리즘, 이분 매칭

## 다익스트라(Dijkstra Shortest Path)

```python
import heapq

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_d, now = heapq.heappop(q)
        if distance[now] < now_d:
            continue
        for next_v, next_d in graph[now]:
            cost = now_d + next_d
            if cost < distance[next_v]:
                distance[next_v] = cost
                heapq.heappush(q, (cost, next_v))

INF = int(1e9)  # 10억

# n: 노드의 갯수
# m: 간선의 갯수
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


dijkstra(start)
print(graph)  # [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
print(distance)  # [1000000000, 0, 2, 3, 7, 1000000000]
'''
[Input Example 1]
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
```

## 최소 신장 트리(Minimum Spanning Tree (MST))

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

# 부모를 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력 받기
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않은 경우만
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

```

## 위상 정렬(Topology Sort)

입력값 입력받기

```python
N, M = map(int, input().split())
indegree_lst = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree_lst[B] += 1
''' Input:
4 2
4 2
3 1
'''
```

queue(큐)를 이용한 위상 정렬

```python
from collections import deque

def topology_sort():
    result = []
    q = deque()
    for i in range(1, N+1):
        if indegree_lst[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree_lst[i] -= 1
            if indegree_lst[i] == 0:
                q.append(i)
    
    return result

print(topology_sort())
# [3, 4, 1, 2]
```

priority queue(우선순위 큐)를 이용한 위상 정렬

```python
import heapq
def topology_sort():
    result = []
    heap = []
    for i in range(1, N+1):
        if indegree_lst[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        now = heapq.heappop(heap)
        result.append(now)
        for i in graph[now]:
            indegree_lst[i] -= 1
            if indegree_lst[i] == 0:
                heapq.heappush(heap, i)
    
    return result

print(topology_sort())
# [3, 1, 4, 2]
```

동빈나 코드

```python
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

''' Topology Sort '''
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
[Input Example 1]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
[Output Example 1]
1 2 5 3 6 4 7
'''
```

## 플로이드 와샬 알고리즘(Floyd–Warshall algorithm)

```python
# 노드(Vertex), 간선(Edge) 수 입력
V = int(input())
E = int(input())

# 무한 설정하기
INF = int(1e9)

# 그래프 선언 후 초기화
graph = [[INF] * (V+1) for _ in range(V+1)]
for row in range(1, V+1):
    for col in range(1, V+1):
        if row == col:
            graph[row][col] = 0

for _ in range(E):
    start, end, distance = map(int, input().split())
    graph[start][end] = min(distance, graph[start][end])

for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, V+1):
    for b in range(1, V+1):
        distance = 0
        if graph[a][b] == INF:
            distance = INF
        else:
            distance = graph[a][b]
        print(f'{a} 에서 {b} 까지 거리는 {distance} 입니다.')
    print('---')

'''
[Input Example 1]
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
[Output Example 1]
...
1 에서 3 까지 거리는 8 입니다.
1 에서 4 까지 거리는 6 입니다.
---
2 에서 1 까지 거리는 3 입니다.
2 에서 2 까지 거리는 0 입니다.
...
'''
```

## 이분 매칭(Bipartite Matching)

```python

```

# 문자열(String)

목차: Manacher Algorithm, Rabin-Karp, KMP, Trie

## Manacher Algorithm

Find the longest palindromic substring in the given string

```python
import sys
input = sys.stdin.readline

def manacher(s):
    string = '#' + '#'.join(s)+'#'
    l = len(string)
    a = [0] * l 
    c = 0 
    r = 0 

    for n in range(l):
        if r < n:
            a[n] = 0
        else:
            a[n] = min(a[2 * c - n], r - n)

        while n-a[n]-1 >= 0 and n+a[n]+1 < l and \
            string[n-a[n]-1] == string[n+a[n]+1]:
            a[n] = a[n] + 1

        if r < n + a[n]:
            r = n + a[n]
            c = n

    return max(a)

s = input()
print(manacher(s))

```

## Rabin-Karp

```python

```

## KMP

```python
def kmp(text, pattern):
    N = len(text)
    M = len(pattern)

    # 실패 함수 테이블 만들기
    table = [0] * M
    j = 0
    for i in range(1, M):
        # i와 j가 일치하지 않으면 j를 바로 뒤의 값으로 변경
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        # i와 j가 일치하면 i, j 모두 1씩 이동하게 됨
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    # print(table)
    
    count = 0  # 맞은 갯수
    loc = []  # 시작 인덱스 저장 위치
    j = 0
    for i in range(N):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            # 전체가 매칭 되면
            if j == (M - 1):
                count += 1
                loc.append(i - M + 2)
                # 찾은 뒤 점프
                j = table[j]
            # 부분 매칭만 되면
            else:
                j += 1
    print(count)
    print(*loc)

T = input()
P = input()
kmp(T, P)
```

## Trie

```python

```

# 동적 프로그래밍(Dynamic Programming)

목차: LIS, LCS, 0-1-knapsack, Matrix Chain Multiplication

## 가장 긴 증가하는 부분 수열(LIS: Longest Increasing Subsequence)

```python
lst = [0, 3, 1, 6, 2, 2, 7]
N = len(lst)

# Solve1: NlogN
from bisect import bisect_left

MIN_VAL = int(-10e10)
dp = [0] * N
tmp = [MIN_VAL]

max_v = 0
for i in range(N):
    if tmp[-1] < lst[i]:
        tmp.append(lst[i])
        max_v += 1
        dp[i] = max_v
    else:
        dp[i] = bisect_left(tmp, lst[i])
        tmp[dp[i]] = lst[i]

print(max_v, dp)  # 4 [1, 2, 2, 3, 3, 3, 4]

# Solve2: N^2
dp = [1] * N
for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp), dp)  # 4 [1, 2, 2, 3, 3, 3, 4]
```

## LCS(Longest Common Subsequence)

> <https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/>

```python
def lcs(A, B):
    A = [" "] + list(A)
    B = [" "] + list(B)
    la = len(A)
    lb = len(B)
    dp = [[""] * lb for _ in range(la)]
    for i in range(1, la):
        for j in range(1, lb):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + A[i]
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]

    return dp[la-1][lb-1]

A = input()
B = input()
print(lcs(A, B))
```

## 배낭문제(0-1-knapsack)

> <https://github.com/wansang93/Algorithm/tree/master/BAEKJOON/problems/12865.md>

```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0, 0]]
dp = [0 for _ in range(K+1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(K, 0, -1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if weight <= j:
            dp[j] = max(value + dp[j-weight], dp[j])

print(dp[K])
```

## Matrix Chain Multiplication

```python

```

# 기하(Geometry)

목차: CCW, Convex Hull, Polygon

## Number of intersection points of two lines in 1 dimension

```python

```

## CCW

```python
p1 = map(int, input().split())
p2 = map(int, input().split())
p3 = map(int, input().split())

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

result = ccw(p1, p2, p3)
if result > 0:
    print(1)  # 반시계
elif result < 0:
    print(-1)  # 시계
else:
    print(0)  # 일직선

"""input
1 1
5 5
7 3
"""
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

```python
# 최빈 값 빠르게 1개 찾기(중복 시 가장 앞에)
print(max(nums, key=nums.count))


# 중복 시 2개 이상 리스트로 추출
from collections import Counter

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]
    modes = []
    
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])

    return modes

# Collection Counter 모듈 없는 버전
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

# Counter 함수 예시
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

## 순열(Permutation) nPr

DFS로 푸는 순열(num_in_same_depth 지울 것!)

비오름차순 정렬 추가(같은 깊이의 숫자 중복은 제거하는 코드 추가)

```python
N, R = map(int, input().split())
answer = []
lst = list(sorted(input()))
is_visited = [False] * N

def permutation(cnt):
    if cnt == R:
        print(*answer)
        return

    # check num in same depth
    num_in_same_depth = -1
    for i in range(N):
        if is_visited[i] or num_in_same_depth == lst[i]:
            continue
        answer.append(lst[i])
        is_visited[i] = True
        num_in_same_depth = lst[i]
        permutation(cnt+1)
        answer.pop()
        is_visited[i] = False

permutation(0)

'''
num_in_same_depth 를 지운 경우
[Input Example 1]
3 3
ABC
[Output Example 1]
A B C
A C B
B A C
B C A
C A B
C B A
'''
```

## 조합(Combination) nCr

DFS로 푸는 조합(num_in_same_depth 지울 것!)

비오름차순 정렬 추가(같은 깊이의 숫자 중복은 제거하는 코드 추가)

```python
N, R = map(int, input().split())
answer = []
lst = list(sorted(input()))

def combination(cnt, start):
    if cnt == R:
        print(*answer)
        return

    # check num in same depth
    num_in_same_depth = -1
    for i in range(start, N):
        if num_in_same_depth == lst[i]:
            continue
        answer.append(lst[i])
        num_in_same_depth = lst[i]
        combination(cnt+1, i+1)
        answer.pop()

combination(0, 0)

'''
num_in_same_depth 를 지운 경우
[Input Example 1]
4 2
ABCD
[Output Example 1]
A B
A C
A D
B C
B D
C D
'''
```

## 중복순열(Permuation with Repetition) nπr

DFS로 푸는 중복순열(num_in_same_depth 지울 것!)

비오름차순 정렬 추가(같은 깊이의 숫자 중복은 제거하는 코드 추가)

```python
N, R = map(int, input().split())
answer = []
lst = list(sorted(input()))

def permutation_repetition(cnt):
    if cnt == R:
        print(*answer)
        return

    # check num in same depth
    num_in_same_depth = -1
    for i in range(N):
        if num_in_same_depth == lst[i]:
            continue
        answer.append(lst[i])
        num_in_same_depth = lst[i]
        permutation_repetition(cnt+1)
        answer.pop()

permutation_repetition(0)

'''
num_in_same_depth 를 지운 경우
[Input Example 1]
3 3
ABC
[Output Example 1]
A A A
A A B
A A C
A B A
A B B
A B C
A C A
A C B
A C C
B A A
B A B
B A C
B B A
B B B
B B C
B C A
B C B
B C C
C A A
C A B
C A C
C B A
C B B
C B C
C C A
C C B
C C C
'''
```

## 중복조합(Combination with Repetition) nHr

DFS로 푸는 중복조합(num_in_same_depth 지울 것!)

비오름차순 정렬 추가(같은 깊이의 숫자 중복은 제거하는 코드 추가)

```python
N, R = map(int, input().split())
answer = []
lst = list(sorted(input()))

def combination_repetition(cnt, start):
    if cnt == R:
        print(*answer)
        return

    # check num in same depth
    num_in_same_depth = -1
    for i in range(start, N):
        if num_in_same_depth == lst[i]:
            continue
        answer.append(lst[i])
        num_in_same_depth = lst[i]
        combination_repetition(cnt+1, i)
        answer.pop()

combination_repetition(0, 0)

'''
num_in_same_depth 를 지운 경우
[Input Example 1]
4 2
ABCD
[Output Example 1]
A A
A B
A C
A D
B B
B C
B D
C C
C D
D D
'''
```

## 멱집합 & 부분 집합(PowerSet & SubSet)

> 출처: <https://velog.io/@tks7205/파이썬에서-부분집합-구하기>

```python
# itertools 라이브러리 사용
from itertools import combinations 

lst = [1, 2, 3]
N = len(lst)
subsets = []
for i in range(N+1):
    subsets += list(combinations(lst, i))

print(subsets)
# [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

# for문 활용
lst = [1, 2, 3]
subsets = [[]]

for i in lst:
    N = len(subsets)
    for j in range(N):
        subsets.append(subsets[j] + [i])

print(subsets)
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

## 다음 순열(Next Permutation)

```python
"""\
Next Permutation 원리

원리: i, j값을 찾은 뒤 교환하고 다시 정렬한다.

1. i 값 찾기(바꿀 첫번째 값)
1-1. 가장 뒤에 값 i로 설정
1-2. i값을 빼면서(<-이쪽으로 탐색)하기
    1-3. 오름차순 아닌거 찾기(i, i-1 비교!)

1-4. i값이 0이면(즉 모두다 뒤에서부터 오름차순이면)
    1-5. 다음 순열은 없음!

2. j 값 찾기(바꿀 두번째 값)
2-1. 가장 뒤에 값 j로 설정
2-2. j값을 빼면서 뒤에서부터 i전까지 탐색(무조건 탐색이 됨)
    2-3. 오름차순 아닌거 찾기(i-1, j 비교!)

3. 교환하기(i-1과 j 교환)
4. 마지막부터 i까지 오름차순으로 정렬하기
"""

N = int(input())
lst = list(map(int, input().split()))

def next_permutation(lst):
    N = len(lst) - 1
    i, j, k = [N] * 3

    while i > 0 and lst[i-1] >= lst[i]:
        i -= 1
    if i == 0:
        return [-1]

    while lst[i-1] >= lst[j]:
        j -= 1

    lst[i-1], lst[j] = lst[j], lst[i-1]

    while i < k:
        lst[i], lst[k] = lst[k], lst[i]
        i += 1
        k -= 1

    return lst

answer = next_permutation(lst)
print(*answer)
```

## 이전 순열(Prev Permutation)

```python
N = int(input())
lst = list(map(int, input().split()))

def prev_permutation(lst):
    L = len(lst) - 1
    i, j, k = [L] * 3
    
    while i > 0 and lst[i-1] <= lst[i]:
        i -= 1
    if i == 0:
        return [-1]
    
    while lst[i-1] <= lst[j]:
        j -= 1
    
    lst[i-1], lst[j] = lst[j], lst[i-1]
    
    while i < k:
        lst[i], lst[k] = lst[k], lst[i]
        i += 1
        k -= 1
    
    return lst

answer = prev_permutation(lst)
print(*ans)
```

# 신호 처리(Signal Processing)

## 고속 푸리에 변환(FFT(Fast Fourier Transform))

```python

```

# 비트 마스킹(Bit Masking)

```python
"""
bit mask의 핵심!!!!!!
bit mask의 num은 숫자가 아닌 32진수 boolean으로 볼 것!!!
(1 << i)는 움직이고 싶은 비트를 2^i 할지(i <= 32)
"""

# 8 = 0b1000 = 00000000_00000000_00000000_00001000(32bit)
num = 8
i = 2
print(bin(num)) # 0b1000

# 비트 i번째 켜기
num = num | (1 << i)
# before: 0b1000
# after:  0b1100 (2^i의 비트가 켜짐)

# 비트 i번째 삭제
num = num & ~(1 << i)
# before: 0b1100
# after:  0b1000

# 비트 i번째 조회(존재하면 1, 없으면 0)
print(num & (1 << i))  # 0

# 비트 반전(flag 처럼 사용 가능)
num = num ^ (1 << i)
num = num ^ (1 << i)
# before: 0b1000
# after:  0b1100 (2^i의 비트가 켜짐)
# after:  0b1100 (2^i의 비트가 꺼짐)

# 모든 비트 끄기
num = 0

# 모든 비트 켜기(n = bit_size)
n = 32
num = num | (2**n - 1)

# 모든 비트 반전
n = 32
num = ~n
```

# 잡기술(Miscellaneous)

## 두 행렬 곱(multiply two matrices without numpy)

```python
def multifly_matrix(lst1, lst2, mod=1):
    ans = []
    for i in range(len(lst1)):
        temp = []
        for j in range(len(lst2[0])):
            s = 0
            for k in range(len(lst1[0])):
                s += lst1[i][k] * lst2[k][j]
            temp.append(s % mod)
        ans.append(temp)

    return ans
```

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

print(two_pointer([1, 2, 3, 2, 5], 5))
# 3
```

## 구간 합(Interval Sum)

### 누적 합(Prefix Sum) 1차원

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

### 누적 합(Prefix Sum) 2차원

```python
N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        dp[i+1][j+1] += lst[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]

# for row in dp:
#     print(*row)

K = int(input())
for _ in range(K):
    y2, x2, y1, x1 = map(int, input().split())
    print(dp[y1][x1] - dp[y1][x2 - 1] - dp[y2 - 1][x1] + dp[y2 - 1][x2 - 1])
```

### 바이너리 인덱스 트리(Binary Indexed Tree(Fenwick Tree))

```python
test
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

파이썬의 재귀는 대략 1000 정도까지 제한되어 있음

이를 풀어주려면 아래와 같은 함수를 사용하면 됨

```python
#  the recursion limit of python is usually set to a small value (approx, 10^4).
import sys
sys.setrecursionlimit(10**6)
```

## 실전에서 느낀 것(What I felt in practice)

### 알파벳 대소문자 변경

백준 2744 대소문자 바꾸기

```python
S = "WrongAnswer"
s2 = S.swapcase()  # wRONGaNSWER
```

### 2차원 list의 총 합, 같은 2차원 list 더하기, 행렬 회전

백준 17144 미세먼지 안녕!

```python
# 2차원 list의 총 합
sum(map(sum, lst))

# 2차원 list의 열의 합
[sum(x) for x in zip(*lst)]

# 2차원 list의 행의 합
list(map(sum, lst))

# 2개의 2차원 list의 합
N= 2
list1 = [[1, 2], [3, 4]]
list2 = [[10, 20], [30, 40]]
new_list = [[sum(x) for x in zip(list1[i], list2[i])] for i in range(N)]
print(new_list)  # [[11, 22], [33, 44]]

# 회전 반시계 돌면서 값 바꿔주기
y, x = cleaner_loc[0]
now_v = _list[y][x]
# temp = 0
for dy, dx in((0, 1), (-1, 0), (0, -1), (1, 0)):
    while True:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < R and 0 <= nx < C:
            now_v, _list[ny][nx] = _list[ny][nx], now_v
            # # 타언어 스타일
            # temp = _list[ny][nx]
            # _list[ny][nx] = now_v
            # now_v = temp
            y = ny
            x = nx
        else:
            break
```

### 숫자를 문자로 바꾼 후 알파벳 순으로 정렬

백준 1755 숫자놀이

```python
dic = {
    "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
    "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero",
}

M, N = map(int, input().split())

# [숫자, 문자]를 2차원 리스트로 만들기
nums = []
for i in range(M, N+1):
    alpha_num = ' '.join([dic[c] for c in str(i)])
    nums.append([i, alpha_num])

# 문자순으로 정렬하기
nums.sort(key=lambda x: x[1])
```

### 10개씩 끊어서 출력하기

```python
# 방법1
for i in range(len(nums)):
    print(nums[i][0], end=' ')
    if i % 10 == 9:
        print()

# 방법2
for i in range(0, N, 10):
    print(*nums[i:i+10])
```

### 파이썬 토글(toggle)

백준 1244 스위치 켜고 끄기

``` python
a, b = 1, 0
# (1 - 자기 자신) 하면 토글이 됨
a = 1 - a
b = 1 - b
```

### 배열 돌리기 여러가지 스킬

백준 17406 배열 돌리기 4

2차원 리스트 deepcopy without deepcopy module

``` python
lst = [[1, 2], [3, 4]]
# 2차원 리스트 deepcopy
copy_lst = [x[:] for x in lst]
# 아래 방법으로 하면 오류가 생길 수 있음(주의!)
shallow_lst = lst[:]
```

회전(시계방향)하면서 값 바꿔주기

``` python
'''
arr: 배열, r, c = 가운데 점(축), s: 확대반경
'''
def _rotate(arr, r, c, s):
    for ss in range(1, s+1):
        x, y, tmp = r-ss, c-ss, arr[r-ss][c-ss]
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            for _ in range(ss * 2):
                arr[x][y] = arr[x+dx][y+dy]
                x, y = x + dx, y + dy

        arr[r-ss][c-ss+1] = tmp
```

``` python
# 예시 코드
lst = [[1, 2], [3, 4]]
shallow_lst = lst[:]
deep_lst = [x[:] for x in lst]

# 얕은 복사는 id가 같음
print(id(lst[0]))  # 1994660564480
print(id(shallow_lst[0]))  # 1994660564480
print(id(deep_lst[0]))  # 1994665346432

# 얕은 복사의 재할당은 문제없음
lst[0] = [0, 1]
print(lst)  # [[0, 1], [3, 4]]
print(shallow_lst)  # [[1, 2], [3, 4]]
print(deep_lst)  # [[1, 2], [3, 4]]

# 얕은 복사의 추가는 문제가 생김
lst[1].append(5)
print(lst)  # [[0, 1], [3, 4, 5]]
print(shallow_lst)  # [[1, 2], [3, 4, 5]]
print(deep_lst)  # [[1, 2], [3, 4]]
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

백준 11650 좌표 정렬하기

```python
lst.sort(key=lambda x: (x[0], x[1]))
```

### 정렬 문자로 된 숫자

백준 1427 소트 인사이드

[sorted docs](https://docs.python.org/3/howto/sorting.html)

```python
sorted(N)[::-1]  # sorted는 아스키 기준으로 정렬하는거 같음
```

### 단어 중복 체크, 연속된 단어는 허용

백준 1316 그룹 단어 체커

```python
# 짧은 코드
cnt += list(word) == sorted(word, key=word.find)

# 긴 코드
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

백준 2941 크로아티아 알파벳

```python
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cr in croatian:
    s = s.replace(cr, '!')
```

### 알파벳 찾기, find와 index의 차이 익히기

백준 10809 알파벳 찾기

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

### 둘 다 홀수일때만 최솟값 구하기

백준 8674 Tabliczka

```python
min(a % 2 * b, b % 2 * a)
```

### 몫 나눈 뒤 올림, 내림, 반올림 하는 법

> 출처: <https://xy-plane.tistory.com/11>

```python
# 내림
share = b//a
share = int(b/a)
# 올림
share = (b+a-1) // a
share = (b-1) // a+1
# 반올림
share = (b+a/2) // a
```

### 다중조건이 True 일 때 쓰면 좋음

백준 16017 Telemarketer or not?

```python
a, b, c, d = [int(input()) for _ in range(4)]
if all((b==c, a>7, d>7)):
    print("ignore")
else:
    print("answer")
```

### 튜플 비교

백준 16199 나이 계산하기

> 튜플 비교 원리: <https://howtodoinjava.com/misc/compare-tuples/>

```python
# 만 나이 계산
old = ny - by - ((bm, bd) > (nm, nd))
```

### (a - b) // c 를 올림, a - b 가 0보다 작으면

```python
- min(0, (a-b)//-c)
```

### 빠른 시간 계산(Overflow 적용)

```python
h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
t = (h2-h1) * 3600 + (m2-m1) * 60 + (s2-s1)
# overflow(1일)
if t < 0:
    t += 3600 * 24
print(t)
```

### 다각형의 면적 구하기

백준 2166

```python
N = int(input())
corners = [tuple(map(int, input().split())) for _ in range(N)]

# e.g. corners = [(2.0, 1.0), (4.0, 5.0), (7.0, 8.0)]
def area(corners):
    n = len(corners) # of corners
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2
    return area

print(round(area(corners), 1))
```

### 2의 제곱수 판단 비트연산

백준 11966 2의 제곱인가?

```python
n & -n == n
# 2의 제곱수면 True 아니면 False
```

### 2진수의 마지막 비트 찾기

백준 17119 비트가 넘쳐흘러

나중에 Fenwick Tree에서 사용

K & -K

```python
for K in range(9):
    print(K, "의 마지막 비트:", K & -K)
"""
0 의 마지막 비트: 0
1 의 마지막 비트: 1
2 의 마지막 비트: 2
3 의 마지막 비트: 1
4 의 마지막 비트: 4
5 의 마지막 비트: 1
6 의 마지막 비트: 2
7 의 마지막 비트: 1
8 의 마지막 비트: 8
"""
```

### 속도 방향이 있는 좌표 한번에 이동하기

백준 17143 낚시왕

```python
# row, column, speed, direction
def get_next_loc(r, c, s, d):
    global R, C
    # 축(aixs)별 사이클(cycle) 구하기
    # 1이 위, 2가 아래
    if d == 1 or d == 2:
        cycle = (R - 1) * 2
        # 방향(d)에 따른 인덱스 가중치 더하기
        if d == 1:
            s += cycle - r
        else:
            s += r
        # 유효한 범위만 계산
        s %= cycle
        
        # r은 s좌표, d는 양수
        d = 2
        r = s
        # 축보다 밖에 있으면 음수 방향으로 출발
        if s >= R:
            d = 1
            r = cycle - s
        return (r, c, d)

    # 3이 오른쪽, 4가 왼쪽
    if d == 3 or d == 4:
        cycle = (C - 1) * 2
        # 방향(d)에 따른 인덱스 가중치 더하기
        if d == 4:
            s += cycle - c
        else:
            s += c
        # 유효한 범위만 계산
        s %= cycle
        
        # c은 s좌표, d는 양수
        d = 3
        c = s
        # 축보다 밖에 있으면 음수 방향으로 출발
        if s >= C:
            d = 4
            c = cycle - s
        return (r, c, d)
```

### 사각형 교차판정

백준 2527 직사각형

```python
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    xl = max(x1, x2)
    xr = min(p1, p2)
    yb = max(y1, y2)
    yt = min(q1, q2)

    xdiff = xr - xl
    ydiff = yt - yb

    # 직사각형
    if xdiff > 0 and ydiff > 0:
        print('a')
    # 점
    elif xdiff == 0 and ydiff == 0:
        print('c')
    # 교차x
    elif xdiff < 0 or ydiff < 0:
        print('d')
    # 선분
    else:
        print('b')
```

### 순위 동률 구하기(index, gold, silver, bronze)

백준 8979 올림픽

```python
# K가 찾고자 하는 index 번호
N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# 인덱스 빨리찾기
idx = [lst[i][0] for i in range(N)].index(K)

rank = -1
for i in range(N):
    if lst[idx][1:] == lst[i][1:]:
        rank = i + 1
        break

print(rank)
```

### 여러가지 조건으로 정렬하기

백준 1431 시리얼 넘버

```python
N = int(input())
lst = [input() for _ in range(N)]

def get_sum(string):
    res = 0
    for c in string:
        if c.isdigit():
            res += int(c)
    
    return res

# 이 부분
lst.sort(key= lambda x: (len(x), get_sum(x), x))
for s in lst:
    print(s)
```

### 토너먼트 몇 번째에서 만나는지 확인하는 방법

백준 1057 토너먼트

```python
N, a, b = map(int, input().split())
cnt = 0
while a != b:
    cnt += 1
    a -= a // 2
    b -= b // 2

print(cnt)
```

### 테스트 케이스가 없는 경우

백준 4375 1

```python
while True:
    try:
        N = int(input())
    except:
        break
    # 로직 처리는 밑에 작성하면 더 깔끔함
```

### 여러줄 입력 & 가장 긴 단어 찾기

백준 5637 가장 긴 단어

```python
import re

# 여러줄 입력
file = open(0).read()[:-1]

# 긴 단어 찾기
lst = re.findall('[A-Z\-a-z]+', file)
lst.sort(key=len, reverse=True)

print(lst[0].lower())
```

### 평평한 문자 행렬화 후 행렬 회전(기본기 문제)

백준 5426 비밀 편지

```python
# n*n행렬 -90도 회전
p = [s[n-i-1::n] for i in range(n)]
```
