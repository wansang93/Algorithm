# # ㄱ,ㄴ,ㄷ,ㄹ
# # 3

# # 출력

# # ['ㄱㄴㄷ', 'ㄱㄴㄹ', 'ㄱㄷㄹ', 'ㄴㄷㄹ']
# # 4

# import math

# # mylist = input().split(',')
# # mynum = int(input())


# def combination(inL, inN):
#     newlist = []
#     newnum = int(math.factorial(len(inL)) / ((math.factorial(inN)) * math.factorial(len(inL)-inN)))

#     for i in range(newnum):
#         newlist.append()
#     print(newlist)
#     print(newnum)

# # print(combination(mylist, mynum))

# print(combination(['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ'], 4))

# 풀이 2

# from itertools import permutations # 이 문제에서는 안쓰지만 어떤 것인지 확인해보세요.
# from itertools import combinations

# import itertools

# user_input = input().split(',')
# user_input_int = int(input())

# print(list(itertools.combinations(user_input, 3)))

# print(list(map(''.join, combinations(user_input, user_input_int))))

# 풀이 3

mylist = input().split(',')
mynum = int(input())

def combination2(arr, r):
    # 1.
    arr = sorted(arr)
    all_list = []
    # 2.
    def generate(chosen):
        if len(chosen) == r:
            # print(chosen)
            all_list.append(''.join(map(str, chosen)))
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    print(all_list)
    print(len(all_list))

combination2(mylist, mynum)