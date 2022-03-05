def solution(id_list, report, k):
    answer = []
    id_report_cnt = {i: 0 for i in id_list}
    who_report_id = {i: [] for i in id_list}

    for r in report:
        a, b = r.split()
        if b not in who_report_id[a]:
            who_report_id[a].append(b)
            id_report_cnt[b] += 1

    ban_list = []
    for i in id_report_cnt:
        if id_report_cnt[i] >= k:
            ban_list.append(i)

    for i in id_list:
        temp = 0
        for j in who_report_id[i]:
            if j in ban_list:
                temp += 1
        answer.append(temp)

    return answer

data1 = ["muzi", "frodo", "apeach", "neo"]
data11 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
data111 = 2

data2 = ["con", "ryan"]
data22 = ["ryan con", "ryan con", "ryan con", "ryan con"]	
data222 = 3

print(solution(data1, data11, data111))  # [2,1,1,0]
print(solution(data2, data22, data222))  # [0,0]
