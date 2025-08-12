# 풀이 2(완탐)
from itertools import product

def solution2(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6):
        for p in product(letters, repeat=i):
            dictionary.append(''.join(p))
    
    dictionary.sort()
    
    return dictionary.index(word) + 1

# 풀이 1(수학)

def solution(word):
    LEN = 5
    letters = ['A', 'E', 'I', 'O', 'U']
    answer = 0

    for idx, ch in enumerate(word):
        weight = (len(letters) ** (LEN - idx) - 1) // (len(letters) - 1)
        answer += letters.index(ch) * weight + 1

    return answer

print(solution("AAAAE"))
