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

# # 파트5
# def solution(land):
#     land.insert(0, [0, 0, 0, 0])

#     for i in range(1, len(land)):
#         for j in range(4):
#             first, second, third = [i for i in range(4) if i != j]
#             land[i][j] += max(land[i-1][first], land[i-1][second], land[i-1][third])

#     answer = max(land[len(land)-1])
#     return answer

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# # 파트5 풀이2
# def solution2(land):
#     sum_list = [0]*4
    
#     for row in land:
#         tmp = sum_list.copy()
#         for i in range(4):
#             sum_list[i] = row[i] + max(tmp[:i] + tmp[i+1:])

#     return max(sum_list)

# # 파트 6

# def solution(sticker):

#     if len(sticker) <= 3:
#         return max(sticker)

#     # 첫 스티커 뜯은 경우
#     dp = sticker.copy()
#     dp[1] = dp[0]
#     dp.pop()  # 마지막 스티커는 못뜯어서 빼버림
#     for i in range(2, len(dp)):
#         dp[i] = max(dp[i] + dp[i-2], dp[i-1])

#     # 첫 스티커 뜯지 않은 경우
#     dp2 = sticker.copy()
#     dp2[0] = 0
#     for i in range(2, len(dp2)):
#         dp2[i] = max(dp2[i] + dp2[i-2], dp2[i-1])

#     return max(dp[len(dp)-1], dp2[len(dp2)-1])

# print(solution([14, 6, 5, 11, 3, 9, 2, 10]))

# # 파트 6 풀이2

# def solution(sticker):
#     n = len(sticker)
#     if n <= 3:
#         return max(sticker)
    
#     # select node 0
#     cashe1 = [sticker[0], sticker[0]]
#     for i in range(2, n-1):
#         cashe1_0th = cashe1[1]
#         cashe1_1st = max(cashe1[1], cashe1[0]+sticker[i])
#         cashe1 = [cashe1_0th, cashe1_1st]
    
#     # select node 1
#     cashe2 = [0, sticker[1]]
#     for i in range(2, n):
#         cashe2_0th = cashe2[1]
#         cashe2_1st = max(cashe2[1], cashe2[0]+sticker[i])
#         cashe2 = [cashe2_0th, cashe2_1st]

#     return max(cashe1[1], cashe2[1])  # maximums of cashe1, 2 last values

test = '1'

test[0].upper()

print(test)
