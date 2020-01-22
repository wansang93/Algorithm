# 풀이1
def solution(N, stages):
    answer = []
    ss = sorted(stages)
    total = len(ss)
    temp = []
    for i in range(1, N+1):
        if i in ss:
            value = ss.count(i)
            temp.append(value/total)
            total -= value
        else:
            temp.append(0)
    # print(temp)
    for i in range(N):
        pop_idx = temp.index(max(temp))
        answer.append(pop_idx+1)
        temp[pop_idx] = -1

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# sorted(result, key=lambda x : result[x], reverse=True)