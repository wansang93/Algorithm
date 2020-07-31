T = int(input())
for t in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001

    for _ in range(N):
        start, end = map(int, input().split())
        for i in range(start, end+1):
            bus_stop[i] += 1

    P = int(input())
    answer = []
    for i in range(P):
        answer.append(bus_stop[int(input())])
 
    print(f'#{t}', *answer)
