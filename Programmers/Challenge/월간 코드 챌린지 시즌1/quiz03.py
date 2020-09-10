def solution(a):
    answer = 1
    len_a = len(a)

    # min 값 구하기
    min_index = 0
    min_value = a[0]
    for i in range(len(a)):
        if a[i] < min_value:
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

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
