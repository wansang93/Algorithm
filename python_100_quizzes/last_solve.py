def make_map(row, column, locate_c, obstacle):
    # 메모리 확보
    matrix = [[0 for _ in range(row)] for _ in range(column)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if [i, j] in obstacle:
                matrix[i][j] = 2
            if [i, j] == locate_c:
                matrix[i][j] = 1

    result = padding(matrix, row, column)
    return result


def padding(matrix, row, column):
    # 메모리 확보
    padding_matrix = [[0 for _ in range(row+2)] for _ in range(column+2)]

    for i in range(column+2):
        for j in range(row+2):
            if i in (0, column+1) or j in (0, row+1):
                padding_matrix[i][j] = 2
            else:
                padding_matrix[i][j] = matrix[i-1][j-1]
    
    return padding_matrix

row = 4
column = 5
locate_c = [0, 0]
obstacle = [[0, 1], [1, 1], [2, 3], [1, 3]]

new_map = make_map(row, column, locate_c, obstacle)
for i in range(len(new_map)):
    print(new_map[i])