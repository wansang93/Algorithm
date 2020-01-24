# 풀이1
def solution(num):
    answer = 0
    count = 0
    tmp = num
    while True:
        if tmp == 1:
            answer = count
            break
        if count == 500:
            answer = -1
            break
        if tmp % 2 == 0:
            tmp /= 2
        else:
            tmp = tmp * 3 + 1

        count += 1
        
    return answer

# 풀이2
def solution2(num):
    answer = 0
    while True:
        if num == 1 or answer > 500:
            break
        elif num % 2 == 0:
            num /= 2
            answer += 1
        else:
            num *= 3
            num += 1
            answer += 1
    if answer > 500:
        answer = -1
    return answer