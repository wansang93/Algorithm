# 풀이1
def solution(strings, n):
    nst = []
    answer = []
    for i in strings:
        nst.append(i[n]+i)
    nst.sort()
    for i in nst:
        answer.append(i[1:])

    return answer