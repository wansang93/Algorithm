from itertools import combinations

def solution(orders, course):
    answer = []
    
    for num in course:
        cadi = dict()
        for order in orders:
            for combi in combinations(sorted(order), num):
                menu = "".join(combi)
                if menu in cadi:
                    cadi[menu] += 1
                else:
                    cadi[menu] = 1
        if cadi:
            cnt = max(cadi.values())
            if cnt > 1:
                for k, v in cadi.items():
                    if v == cnt:
                        answer.append(k)

    answer.sort()
    return answer


data1 = (["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
data2 = (["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
data3 = (["XYZ", "XWY", "WXA"], [2,3,4])

print(solution(*data1))
print(solution(*data2))
print(solution(*data3))
