# 이것이 코딩 테스트다(2021)

나동빈 / 한빛 미디어

- 2020-10-27(1, 2장)
- 2020-11-24(2, 3장)

교제 사이트 링크 -> [https://github.com/ndb796/python-for-coding-test](https://github.com/ndb796/python-for-coding-test)

# 1. 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기

## 1-1. 코딩 테스트 준비하기, 참고하기

- request, json 라이브러리 익히기
- 리플잇 링크 -> [repl.it](https://repl.it/)
- 파이썬 튜터 링크 -> [http://www.pythontutor.com/visualize.html](http://www.pythontutor.com/visualize.html)
- 팀노트 만들기, 예시 링크 -> [https://github.com/ndb796/Python-Competitive-Programming-Team-Notes](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes)

## 1-2. 파이썬 스킬

1. x*y 의 리스트 초기화
   ```python
   x, y = 3, 5
   mylist = [[0] * x for _ in range(y)]
   ```

2. 정렬
   ```python
   mylist = {('a', 50), ('b', 30), ('c', 60)}
   sorted(mylist, key=lambda x: x[1])
   ```

3. map
   ```python
   list1 = [1, 2, 3, 4, 5]
   list2 = [50, 40, 30, 20, 10]
   map(lambda a, b: a+b, list1, list2)
   ```

4. 라이브러리들
   ```python
   import itertools  # 순열과 조합
   import heapq  # 힙 자료구조
   import bisect  # 이진 탐색
   import collections  # 덱, 카운터
   import math  # 수학

   # 1. 표준 라이브러리
   eval('(3+5)*7')  # 56

   # 2. 순열, 조합, 중복순열, 중복조합
   mylist = ['1', '2', 'b', 'a']

   from itertools import permutations  # 순열
   from itertools import combinations  # 조합
   from itertools import product  # 중복순열
   from itertools import combinations_with_replacement  # 중복조합

   print(list(permutations(mylist, 2)))
   print(list(combinations(mylist, 2)))
   print(list(product(mylist, repeat=2)))
   print(list(combinations_with_replacement(mylist, 2)))

   # 3. Count
   from collections import Counter
   counter = Counter(['a', 'a', 'b', 'b', 'a', 'c', 'd', 'c'])
   print(counter['a'])  # 3
   print(dict(counter))  # {'a': 3, 'b': 2, 'c': 2, 'd': 1}

   # 최대 공약수, 최소 공배수
   import math

   # 최대 공약수(GCD)
   print(math.gcd(21, 14))

   # 최고 공배수
   def lcm(a, b):
      return a * b // math.gcd(a, b)
   print(lcm(21, 14))
   ```

# 2. 그리디 & 구현

## 2-1. 그리디(Greedy)

탐욕법으로 얻은 해가 최적의 해가 되는 상황에서 사용

### 2-1-1. 1이 될 때 까지

``` python
def until_one(n, k):
    count = 0
    while True:
        target = (n//k) * k
        count += n - target
        n = target
        if n < k:
            break        
        count += 1
        n //= k
    return count + n - 1
```

### 2-1-2. 곱하기 혹은 더하기

```python
def max_num(s):
    num = int(s[0])
    for c in s[1:]:
        i = int(c)
        if i == 0 or i == 1:
            num += i
        else:
            num *= i
    
    return num
```

### 2-1-3.모험가 길드

```python
def adventurer_guild(l):
    count = 0
    mylist = l.sort()
    people = 0
    for i in mylist:
        people += 1
        if i <= people:
            people = 0
            count += 1
    
    return count
```

## 2-2. 구현(Implementation)

풀이는 쉽지만 소스코드로 옮기기 어려운 문제

구현의 유형
- 알고리즘은 간단, 코드가 지나칠 만큼 길어지는 문제
- 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
- 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
- 적절한 라이브러리를 찾아서 사용해야 하는 문제

### 2-2-1. 상하좌우

```python
def udlr(n, plans, now):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    for plan in plans:
        for i in range(len(move_types)):
            if move_types[i] == plan:
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]
        if nx < 1 or nx > n or ny < 1 or ny < n:
            continue
        now = nx, ny

    return now
```

### 2-2-2. 시각

```python
def count_three(n):
   count = 0
   for i in range(n+1):
      for j in range(60):
         for k in range(60):
            if '3' in str(i) + str(j) + str(k):
               count += 1
   
   return count
```

### 2-2-3. 왕실의 나이트

```python
def knight_avaliable(location):
    count = 0
    x = int(ord(location[0])) - int(ord('a')) + 1
    y = int(location[1])
    knight_move = [(-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1),
                   (2, 1), (1, 2), (-1, 2)]

    for m in knight_move:
        nx = m[0] + x
        ny = m[1] + y
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            count += 1

    return count
```

### 2-2-4. 문자열 재정렬

```python
def sort_string(data):
    value = 0
    result = ''
    for x in data:
        if x.isalpha():
            result += x
        else:
            value += int(x)

    result.sort()
    result += str(value)
    return result
```

# 3. DFS & BFS

- 탐색: **원하는 데이터를 찾는 과정**
  
  DFS(Depth First Search), BFS(Breadth-First Search)는 대표적 탐색 알고리즘 중 하나

- 스택과 큐 구현

  ```python
  # 스택(list 활용)
  stack = []
  
  # 큐(deque 활용)
  from collections import deque
  queue = deque()
  ```

- 재귀 함수(Recursive Function)는 파이썬에서 최대 깊이 초과가 있다.



# 6. DP

- 메모리를 적절히 사용, 다시 계산하지 않도록
- DP를 사용할 수 있는 경우
  1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있는지
  2. 중복되는 부분 문제: 동일한 작은 문제 를 반복적으로 해결