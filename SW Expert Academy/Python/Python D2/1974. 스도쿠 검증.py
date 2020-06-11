T = int(input())
for t in range(1, T+1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    answer = 1

    # 가로 검증
    for row in sudoku:
        is_ok = [False] * 10
        for i in row:
            if is_ok[i] == True:
                answer = 0
                break
            else:
                is_ok[i] = True
        if answer == 0:
            break

    # 세로 검증
    if answer == 1:  # 가로 검증 성공시만 실행
        for i in range(len(sudoku)):
            is_ok = [False] * 10
            for j in range(len(sudoku)):
                if is_ok[sudoku[j][i]] == True:
                    answer = 0
                    break
                else:
                    is_ok[sudoku[j][i]] = True
            if answer == 0:
                break
        
    # 3x3 검증
    if answer == 1:  # 가로 세로 검증 성공시만 실행
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                is_ok = [False] * 10
                for m in range(3):
                    for n in range(3):
                        if is_ok[sudoku[i+m][j+n]] == True:
                            answer = 0
                            break
                        else:
                            is_ok[sudoku[i+m][j+n]] = True
                if answer == 0:
                    break
            if answer == 0:
                break                    


    print(f'#{t} {answer}')