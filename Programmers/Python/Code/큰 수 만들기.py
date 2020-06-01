############### 보류 ###############


# 실패한 풀이1(이유: 런타임 오류)
import itertools

def solution(number, k):
    length = len(number) - k
    print(list(itertools.combinations(number, length)))
    return max(list(map(''.join, list(itertools.combinations(number, length)))))

print(solution('abcd', 3))


# permutation and combination algorithm
'''
permutation algorithm by recursive funciton
https://www.youtube.com/watch?v=hqijNdQTBH8
'''
# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = list(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield list(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield list(pool[i] for i in indices)


# 풀이2(진행 중) 너무나 어렵ㅜㅜ
def solution2(number, k):
    answer = [0] * (len(number) - k)


#   0    0    0
#   4    1    6
#  cur
#   0   1    2    
        
# answer = ''.join(answer)
    return answer

print(solution2('4177252841', 4))
