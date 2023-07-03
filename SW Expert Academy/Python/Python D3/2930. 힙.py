import heapq

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    heap = []
    ans = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:
            heapq.heappush(heap, -tmp[1])
        elif tmp[0] == 2:
            if not heap:
                ans.append(-1)
            else:
                ans.append(-heapq.heappop(heap))
    
    print(f'#{test_case}', *ans)
