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


# 간단하게 짜기
def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# print(selection_sort(array))
# print(insert_sort(array))
# print(quick_sort(array, 0, len(array)-1))
# print(quick_sort2(array))
# print(array)


# 4-4. 계수 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

# 출력
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')


# 4-4-1. 예제 문제
n, k = 5, 3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# print(sum(a))  # 26

# 5-1. 이진 탐색 재귀적 구현
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


# n, target = 10, 7
# array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# result = binary_search2(array, target, 0, n-1)
# if result == None:
#     print(-1)
# else:
#     print(result)  # 3


# 5-1-1. 떡볶이 떡 만들기
def solution(array, start, end, M):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in array:
            if x > mid:
                total += x - mid
        if total < M:
            end = mid - 1
        else:
            result = mid 
            start = mid + 1

    return result

# N, M = 4, 6
# array = [19, 15, 10, 17]
# print(solution(array, 0, max(array), M))

# 5-1-2. 정렬된 배열에서 특정 수의 갯수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = 7, 2
array = [1, 1, 2, 2, 2, 2, 3]

# count = count_by_range(array, x, x)
# if count == 0:
#     print(-1)
# else:
#     print(count)  # 4


# 6-2. 개미 전사
def ant_warriors(lst):
    N = len(lst)
    d = [0] * N
    d[0] = lst[0]
    d[1] = max(lst[0], lst[1])
    for i in range(2, N):
        d[i] = max(d[i-1], d[i-2] + lst[i])

    # print(d)
    return d[N-1]

# lst = [1, 2, 3, 4, 5, 3, 0, 3]
# print(ant_warriors(lst))

# 6-3. 1로 만들기
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

# 6-4. 효율적인 화폐 구성
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

# data = [2, 3]
# m = 12
# print(money_solution(data, m))  # 4

# 6-5. 금광
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

# 6-6. 병사 배치하기(LIS 응용)
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

# print(deploy_soldiers(7, [4, 2, 5, 8, 4, 11, 15]))

# 7-1. 다익스트라 알고리즘 간단 구현
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



# INF = int(1e9)  # 10억

# # n: 노드의 갯수
# # m: 간선의 갯수
# n, m = map(int, input().split())
# start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

# # 모든 간선 정보 입력받기
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))


# dijkstra2(start)
# print(distance)
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
[Output Example 1]
0
2
3
7
INFINITY
'''


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


# INF = int(1e9)  # 10억

# # n: 노드의 갯수
# # m: 간선의 갯수
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)

# # 모든 간선 정보 입력받기
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))


# print(graph)
# dijkstra(start)
# print(distance)

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

# print(interval_sum([10, 20, 30, 40, 50], [(3, 4), (2, 3), (1, 4)]))  # [70, 50, 100]

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
