def solution(k, m, score):
    lst = [0] * (k + 1)
    for s in score:
        lst[s] += 1

    answer = 0
    for i in range(k, 0, -1):
        if lst[i] >= m:
            answer += (lst[i] // m) * i
        lst[i-1] += lst[i] % m

    return answer * m

data = 	[1, 2, 3, 1, 2, 3, 1]
data2 = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

print(solution(3, 4, data))
print(solution(4, 3, data2))
