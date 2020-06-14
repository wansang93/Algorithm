for t in range(1, 11):
    N = int(input())
    matrix = []
    for i in range(8):
        matrix.append(list(input()))
    count = 0

    # 가로 회문
    for i in range(8):
        for j in range(8-N+1):
            temp1 = matrix[i][j:j+N]
            if temp1 == list(reversed(temp1)):
                count += 1
            # print(i, j, temp1, count)

    # 세로 회문
    for i in range(8-N+1):
        for j in range(8):
            temp2 = []
            for k in range(N):
                temp2.append(matrix[i+k][j])
            if temp2 == list(reversed(temp2)):
                count += 1
            # print(i, j, temp2, count)
            
    print(f'#{t} {count}')