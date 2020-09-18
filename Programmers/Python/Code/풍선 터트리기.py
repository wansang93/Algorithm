def solution(a):
    answer = 1
    len_a = len(a)

    min_value = a[0]
    min_index = 0
    for i in range(len_a):
        if min_value > a[i]:
            min_index = i
            min_value = a[i]

    # min_index 전까지 answer 구하기
    min_value = a[0]
    for i in range(min_index):
        if min_value >= a[i]:
            min_value = a[i]
            answer += 1

    # 뒤에서부터 min_index 전까지 answer 구하기
    min_value = a[-1]
    for i in range(len_a-1, min_index, -1):
        if min_value >= a[i]:
            min_value = a[i]
            answer += 1
        
    return answer

# 다른 사람 풀이
def solution2(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        i = 1
        while m != M:
            if m >= a[i]:
                m = a[i]
                answer += 1
            i += 1
        a.reverse()
    return answer