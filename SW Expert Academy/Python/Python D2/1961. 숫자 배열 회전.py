# 문제 설명
# 문제 이해가 안된 나에게 다시 설명한다면
'''
1 2 3
4 5 6
7 8 9 라는 배열이 있을 때
90도 회전하면
7 4 1
8 5 2
9 6 3
즉, (741, 862, 963)이다. 세로로 적으면
741
862
963
이다.

마찬가지로 180도 270도 회전하면
(987 654 321)
(369 258 147)
이다.

이 세 경우를 세로로 적으면 정답과 같이 된다.
741 987 369
852 654 258
963 321 147
'''

def rotate90(matrix):
    rotation_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            rotation_matrix[y][N-1-x] = matrix[x][y]
    
    return rotation_matrix


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(input().split()))

    matrix = rotate90(matrix)  # rotate90
    matrix2 = rotate90(matrix)  # rotate180
    matrix3 = rotate90(matrix2)  # rotate270

    print(f'#{t}')
    for i in range(N):
        print(''.join(matrix[i]), ''.join(matrix2[i]), ''.join(matrix3[i]))