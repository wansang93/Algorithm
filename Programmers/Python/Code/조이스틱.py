def solution(name):
    
    answer = 0
    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    n = len(name)
    min_move = n - 1
    now, nxt = 0, 1
    while now < n and nxt < n:
        while nxt < n and name[nxt] == 'A':
            nxt += 1
        # 왼쪽 갔다가 오른쪽
        min_move = min(min_move, 2 * now + (n - nxt))
        # 오른쪽 갔다가 왼쪽
        min_move = min(min_move, 2 * (n - nxt) + now)
        now = nxt
        nxt += 1

    answer += min_move
    return answer

# def solution(name):
#     answer = 0
#     min_move = len(name) - 1
#     for i, ch in enumerate(name):
#         # 위 아래 움직임
#         if ord(ch) > ord('M'):
#             answer += (ord('Z') - ord(ch) + 1)
#         elif ord(ch) <= ord('M'):
#             answer += (ord(ch) - ord('A'))

#         # 가로 세로 움직임
#         next = i + 1
#         while next < len(name) and name[next] == 'A':
#             next += 1
        
#         min_move = min(min_move, 2 * i + len(name) - next)
#     answer += min_move

#     return answer

data = 'JEROEN'
data2 = 'JAN'
print(solution(data))
print(solution(data2))
