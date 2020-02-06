# 풀이1
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        count = 0
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            count += 1
        answer.append(count)
    answer.append(0)
    return answer

# 풀이2
def solution2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer