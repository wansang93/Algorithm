# 풀이1
def solution(n, arr1, arr2):
    answer = []
    newlist = []
    for i, j in zip(arr1, arr2):
        t = str(bin(i | j)[2:]).rjust(n, '0')
        newlist.append(t)
    for s in newlist:  # 이부분을 replace를 이용해서 수정바람
        temp =''
        for c in s:
            if c == '0':
                temp += ' '
            elif c =='1':
                temp += '#'
        answer.append(temp)
            
    return answer