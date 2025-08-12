# 풀이1 최적화
def solution(n):
    def dfs(row, columns, hills, dales):
        if row == n:
            return 1
        count = 0
        available_positions = (~(columns | hills | dales)) & ((1 << n) - 1)
        while available_positions:
            position = available_positions & -available_positions
            available_positions &= available_positions - 1
            count += dfs(row + 1, columns | position, (hills | position) << 1, (dales | position) >> 1)
        return count

    return dfs(0, 0, 0, 0)


# 풀이2
answer = 0


def is_valid(r, board):
    for i in range(r):
        if board[r] == board[i] or abs(board[r] - board[i]) == r - i:
            return False
    return True


def dfs(r, n, board):
    global answer
    if r == n:
        answer += 1
        return
    
    for c in range(n):
        board[r] = c
        if is_valid(r, board):
            dfs(r+1, n, board)


def solution(n):
    global answer
    board = [-1] * n
    dfs(0, n, board)
    return answer
