# 풀이1
# 이 방법은 효율성에서 에러가 발생함으로 heapq를 이용해야된다.
def solution(scoville, K):
    answer = 0
    mylist = sorted(scoville)
    least = min(mylist)
    while True:
        if len(mylist) <= 1:
            if mylist[0] < K:
                return -1
            else:
                return answer
        if least >= K:
            break
        else:
            a = mylist.pop(0)
            b = mylist.pop(0)
            mylist.append(a + (b * 2))
            mylist.sort()
            least = min(mylist)
            answer += 1
    return answer

# 풀이2
import heapq as hq

def solution2(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

print(solution2([1, 2, 3, 9, 10, 12], 7))

# heapq library documents in english
# https://docs.python.org/3/library/heapq.html

# 힙큐 관련 라이브러리 설명서
# https://python.flowdas.com/library/heapq.html