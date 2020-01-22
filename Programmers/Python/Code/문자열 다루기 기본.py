# 풀이1
def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == 1:
            answer = True
    
    return answer

# 풀이2
def solution2(s):
    answer = False
    if len(s) in (4, 6) and s.isdigit():
        answer = True
    return answer