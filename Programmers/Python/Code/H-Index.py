# 내 풀이
def solution(citations):
    citiations = sorted(citations)
    answer = 0
    l = len(citations)
    for i, citiation in enumerate(citiations):
        if citiation >= l - i:
            answer = max(answer, l-i)

    return answer

# 다른 사람 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


citations = [3, 0, 6, 1, 5]
print(solution(citations))
