# 풀이1
def solution(arrangement):
    arrangement = list(arrangement)
    answer = 0
    bong = 0
    while arrangement:
        if arrangement[0] == '(':
            bong += 1
            arrangement.pop(0)
            if arrangement[0] == ')':
                bong -= 1
                answer += bong
                arrangement.pop(0)
        else:
            bong -= 1
            answer += 1
            arrangement.pop(0)
    return answer