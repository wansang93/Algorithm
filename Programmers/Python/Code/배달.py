from collections import deque


def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    for i, j, cost in road:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    answer = 0
    
    q = deque()
    q.append((1, 0))
    inf = int(1e10)
    # 핵심 메모리
    table = [inf]*(N+1)
    table[1] = 0
    
    while q:
        temp = q.popleft()
        print(temp)
        start_point = temp[0]
        cost = temp[1]

        for i in graph[start_point]:
            end_point, new_cost = i[0], i[1]
            # 핵심 코드
            if cost + new_cost <= K and cost + new_cost < table[end_point]:
                table[end_point] = cost + new_cost
                q.append((end_point, cost+new_cost))

    # print(table)
    for i in table:
        if i != inf:
            answer += 1
            
    return answer

N = 6
K = 4
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]

print(solution(N, road, K))
