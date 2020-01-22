# 풀이1
def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if answer == []:
        answer = [-1]
    return answer

# 풀이2
def solution2(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if not answer:
        answer.append(-1)
    return answer