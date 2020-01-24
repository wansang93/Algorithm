# 풀이1
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        tmp = ''
        for c in s:
            if c in skill:
                tmp += c

    is_ok = True
    tmp_index = skill.index(tmp[0])
    for i in range(1, len(tmp)):
        # tmp와 rule을 비교하여 참이면 append('가능')
        if tmp_index < skill.index(tmp[i]):
            tmp_index = skill.index(tmp[i])
        # tmp와 rule을 비교하여 불가능이면 append('불가능')
        else:
            is_ok = False
            break
    if is_ok == True:
        answer += 1
    
    return answer

# 풀이2
def solution2(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        temp = []
        isOK = True
        for s in skills:
            if s in skill:
                temp.append(s)
        
        for i, j in zip(temp, skill):
            if i != j:
                isOK = False
        
        if isOK == True:
            answer += 1
    return answer