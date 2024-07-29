def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    sum_ = sum1 + sum2
    if sum_ % 2 == 1:
        return -1
    
    combine_lst = queue1 + queue2
    target_sum = sum_ // 2
    s, e = 0, len(queue1)
    answer = 0
    while s < len(combine_lst) and e < len(combine_lst):
        if sum1 == target_sum:
            return answer
        if sum1 > target_sum:
            sum1 -= combine_lst[s]
            s += 1
        else:
            sum1 += combine_lst[e]
            e += 1
        
        answer += 1
    
    return -1
