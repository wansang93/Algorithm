# 풀이1: using a for loop
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        i = i.capitalize()
        answer += i + ' '
    return answer[:-1]


# 풀이2: using list comprehension
def solution2(s):
    answer = ' '.join([i.capitalize() for i in s.lower().split(' ')])   
    return answer