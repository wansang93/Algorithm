def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i, ch in enumerate(name):
        # 위 아래 움직임
        if ord(ch) > ord('M'):
            answer += (ord('Z') - ord(ch) + 1)
        elif ord(ch) <= ord('M'):
            answer += (ord(ch) - ord('A'))

        # 가로 세로 움직임
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, 2 * i + len(name) - next)
    answer += min_move

    return answer

data = 'JAN'
print(solution(data))
