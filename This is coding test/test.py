# 1-1. x*y 의 리스트 초기화
x, y = 3, 5
mylist = [[0] * x for _ in range(y)]
# print(mylist)

# 1-2. 정렬
mylist = {('a', 50), ('b', 30), ('c', 60)}
sorted(mylist, key=lambda x: x[1])
# print(mylist)

# 1-3. map
list1 = [1, 2, 3, 4, 5]
list2 = [50, 40, 30, 20, 10]
mylist = list(map(lambda a, b: a+b, list1, list2))
# print(mylist)

# 1-4. 라이브러리들
import itertools  # 순열과 조합
import heapq  # 힙 자료구조
import bisect  # 이진 탐색
import collections  # 덱, 카운터
import math  # 수학

# 1. 표준 라이브러리
eval('(3+5)*7')  # 56

# 2. 순열, 조합, 중복순열, 중복조합
from itertools import permutations  # 순열
from itertools import combinations  # 조합
from itertools import product  # 중복순열
from itertools import combinations_with_replacement  # 중복조합

mylist = ['1', '2', 'b', 'a']
# print(list(permutations(mylist, 2)))
# print(list(combinations(mylist, 2)))
# print(list(product(mylist, repeat=2)))
# print(list(combinations_with_replacement(mylist, 2)))

# 3. Count
from collections import Counter
counter = Counter(['a', 'a', 'b', 'b', 'a', 'c', 'd', 'c'])
# print(counter['a'])
# print(dict(counter))

import math

# 최대 공약수(GCD)
# print(math.gcd(21, 14))

# # 최고 공배수
def lcm(a, b):
    return a * b // math.gcd(a, b)
# print(lcm(21, 14))


# 2-1-1. 1이 될 때 까지
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


# 2-1-2. 곱하기 혹은 더하기
def max_num(s):
    num = int(s[0])
    for c in s[1:]:
        i = int(c)
        if i == 0 or i == 1:
            num += i
        else:
            num *= i
    
    return num


# 2-1-3.모험가 길드
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


# 2-2-1. 상하좌우
def udlr(n, plans, now):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    nx, ny = 0, 0
    for plan in plans:
        for i in range(len(move_types)):
            if move_types[i] == plan:
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]
        if nx < 1 or nx > n or ny < 1 or ny < n:
            continue
        now = nx, ny

    return now


# 2-2-2. 시각
def count_three(n):
   count = 0
   for i in range(n+1):
      for j in range(60):
         for k in range(60):
            if '3' in str(i) + str(j) + str(k):
               count += 1
   
   return count


# 2-2-3. 왕실의 나이트
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


# 2-2-4. 문자열 재정렬
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


# 3. 팩토리얼 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


# 3. 최대 공약수 구현
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# 3-1. DFS(Depth-First Search)
def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 3-2. BFS
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



graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# visited = [False] * 9
# dfs(graph, 1, visited)
# print()
# visited = [False] * 9
# bfs(graph, 1, visited)


# 3-1-1. 음료수 얼려 먹기
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


# 3-1-2. 미로 탈출
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
        
    

# 4-1. 선택 정렬
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


# 4-2. 삽입 정렬
import copy


def insert_sort(lst_unsorted):
    lst = copy.deepcopy(lst_unsorted)

    n = len(lst)
    for i in range(n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst

# 4-3. 퀵 정렬

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


# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# print(selection_sort(array))
# print(insert_sort(array))
# print(array)


# 9-1. 소수

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_prime_number2(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


# print(is_prime_number(2**7-1))
# print(is_prime_number2(2**7-1))

def prime_list(n):
    sieve = [False, False] + [True] * (n-1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

# print(prime_list(100))

# 9-2. 투 포인터

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

# print(two_pointer([1, 2, 3, 2, 5], 5))

# 9-3. 구간 합

def interval_sum(lst, query):
    p = [0] * (len(lst) + 1)
    result = [0] * len(query)

    for i, v in enumerate(lst):
        p[i+1] = p[i] + v

    for i, v in enumerate(query):
        result[i] = p[v[1]] - p[v[0]-1]

    return result

# print(interval_sum([10, 20, 30, 40, 50], [(3, 4), (2, 3), (1, 4)]))

# # 10-1. Requests 예시
# import requests

# target = 'http://google.com'
# response = requests.get(url=target)
# print(response.text)  # <!doctype html><html itemscope="" ...


# # 10-4-4. JSON 객체 파일 저장 예시
# import json


# # 사전 자료형(dict) 데이터 선언
# user = {
#     "id": "gildong",
#     "password": "1!2@3#4$",
#     "age": 30,
#     "hobby": ["football", "programming"]
# }

# # JSON 데이터로 변환하는 파일로 저장
# with open("user.json", "w", encoding="utf-8") as file:
#     json.dump(user, file, indent=4)

# # 10-4-6. REST API를 호출하여 회원 정보를 처리하는 예제
# import requests

# # REST API 경로에 접속하여 응답(Response) 데이터 받아오기
# target = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url=target)

# # 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 반환
# data = response.json()

# # 모든 사용자(user) 정보를 확이하며 이름 정보만 삽입
# name_list = []
# for user in data:
#     name_list.append(user['name'])

# print(name_list)
# # ['Leanne Graham', 'Ervin Howell', ... ,'Clementina DuBuque']
