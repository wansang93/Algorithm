def solution(n):
    answer = 0
    for i in range(1, n+1):
        j = i
        temp = j
        while True:
            j += 1
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
            else:
                temp += j
    return answer
