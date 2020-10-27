# x, y = 3, 5
# mylist = [[0] * x for _ in range(y)]

# mylist = {('a', 50), ('b', 30), ('c', 60)}
# sorted(mylist, key=lambda x: x[1])


# list1 = [1, 2, 3, 4, 5]
# list2 = [50, 40, 30, 20, 10]
# map(lambda a, b: a+b, list1, list2)

# import itertools  # 순열과 조합
# import heapq  # 힙 자료구조
# import bisect  # 이진 탐색
# import collections  # 덱, 카운터
# import math  # 수학

# # 1. 표준 라이브러리
# eval('(3+5)*7')  # 56

# # 2. 순열, 조합, 중복순열, 중복조합
# mylist = ['1', '2', 'b', 'a']

# from itertools import permutations  # 순열
# from itertools import combinations  # 조합
# from itertools import product  # 중복순열
# from itertools import combinations_with_replacement  # 중복조합

# print(list(permutations(mylist, 2)))
# print(list(combinations(mylist, 2)))
# print(list(product(mylist, repeat=2)))
# print(list(combinations_with_replacement(mylist, 2)))

# # 3. Count
# from collections import Counter
# counter = Counter(['a', 'a', 'b', 'b', 'a', 'c', 'd', 'c'])
# print(counter['a'])
# print(dict(counter))

# import math

# # 최대 공약수(GCD)
# print(math.gcd(21, 14))

# # 최고 공배수
# def lcm(a, b):
#     return a * b // math.gcd(a, b)
# print(lcm(21, 14))


# def until_one(n, k):
#     count = 0
#     while True:
#         target = (n//k) * k
#         count += n - target
#         n = target
#         if n < k:
#             break        
#         count += 1
#         n //= k
#     return count + n - 1

# def max_num(s):
#     num = int(s[0])
#     for c in s[1:]:
#         i = int(c)
#         if i == 0 or i == 1:
#             num += i
#         else:
#             num *= i
    
#     return num

# def adventurer_guild(l):
#     count = 0
#     mylist = l.sort()
#     people = 0
#     for i in mylist:
#         people += 1
#         if i <= people:
#             people = 0
#             count += 1
    
#     return count

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

