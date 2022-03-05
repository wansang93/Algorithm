# prefix 2d array를 활용해서 풀면 효율성이 증가할듯


def solution(board, skill):
    answer = 0

    for s in skill:
        stype, r1, c1, r2, c2, degree = s
        if stype == 1:
            degree = -degree

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += degree

    # print(board)

    for row in board:
        for each in row:
            if each > 0:
                answer += 1

    return answer

data1 = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
data11 = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

data2 = [[1,2,3],[4,5,6],[7,8,9]]
data22 = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(data1, data11))
print(solution(data2, data22))
