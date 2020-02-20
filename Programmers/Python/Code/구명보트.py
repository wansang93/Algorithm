# 풀이1
def solution(people, limit):
    answer = 0
    people = sorted(people)
    first = 0
    end = len(people)-1
    while first <= end:
        if people[end] + people[first] <= limit:
            end -= 1
            first += 1
        else:
            end -= 1        
        answer += 1

    return answer