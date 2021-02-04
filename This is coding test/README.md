# 이것이 코딩 테스트다(2021)

나동빈 / 한빛 미디어

- 2020-10-27(1, 2장)
- 2020-11-24(2, 3장)
- 2021-02-04(3, 4장)
- 2021-01-24(9장)
- 2021-01-04(4, 10장)

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

```python

```

## 4-4. 계수 정렬


# 6. DP

- 메모리를 적절히 사용, 다시 계산하지 않도록
- DP를 사용할 수 있는 경우
  1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있는지
  2. 중복되는 부분 문제: 동일한 작은 문제 를 반복적으로 해결

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
