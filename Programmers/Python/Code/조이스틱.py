############### 보류 ###############

# test case
'AABAB'
'ABAAB'
# solution1: (~ing)
def solution(name):

    answer = 0  # 바꾼 횟수
    cur = 0  # 현재 커서의 위치
    while True:

        c = ord(name[cur])  # A: 65, M: 77
        if c <= 77:
            answer += c - 65
        else:
            answer += 91 - c

    return answer



print(solution('JEROEN'))  # 56
