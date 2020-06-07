def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if basket != [] and board[j][i-1] == basket[-1]:
                    answer += 2
                    basket.pop(-1)
                else:
                    basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer
