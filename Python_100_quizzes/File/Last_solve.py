def solution(board, moves):
    score = 0
    stack = []
    while moves:  # 이동에 있는 모든 것을 탐색한다.
        line = len(board)
        m = moves.pop(0)-1  # 이동을 하나 꺼낸다.
        for i in range(line):  # for 꺼낸 숫자의 라인을 위에서 부터 쭉 읽는다.
            cur = board[i][m]  # 커서(공 값)
            if cur == 0:  # 커서가 0이면 라인에 1값을 뺀다. 
                line -= 1  # 라인의 모든 숫자가 0이면 line은 0이된다.
            else:  # 0이 아닌값이 있으면
                if stack != [] and stack[-1] == cur:
                    stack.pop()
                    score += cur * 2
                else:
                    stack.append(cur)
                board[i][m] = 0  # 라인에 공값을 비워둔다.
                break
        # 라인관리
        if line == 0:
            score -= 1

        print(stack)
        print(score)
    return score


board = [[0,0,0,0],[0,1,0,3],[2,5,0,1],[2,4,4,1],[5,1,1,1]]
moves = [1,1,1,1,3,3,3]

print(solution(board, moves))
