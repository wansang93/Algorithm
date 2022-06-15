import re

def solution(new_id):
    result = new_id.lower()
    result = re.sub('[^a-z0-9\\.\\-\\_]', '', result)
    result = re.sub('\\.+' ,'.', result)
    if result.startswith('.'):
        result = result[1:]
    if result.endswith('.'):
        result = result[:-1]
    if not result:
        result = 'a'
    if len(result) >= 16:
        result = result[:15]
        if result.endswith('.'):
            result = result[:-1]
    if len(result) <= 1:
        result += result[-1] * 2
    elif len(result) == 2:
        result += result[-1]

    return result


# 2번째 풀이
def solution2(new_id):
    answer = new_id
    
    # 1단계
    answer = new_id.lower()
    # 2단계
    temp = []
    for c in answer:
        if c.islower() or c.isdecimal() or c in ("-", "_", "."):
            temp.append(c)
    answer = "".join(temp)
    # 3단계
    while '..' in answer:
        answer = answer.replace("..", ".")
    # 4단계
    if answer.startswith("."):
        answer = answer[1:]
    if answer.endswith("."):
        answer = answer[:-1]
    # 5단계
    if answer == "":
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith("."):
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]
    
    return answer