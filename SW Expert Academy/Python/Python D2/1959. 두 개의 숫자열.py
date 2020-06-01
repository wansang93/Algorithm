T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    maximum = -999999999

    if len(Ai) > len(Bj):
        Ai, Bj = Bj, Ai
    
    for i in range(len(Bj)-len(Ai)+1):
        temp = 0
        for j in range(len(Ai)):
            temp += Ai[j] * Bj[j+i]
        if temp > maximum:
            maximum = temp

    print('#{} {}'.format(t, maximum))