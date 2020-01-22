# 풀이1
def solution(arr):
    answer = []
    
    index = 0
    answer.append(arr[0])
    for i in arr:
        if i != answer[index]:
            answer.append(i)
            index += 1    
    
    return answer

# 풀이2
def solution2(arr):
    answer = [arr[0]]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer

# 풀이3
def solution3(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer