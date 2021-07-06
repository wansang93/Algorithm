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
            return p_name

# 풀이3
def solution3(participant, completion):
    temp = 0
    dic = {}
    for i in participant:
        hs = hash(i)
        temp += hs
        dic[hs] = i
    for j in completion:
        temp -= hash(j)
    answer = dic[temp]

    return answer

# 풀이4
from collections import Counter
def solution4(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]

data1 = ["mislav", "stanko", "mislav", "ana"]
data2 = ["stanko", "ana", "mislav"]

print(solution4(data1, data2))
