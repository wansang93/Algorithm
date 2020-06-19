for t in range(1, 11):
    T = int(input())
    
    # row, column
    N, M = 100, 100
    
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    max_value = 0
    
    # check vertical
    for x in range(N):
        temp = 0
        for y in range(M):
            temp += matrix[x][y]
        if max_value < temp:
            max_value = temp

    # check horizon
    for y in range(M):
        temp = 0
        for x in range(N):
            temp += matrix[x][y]
        if max_value < temp:
            max_value = temp

    # diagonal left to right
    temp1 = 0
    # diagonal right to left
    temp2 = 0
    for i in range(M):
        temp1 += matrix[i][i]
        temp2 += matrix[N-1-i][i]
    if max_value < temp1:
        max_value = temp1
    if max_value < temp2:
        max_value = temp2

    print(f'#{t} {max_value}')
