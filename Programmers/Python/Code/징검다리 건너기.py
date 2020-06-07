# 정확성 테스트: 100%
# 효율성 테스트: 0% (새로운 탐색방법 공부하기)
def solution(stones, k):
    answer = 0
    while True:
        count = 0
        for i in range(len(stones)):
            if stones[i] == 0:
                count += 1
                if count >= k:
                    return answer
            elif stones[i] > 0:
                stones[i] -= 1
                count = 0
        answer += 1

    return answer