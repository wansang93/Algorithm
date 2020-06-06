# # 파트4
# def solution(board):
#     answer = 0
#     row = len(board)

#     dp = [[0 for _ in range(row)] for i in range(row)]
#     for i in range(row):
#         column = len(board[i])
#         for j in range(column):
#             if board[i][j] == 1:
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#                 answer = max(dp[i][j], answer)

#     return answer

# 파트5
def solution(land):
    land.insert(0, [0, 0, 0, 0])

    for i in range(1, len(land)):
        for j in range(4):
            first, second, third = [i for i in range(4) if i != j]
            land[i][j] += max(land[i-1][first], land[i-1][second], land[i-1][third])

    answer = max(land[len(land)-1])
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# 파트5 풀이2
def solution2(land):
    sum_list = [0]*4
    
    for row in land:
        tmp = sum_list.copy()
        for i in range(4):
            sum_list[i] = row[i] + max(tmp[:i] + tmp[i+1:])

    return max(sum_list)