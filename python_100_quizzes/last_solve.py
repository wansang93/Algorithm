# ㄱ,ㄴ,ㄷ,ㄹ
# 3

# 출력

# ['ㄱㄴㄷ', 'ㄱㄴㄹ', 'ㄱㄷㄹ', 'ㄴㄷㄹ']
# 4

import math

# mylist = input().split(',')
# mynum = int(input())


def combination(inL, inN):
    newlist = []
    newnum = int(math.factorial(len(inL)) / ((math.factorial(inN)) * math.factorial(len(inL)-inN)))

    for i in range(newnum):
        newlist.append()
    print(newlist)
    print(newnum)

# print(combination(mylist, mynum))

print(combination(['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ'], 4))

# from itertools import permutations # 이 문제에서는 안쓰지만 어떤 것인지 확인해보세요.
# from itertools import combinations

# import itertools

# user_input = input().split(',')
# user_input_int = int(input())

# print(list(itertools.combinations(user_input, 3)))

# print(list(map(''.join, combinations(user_input, user_input_int))))