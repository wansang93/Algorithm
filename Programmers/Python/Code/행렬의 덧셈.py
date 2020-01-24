# 풀이1
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])  
        answer.append(tmp)
    return answer

# 풀이2
def solution2(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = []
        for k, l in zip(i, j):
            temp.append(k+l)
        answer.append(temp)
    return answer
