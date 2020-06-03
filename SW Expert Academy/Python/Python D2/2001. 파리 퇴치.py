T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [0] * N
    answer = 0
    
    for n in range(N):
        flies[n] = [int(i) for i in input().split()]

    for x in range(N-M+1):
        for y in range(N-M+1):
            temp = 0
            for row in range(M):
                for column in range(M):
                    temp += flies[x+row][y+column]
            if answer < temp:
                answer = temp

    print('#{} {}'.format(t, answer))
