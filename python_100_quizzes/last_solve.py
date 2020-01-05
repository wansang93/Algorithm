# 1. 1  → (1)
# 2. 11 → (1이 1개)
# 3. 12 → (1이 2개)
# 4. 1121 → (1이 1개 2가 1개)
# 5. 1321 → (1이 3개 2가 1개)
# 6. 122131 → (1이 2개 2가 1개 3이 1개)
# 7. 132231 → (1이 3개 2가 2개 3이 1개)

n = int(input())


def solution(n):
    result = [1]
    if n < 2:
        return '1'
    for _ in range(1, n):
        newresult = []    
        for j in range(1, max(result)+1):
            if result.count(j) > 0:
                newresult.append(j)
                newresult.append(result.count(j))
        result = newresult
    
    return ''.join(map(str, result))

print(solution(n))


# 풀이85-2


def solution2(n):
    answer='1'
    if n == 1:
        return answer
    for _ in range(1,n):
        answer = rule(answer)
    return answer


def rule(n):
    num_l = max([int(i) for i in n])
    d = [str(i)+str(str(n).count(str(i))) for i in range(1,num_l+1)]
    return ''.join(d)


print(solution2(n))