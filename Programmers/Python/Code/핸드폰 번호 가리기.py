# 풀이1
def solution(phone_number):
    answer = ''
    for _ in range(len(phone_number)-4):
        answer += "*"
    answer += phone_number[-4:]
    return answer

# 풀이2
def solution2(phone_number):
    answer = len(phone_number[:-4]) * '*'
    answer += phone_number[-4:]
    return answer