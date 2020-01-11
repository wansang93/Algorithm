field = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

# field = [] #입력받은 텃밭 리스트
# for i in range(5):
#     field.append(input('텃밭을 입력하세요 :').split(' '))

def check_square(field, x, y, temp):
    is_OK = True
    N = 1
    while is_OK == True:
        sum_tmp = 0
        if 0 <= x+N < len(field[x]) and 0 <= y+N < len(field):  # row와 column가 그 안쪽이고
            for i in range(x, x+N+1):
                for j in range(y, y+N+1):
                    sum_tmp += field[i][j]        
            if sum_tmp == 0:
                N += 1  # N에 1을 추가해서 다시 검색
            else:
                is_OK = False
        else:
            is_OK = False
        if is_OK == False:
            if temp[2] < N-1:  # temp[2] 값과 비교 반복문 횟수가 더 많으면
                temp[0] = x
                temp[1] = y
                temp[2] = N-1
    return temp

def solution(field):
    result = field.copy()  # 텃밭을 가꾼 후 저장된 리스트
    temp = [0, 0, -1]  # [column, row, square_size-1]
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 0:
                temp = check_square(field, i, j, temp)
    print(temp)

    for i in range(temp[0], temp[0]+temp[2]+1):
        for j in range(temp[1], temp[1]+temp[2]+1):
            result[i][j] = '#'

    return result

print(solution(field))