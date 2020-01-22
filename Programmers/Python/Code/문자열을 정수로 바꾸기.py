# 풀이1
def solution(s):
    answer = 0
    if s[0] == "-":
        answer = - int(s[1:])
    elif s[0] == "+":
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer

# 풀이2
def solution(s):
    answer = 0
    if s[0] == '-':
        answer = -int(s[1:])
    else:
        answer = int(s)
    return answer

# 풀이3
def solution(s):
    answer = int(s)
    return answer