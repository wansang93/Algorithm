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

def move(matrix, movement):
    # 캐릭터가 어디있는지 찾고
    locate_c = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if 1 == matrix[i][j]:
                print([i, j], '에서 ', end='')
                locate_c.extend([i, j])
                matrix[i][j] = 0
                break
    # 맵에서 이동시킨다.
    # movement(up: 1, down: 2, left: 3, right: 4)
    for i in movement:
        if i == 1 and matrix[locate_c[0]-1][locate_c[1]] == 0:
            locate_c[0] -= 1
        elif i == 2 and matrix[locate_c[0]+1][locate_c[1]] == 0:
            locate_c[0] += 1
        elif i == 3 and matrix[locate_c[0]][locate_c[1]-1] == 0:
            locate_c[1] -= 1
        elif i == 4 and matrix[locate_c[0]][locate_c[1]+1] == 0:
            locate_c[1] += 1

    print(locate_c, '로 이동')
    matrix[locate_c[0]][locate_c[1]] = 1

    return matrix

row = 4
column = 5
locate_c = [0, 0]
obstacle = [[0, 1], [1, 1], [2, 3], [1, 3]]


new_map = make_map(row, column, locate_c, obstacle)

for i in range(len(new_map)):
    print(new_map[i])

# movement(up: 1, down: 2, left: 3, right: 4)


# movement = [2, 2, 2, 4, 4, 4]
# new_map2 = move(new_map, movement)

# for i in range(len(new_map2)):
#     print(new_map[i])


def move2(world_map, moving):
    x,y = 0,0
    for i,m in enumerate(world_map):
        if 1 in m:
            x,y = m.index(1),i
    world_map[y][x] = 0
    for i in moving:
        if i==1 and world_map[y-1][x]!=2:
            y-=1
            
        elif i==2 and world_map[y+1][x]!=2:
            y+=1
            
        elif i==3 and world_map[y][x-1]!=2:
            x-=1
            
        elif i==4 and world_map[y][x+1]!=2:
            x+=1
    world_map[y][x] = 1
    print('#' * 20)
    for i in world_map:
        print(i)
    return [x,y]

movement = [2, 2, 2, 4, 4, 4]
new_map2 = move2(new_map, movement)
