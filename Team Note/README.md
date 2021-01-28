# Python Competitive Programming Team Notes

- This repository is a python library for PS(Problem-Solving) Competition.
- When you need an implementation of a specific algorithm, please let me know.
- 알고리즘 대회를 위한 **파이썬 (Python) 소스코드 저장소**입니다.
- **동빈나** 님의 사이트를 참고해서 만들었습니다. -> [동빈나님 Team Notes](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/README.md)

# 잡기술

## 단어 중복 체크, 연속된 단어는 허용

백준 1316번 그룹 단어 체커

```python
cnt += list(word) == sorted(word, key=word.find)
```

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

# Contents

### Sorting

- [Selection Sort]
- [Insertion Sort]
- [Quick Sort]
- [Counting Sort]
- [Python Sort Library]

### Searching

- [Binary Search]
- [Python Binary Search Library]
    - [Count the number of frequencies of elements whose value is between \[left, right\] in a sorted array]
- DFS
- BFS
    - [Find the number of connected components]
- [DFS & BFS Examples 1]

### Graph

- [Dijkstra Shortest Path]
- [Minimum Spanning Tree (MST)]
- [Topology Sort]
- Floyd–Warshall algorithm
- Bipartite Matching

### Data Structure

- [Disjoint-Set (Union-Find)]
- Tree
- Line
- Plane

### String

- Rabin-Karp
- KMP
- Trie

### Dynamic Programming

- Tiling Problem
- 0-1 Knapsack Problem
- LIS (Longest Increasing Subsequence)
- LCS (Longest Common Subsequence)
- Matrix Chain Multiplication

### Geometry

- [Number of intersection points of two lines in 1 dimension]
- CCW
- Convex Hull
- Polygon

### Probability Theory

- Permutation
- Combination

### Number Theory

- [GCD (Greatest Common Divisor)]
- [LCM (Least Common Multiple)]
- [Check Prime Number]
- [Find All Divisors]
- [Prime Factorization]
- Sieve of Eratosthenes

### Signal Processing

- FFT

### Miscellaneous

- Two Pointers
    - [Number of intervals whose sum is M]
- Interval Sum
    - [Prefix Sum]
    - [Fenwick Tree (Binary Indexed Tree)]
- [Matrix Rotation]
- Handling Recursion Limit