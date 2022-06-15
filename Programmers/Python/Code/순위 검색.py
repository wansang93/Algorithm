# TODO: 정답 풀이
def solution2(info, query):
    answer = []
    
    return answer


# 시간 초과 풀이
def solution2(info, query):
    answer = []
    
    lst = []
    for i in range(len(info)):
        lst.append(info[i].split())

    for q in query:
        # lang, group, expr, soul, score = q.split("and")
        temp = q.split(" and ")
        lang, group, expr = temp[:3]
        soul, score = temp[-1].split()
        cnt = 0
        for i in range(len(lst)):
            if lang in (lst[i][0], '-') and \
                group in (lst[i][1], '-') and \
                expr in (lst[i][2], '-') and \
                soul in (lst[i][3], '-') and \
                int(score) <= int(lst[i][4]):
                cnt += 1

        answer.append(cnt)
    
    return answer


data1 = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution2(*data1))
