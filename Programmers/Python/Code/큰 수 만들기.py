# 풀이 1(스택을 이용)
def solution(number, k):
    answer = []
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    
    answer = ''.join(answer[:len(answer)-k])

    return answer


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

