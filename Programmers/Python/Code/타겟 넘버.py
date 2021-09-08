from collections import deque 

def solution(numbers, target):
    answer = 0
    q = deque([0, 0])
    while q:
        idx, sums = q.popleft()
        if idx == len(numbers):
            if sums == target:
                answer += 1
        else:        
            add = numbers[idx]
            q.append(idx+1, sums+add)
            q.append(idx+1, sums-add)
        
    return answer