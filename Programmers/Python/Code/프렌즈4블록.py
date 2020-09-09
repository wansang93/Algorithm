def is_break(y, x, board):
    if board[y][x] != '0' and board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1]:
        return True
    else:
        return False

def solution(m, n, board):
    answer = 0

    board = [[c for c in x] for x in board]

    while True:
        break_list = []

        # check break_block
        for y in range(m-1):
            for x in range(n-1):
                if is_break(y, x, board):
                    break_list.append((y, x))
                    break_list.append((y, x+1))
                    break_list.append((y+1, x))
                    break_list.append((y+1, x+1))
                    
        break_list = list(set(break_list))

        # nothing to break -> return answer
        if not break_list:
            return answer

        # change to break block
        for break_block in break_list:
            y, x = break_block[0], break_block[1]
            board[y][x] = '0'
            answer += 1

        # change board state
        for x in range(n):
            for y in range(m-1, -1, -1):
                if board[y][x] == '0':
                    for k in range(y-1, -1, -1):
                        if board[k][x] != '0':
                            board[y][x] = board[k][x]
                            board[k][x] = '0'
                            break
                    else:
                        break
