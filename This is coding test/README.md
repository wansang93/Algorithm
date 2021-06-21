# 이것이 코딩 테스트다(2021)

나동빈 / 한빛 미디어

- 2020-10-27(1, 2장)
- 2020-11-24(2, 3장)
- 2021-01-04(4, 10장)
- 2021-01-24(9장)
- 2021-02-04(3, 4장)
- 2021-05-14(5장)
- 2021-05-16(6장)
- 2021-06-20(7장)

교제 사이트 링크 -> [https://github.com/ndb796/python-for-coding-test](https://github.com/ndb796/python-for-coding-test)

유튜브 링크 -> [https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

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
  queue = deque()  # queue 생성
  queue.append('a')  # a 추가
  queue.popleft()  # 제거
  queue.reverse()  # 역순
  ```

- 재귀 함수(Recursive Function)
  - 파이썬에서 최대 깊이 초과가 있음, 재귀 함수가 무한으로 발생(recursive depth exceeded) 방지
  - 모든 재귀 함수는 반복문으로 작성 가능
  - 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 내부에 스택 프레임이 쌓임
    - 스택을 사용할 때, 스택 라이브러리 대신 재귀 함수를 사용하는 경우가 많음
  
  팩토리얼 구현
  ```python
  def factorial_recursive(n):
      if n <= 1:
          return 1
      return n * factorial_recursive(n-1)
  ```

  유클리드 호제법 구현
  ```python
  def gcd(a, b):
      if a % b == 0:
          return b
      else:
          return gcd(b, a % b)
  ```

## 3-1. DFS(Depth First Search)

- 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색
- 스택 자료구조(혹은 재귀 함수)를 이용

```python
def dfs(graph, start, visited):
    visited[start] = True
    # print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
```

## 3-2. BFS(Breath First Search)

- 넓이 우선 탐색, 가까운 노드들을 우선적으로 탐색
- 큐 자료구조를 이용

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

### 3-3-1. 음료수 얼려 먹기

```python
def dfs(x, y, n, m):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(x-1, y, n, m)
        dfs(x, y-1, n, m)
        dfs(x+1, y, n, m)
        dfs(x, y+1, n, m)
        return True
    return False
```

### 3-3-2. 미로 탈출

```python
from collections import deque

def bfs(x, y, n, m, graph):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]
```

# 4. 정렬 알고리즘

Sorting: Arrange systematically in groups; separate according to type

## 4-1. 선택 정렬

```python
import copy

def selection_sort(lst_unsorted):
    lst = copy.deepcopy(lst_unsorted)

    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(1+i, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
```

## 4-2. 삽입 정렬

```python
import copy

def insert_sort(lst_unsorted):
    lst = copy.deepcopy(lst_unsorted)

    n = len(lst)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst
```

## 4-3. 퀵 정렬

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

## 4-4. 계수 정렬

공간 복잡도가 더 높을 수 있지만 매우 빠름

데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용

데이터 갯수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의경우에도 O(N+K)를 보장

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```

# 5. 이진 탐색

## 5-1. 이진 탐색 개요

- 탐색 범위를 절반으로 줄여 데이터를 탐색 하는 방법
- 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정

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


n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search(array, target, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)  # 3
```

# 6. DP

- 메모리를 적절히 사용, 다시 계산하지 않도록
- DP를 사용할 수 있는 **조건**
  1. 최적 부분 구조(Optimal Substructure): 큰 문제를 작은 문제로 나눌 수 있는지
  2. 중복되는 부분 문제(Overlapping Subproblem): 동일한 작은 문제를 반복적으로 해결
- 방법
  1. **하향식(Top Down)**
     - 메모이제이션(Memoization) 방식
       - 한 번 계산한 결과를 메모리 공간에 메모
       - 값을 기록해 놓아 **캐싱(Caching)**라고도 불림
  2. **상향식(Bottom Up)**
     - 결과 저장용 리스트를 **DP 테이블**
- DP vs 분할 정복
  - 공통점: 큰 문제를 작은 문제로 나눠 작은 문제의 답을 모아 큰 문제를 해결
  - 차이점: 부분 문제의 중복
    - DP: 각 부분 문제들이 서로 영향을 미치며 부분 문제의 중복
    - 분할 정복: 동일한 부분 문제의 반복 계산x
- **접근 방법**
  1. DP 유형인지 확인, 다른 방법이 가능하면 다르게 풀기
  2. 재귀 함수로 비효율적인 완전 탐색 프로그램으로 작성
  3. 작은 문제에서 구한 답이 큰 문제로 그대로 사용할 수 있으면 코드 개선

## 6-1. 피보나치 수열

단순 재귀함수 사용(시간 복잡도: O(2**N))

```python
def fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
```

Top-Down DP(시간 복잡도: O(N))

```python
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
```

## 6-2. 개미 전사

```python
def ant_warriors(lst):
    N = len(lst)
    d = [0] * N
    d[0] = lst[0]
    d[1] = max(lst[0], lst[1])
    for i in range(2, N):
        d[i] = max(d[i-1], d[i-2] + lst[i])

    # print(d)
    return d[N-1]

lst = [1, 2, 3, 4, 5, 3, 0, 3]
print(ant_warriors(lst))  # 12
```

## 6-3. 1로 만들기

```python
def make_the_one(x):
    d = [0] * (x+1)

    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
    # print(d)
    
    return d[x]

# x = 26
# print(make_the_one(x))
```

## 6-4. 효율적인 화폐 구성

```python
INF = 10000
def money_solution(lst, m):
    n = len(lst)
    d = [0] + [INF] * m
    for i in range(n):
        for j in range(lst[i], m+1):
            if d[j - lst[i]] != INF:
                d[j] = min(d[j], d[j-lst[i]]+1)
    # print(d)

    return d[m]

data = [2, 3]
m = 12
print(money_solution(data, m))  # 4
```

## 6-5. 금광

```python
def gold_mine(n, m, lst):

    dp = []
    idx = 0
    for i in range(n):
        dp.append(lst[idx:idx+m])
        idx += m

    for x in range(1, m):
        for y in range(n):
            if y == 0:
                left_up = 0
            else:
                left_up = dp[y-1][x-1]
            if y == n-1:
                left_down = 0
            else:
                left_down = dp[y+1][x-1]
            left = dp[y][x-1]
            dp[y][x] = dp[y][x] + max(left, left_up, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    return result

# print(gold_mine(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]))
```

## 6-6. 병사 배치하기(LIS 응용)

```python
def deploy_soldiers(n, lst):
    result = 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # print(dp)
    result = n - max(dp)
    return result

print(deploy_soldiers(7, [4, 2, 5, 8, 4, 11, 15]))
```

# 7. 최단 경로 알고리즘

- 문제 상황
  - 한 지점에서 다른 한 지점까지의 최단 경로
  - 한 지점에서 다른 모든 지점까지의 최단 경로
  - 모든 지점에서 다른 모든 지점까지의 최단 경로

## 7-1. 다익스트라 최단 경로 알고리즘

- 특정 노드 -> 다른 모든 노드로 가는 최단 경로 계산
- 그리디로 분류
- 동작 과정
  - 출발 노드 설정
  - 최단 거리 테이블을 초기화
  - 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
  - 해당 노드를 거쳐 다른 노드로 가는 비용을 계산, 최단 거리 테이블 갱신

예시 코드(단순)

```python
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra2(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


INF = int(1e9)  # 10억

# n: 노드의 갯수
# m: 간선의 갯수
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


dijkstra2(start)
print(distance)
```

힙(Heap)자료구조를 이용

예시 코드(우선순위 큐)

```python
import heapq
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)  # 10억

# n: 노드의 갯수
# m: 간선의 갯수
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


print(graph)
dijkstra(start)
print(distance)
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

## 7-2. 플로이드 워셜 알고리즘

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
- 플로이드 워셜(Floyd-Warshall)알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
  - 다만 매 단계마다 방문하지 않은 노드 중 최단 거리를 갖는 노드를 찾는 과정이 필요x
- 2차원 테이블에 최단 거리 정보를 저장
- 다이나믹 프로그래밍로 분류
- 동작 과정
  - 그래프를 준비하고 최단 거리 테이블을 초기화
  - 각 노드별로 점화식 수행(Dab = min(Dab, Dak + Dkb))
- 성능 분석
  - 노드의 개수가 N개일 때 알고리즘 상 N번의 단계를 수행
  - 각 단계마다 O(N**2)의 연산을 통해 모든 경로 고려
  - 시간복잡도 O(N**3)

코드

```python

```

## 7-3. 전보

```python

```


## 7-4. 미래 도시

```python

```

# 8. 기타 그래프 이론

추후 업데이트

# 9. 코딩 테스트에서 자주 출제되는 기타 알고리즘

## 9-1. 소수(Prime Number)

### 9-1-1. 해당 수가 소수인지 판별

기본적인 알고리즘
- 시간복잡도: O(x)

```python
def is_prime_number(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True
```

개선된 알고리즘
- 시간복잡도: O(x**(1/2))

```python
def is_prime_number(x):
    for i in range(2, int(x**0.5+1):
        if x % i == 0:
            return False
    return True
```

### 9-1-2. 다수의 수가 소수인지 판별

다수의 소수 판별: 에라토스테네스의 체
- 시간복잡도: O(NloglogN)
- 장점: 큰 수의 이하인 소수들을 구할 때 빠름
- 단점: 메모리 공간, 하나의 소수만 궁금할 때 효율성 낮음

```python
def prime_list(n):
    sieve = [False, False] + [True] * (n-1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]
```

## 9-2. 투포인터(Two Pointers)

리스트에 순차적으로 접근해야 할 때 두 점의 위치를 기록하면서 처리

### 9-2-1. 특정한 합을 가지는 부분 연속 수열 찾기

문제
- N개의 자연수로 구성된 수열
- 합이 M인 부분 연속 수열의 갯수를 구해라
- 수행 시간 제한은 O(N)
- 완전 탐색의 경우 O(N**2)

해결법

```python
def two_pointer(lst, m):
    n = len(lst)
    count = 0
    end = 0
    interval_sum = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += lst[end]
            end += 1
        if interval_sum == m:
            count += 1
        interval_sum -= lst[start]

    return count
```

## 9-3. 구간 합(Interval Sum)

연속적으로 나열된 N개의수가 있을 때 특정 구간의 모든수를 합한 값을 계산

### 9-3-1. 구간 합 빠르게 계산하기

문제
- N개의 정수로 구성된수열
- M개의 쿼리(Query) 정보가 주어짐
  - 각 쿼리는 Left, Right로 구성
  - 각 쿼리에 대해 [Left, Right] 구간에 포함된 데이터의 합을 출력
- 수행 시간 제한은 O(N + M)

해결법
- 접두사 합(Prefix Sum): 배열의 맨 앞부터 특정 위치까지 합을 미리 구해 놓는 것
  - N개의 수 위치 각각에 접두사 합을 계산하여 P에 저장
  - 매 M개의 쿼리 정보를 확일 할 때 구간합은 P[Right] - P[Left-1]이다.

```python
def interval_sum(lst, query):
    p = [0] * (len(lst) + 1)
    result = [0] * len(query)

    for i, v in enumerate(lst):
        p[i+1] = p[i] + v

    for i, v in enumerate(query):
        result[i] = p[v[1]] - p[v[0]-1]

    return result
```

# 10. 개발형 코딩 테스트

## 10-1. 개발형 코딩 테스트

코딩테스트의 유형
- 정해진 목적에 따라 동작하는 완성된 프로그램을 개발
  - 예1) 모바일 클라이언트 개발: 안드로이드, IOS 앱 개발
  - 예2) 웹 서버 개발: 스프링(Spring), 장고(Django) 등의 서버 개발 프레임 워크 활용

- 해커톤(Hackathon): 단기간에 아이디어를 제품화하는 프로젝트 이벤트

- 분야와 상관없이 알아야 하는 개념들
  - 서버, 클라이언트, JSON, REST API, ...

## 10-2. 서버와 클라이언트

- 클라이언트 -> Request
  - Request를 보내고 Response를 도착할 때 까지 기다림
- 서버 -> Response
  - Request를 처리후 Response를 함

## 10-3. HTTP 프로토콜

- HTTP(HyperText Transfer Protocol): 웹 상에서 데이터를 주고 받기 위한 프로토콜
- 클라이언트는 Request 목적에 따라 적절한 HTTP method를 이용
  - GET: 특정 데이터 조회, 정보 검색 등
  - POST: 특정 데이터 생성, 회원 가입 등
  - PUT: 특정 데이터 수정, 회원 정보 수정 등
  - DELETE: 특정 데이터 삭제, 회원 정보 등

파이썬 GET 예시

```bash
# ImportError: No module named requests
pip install requests
```

```python
import requests

target = 'http://google.com'
response = requests.get(url=target)
print(response.text)  # <!doctype html><html itemscope="" ...
```

## 10-4. REST

### 10-4-1. REST 등장 배경

- HTTP는 다양한 HTTP메서드를 지원
- 실제로는 서버가 각 메서드의 기본 설명을 따르지 않아도 프로그램을 개발 가능
- 저마다 다른 방식을 개발시 문제가 될 수 있어 기준이 되는 아키텍처가 필요

### 10-4-2. REST 개요

- **REST(Representational State Transfer)** 는 *각 자원(Resource)에 대해 자원의 상태에 대한 정보를 주고받는 개발 방식*
  - 자원(Resource): URI를 이용
  - 행위(Verb): HTTP 메서드를 이용
  - 표현(Representations): 페이로드를 이용

> URI: Uniform Resource Identifier(구분자)
> 1. rewrite 기술을 사용하여 만든 의미있는 식별자
> 2. REST 서비스(url로 실행되는 서비스)
> 3. Web-oriented architecture(웹 기반의 구조문법)
> 
> URL: Uniform Resource Locator(위치)
> > 출처: [https://blog.lael.be/post/61](https://blog.lael.be/post/61)

### 10-4-3. REST API 란?

- **API(Application Programming Interface)**: 프로그램이 상호작용하기 위한 인터페이스를 의미
- **REST API**: REST 아키텍처를 따르는 API
- **REST API 호출**: REST 방식을 따르고 있는 서버에 특정한 요청을 전송

REST 방식을 따르고 있는 서버에 특정한 요청을 전송하면 어떠한 데이터 형식으로 받을 것인가?

### 10-4-4. JSON

JSON(JavaScript Object Notation): 데이터를 주고받는 데 사용하는 경량의 데이터 형식

JSON 데이터는 키와 값의 쌍으로 이루어진 데이터 객체, 파이썬 딕셔너리와 매우 비슷

JSON 객체 파일 저장 예제

```python
import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id": "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby": ["football", "programming"]
}

# JSON 데이터로 변환하는 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)
```

### 10-4-5. REST API 연습용 서비스

- 목킹(Mocking)이란 어떠한 기능이 있는 것처럼 흉내내어 구현한 것
- 가상의 REST API 제공 서비스 -> [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/)
  - 사용자, 개시물 등 가상의 API를 클라이언트 측에서 호출해 사용
    ```json
    // 20210103214557
    // https://jsonplaceholder.typicode.com/users/1

    {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
        }
    }
    ```

### 10-4-6. REST API를 호출하여 회원 정보를 처리하는 예제

```python
import requests

# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 반환
data = response.json()

# 모든 사용자(user) 정보를 확이하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)
# ['Leanne Graham', 'Ervin Howell', ... ,'Clementina DuBuque']
```
