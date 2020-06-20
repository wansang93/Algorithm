T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = []
    for i in range(N):
        farm.append([int(i) for i in input()])

    # middle
    harvest = sum(farm[N//2])

    # upside
    j = N//2
    k = 1
    for i in range(N//2):
        harvest += sum(farm[i][j:j+k])
        j -= 1
        k += 2
    # downside
    j = N//2
    k = 1
    for i in range(N-1, N//2, -1):
        harvest += sum(farm[i][j:j+k])
        j -= 1
        k += 2
    
    print(f'#{t} {harvest}')

