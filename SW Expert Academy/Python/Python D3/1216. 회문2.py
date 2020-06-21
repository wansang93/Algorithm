for t in range(1, 11):
    T = int(input())
    
    # row, column
    N, M = 100, 100
    
    matrix = []
    for i in range(N):
        matrix.append([c for c in input()])
    max_value = 1
    
    # check vertical
    for x in range(N):
        for y in range(M):
            temp = ''
            for k in range(M-y):
                temp += matrix[x][y+k]

            while max_value < len(temp):
                if temp == temp[::-1]:
                    if max_value < len(temp):
                        max_value = len(temp)
                        break
                else:
                    temp = temp[:-1]

    # check horizon
    for y in range(M):
        for x in range(N):
            temp = ''
            for k in range(N-x):
                temp += matrix[x+k][y]

            while max_value < len(temp):
                if temp == temp[::-1]:
                    if max_value < len(temp):
                        max_value = len(temp)
                        break
                else:
                    temp = temp[:-1]

    print(f'#{t} {max_value}')
