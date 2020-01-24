# 풀이1
def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
    else:
        min = arr[0]
        index = 0
        for idx, value in enumerate(arr):
            if value < min:
                min = value
                index = idx
        answer = arr
        answer.pop(index)
                
    return answer

# 풀이2
def solution2(arr):
    m = min(arr)
    arr.remove(m)
    if arr == []:
        answer = [-1]
    else:
        answer = arr
    return answer