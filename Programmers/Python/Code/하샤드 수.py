# 풀이1
def solution(x):
    answer = True
    divider = []
    for i in str(x):
        divider.append(int(i))
    
    if x % sum(divider) != 0:
        answer = False
    return answer
    
# 풀이2
def solution2(x):
    answer = True
    t = sum([int(i) for i in str(x)])
    if x % t != 0:
        answer = False
    return answer