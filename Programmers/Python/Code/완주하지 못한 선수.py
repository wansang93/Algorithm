# 풀이1
def solution(participant, completion):
    answer = ''
    for i, j in zip(sorted(participant) ,sorted(completion)):
        if i != j:
            answer = i
    if answer == '':
        answer = sorted(participant)[-1]
    return answer

# 풀이2
def solution2(participant, completion):
    completion.append("z" * 20)
    for p_name, c_name in zip(sorted(participant), sorted(completion)):
        if p_name != c_name:
            return(p_name)