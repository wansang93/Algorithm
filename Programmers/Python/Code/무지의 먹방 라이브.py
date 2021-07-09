import heapq
def solution(food_times, k):
    answer = 0

    # 예외 처리
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐 구현!
    heap = []
    for i, v in enumerate(food_times):
        heap.append([v, i])
    heapq.heapify(heap)


    # 조건?
    l = len(heap)
    previous = 0
    while True:
        v = heap[0][0]
        diff = (v - previous) * l
        # 조건 만족
        if k >= diff:
            heapq.heappop(heap)
            k -= diff
            l -= 1
            previous = v
        else:
            break
    heap.sort(key=lambda x: x[1])
    which = k % l
    answer = heap[which][1] + 1

    return answer


data = [3, 1, 2]
k = 5
print(solution(data, k))
