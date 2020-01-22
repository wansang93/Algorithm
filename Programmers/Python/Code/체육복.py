# 풀이1
def solution(n, lost, reserve):
    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))
    answer = n - len(set_lost)

    while set_reserve:
        if set_reserve[0]-1 in set_lost:
            set_lost.remove(set_reserve[0]-1)
            answer += 1
        elif set_reserve[0]+1 in set_lost:
            set_lost.remove(set_reserve[0]+1)
            answer += 1
        set_reserve.pop(0)
    return answer

# 풀이2
def solution2(n, lost, reserve):
    new_lost = [i for i in lost if i not in reserve]
    new_reserve = [j for j in reserve if j not in lost]
    answer = n - len(new_lost)
    
    for i in new_lost:
        if i-1 in new_reserve:
            new_reserve.remove(i-1)
            answer += 1
            continue
        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
            answer += 1
    
    return answer