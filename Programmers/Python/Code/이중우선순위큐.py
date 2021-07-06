# 풀이1
import heapq

def solution(operations):
    heap = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(heap, num)
        elif op == 'D':
            if heap:
                heapq.heapify(heap)
                if num == -1:  # 최솟값 삭제
                    heapq.heappop(heap)
                elif num == 1:  # 최댓값 삭제
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
    
    answer = [0, 0]
    if heap:
        answer = [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]

    return answer


# 풀이2
import heapq
def solution(operations):
    heap = []
    max_heap = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-num, num))

        elif op == 'D':
            if num == 1 and max_heap:
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif num == -1 and max_heap:
                min_value = heapq.heappop(heap)
                max_heap.remove((-min_value, min_value))
    
    answer = [0, 0]
    if heap:
        answer = [max(heap), min(heap)]

    return answer


data = ["I 7","I 5","I -5","D -1"]
print(solution(data))



'''
iterable = [6,1,7,9,3,5,4]
selectCount = 3
largests = heapq.nlargest(selectCount, iterable)
print(largests)
# [9, 7, 6]
'''