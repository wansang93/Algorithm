# 풀이1
def solution(priorities, location):
    answer = 1
    while True:
        if priorities[0] == max(priorities):
            if location == 0:
                return answer
            else:
                priorities.pop(0)
                location -= 1
                answer += 1
        else:
            priorities.append(priorities.pop(0))
            location -= 1
        if location < 0:
            location = len(priorities)-1

# 풀이2
def solution2(priorities, location):
    answer = 1
    m = max(priorities)
    while True:
        if priorities[0] == m:
            if location == 0:
                return answer
            else:
                priorities.pop(0)
                m = max(priorities)
                location -= 1
                answer += 1
        else:
            priorities.append(priorities.pop(0))
            location -= 1
        if location < 0:
            location = len(priorities)-1
