# 풀이1
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = []
        start, end, where = commands[i]
        temp = sorted(array[start-1:end])
        answer.append(temp[where-1])
    
    return answer

# 풀이1 개선
def solution2(array, commands):
    answer = []
    for li in commands:
        temp = []
        start, end, where = li
        temp = sorted(array[start-1:end])
        answer.append(temp[where-1])
    return answer


# 풀이2(풀이1 개선의 개선) 다른사람 풀이
def solution3(array, commands):
    answer = []

    for i, j, k in commands:
        a = sorted(array[i-1:j])
        print(a)
        answer.append(a[k-1])

    return answer