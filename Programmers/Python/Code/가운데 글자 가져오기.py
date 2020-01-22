# 풀이1
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[(len(s)-1)//2:(len(s))//2+1]
    else:
        answer = s[(len(s)-1)//2]
    return answer

# 풀이2
def solution2(s):
    answer = s[(len(s)-1//2):len(s)//2+1]
    return answer