answer = 0
dd = ((-1, 1), (0, 1), (1, 1), (1, 0))

def solution(h, w, n, board):
    global answer, dd
    answer = 0

    for y in range(h):
        for x in range(w):
            # print(board[y][x], end="")
            if board[y][x] == "1":
                for d in dd:
                    check_n(y, x, d, h, w, n, board)
        # print()

    return answer


def check_n(y, x, d, h, w, n, board):
    global answer
    # outofindex가 아니면서 0이면? return
    ny = y - d[0]
    nx = x - d[1]
    if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == "1":
        return

    ny = y + d[0] * n
    nx = x + d[1] * n
    if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == "1":
        return

    cnt = 1
    ny -= d[0]
    nx -= d[1]
    while True:
        if cnt == n:
            answer += 1
            break
        # outofindex면 나가리~
        if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == "1":
            ny -= d[0]
            nx -= d[1]
            cnt += 1
        else:
            break

    return


h, w, n, board = 7, 9, 4, ["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]
h2, w2, n2, board2 = 5, 5, 5, ["11111","11111","11111","11111","11111"]
print(solution(h, w, n, board))
print(solution(h2, w2, n2, board2))
