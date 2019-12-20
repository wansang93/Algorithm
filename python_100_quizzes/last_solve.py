# 입력
# 탑 = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
# 규칙 = "ABD"

# 출력
# ["가능","불가능","가능","가능]

tower = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]  # input().split()
rule = "ABD"  # input()
availability = []

for s in tower:
    tmp = ''
    for c in s:
        if c in rule:
            tmp += c
    
    is_ok = True
    tmp_index = rule.index(tmp[0])
    for i in range(1, len(tmp)):
        # tmp와 rule을 비교하여 참이면 append('가능')
        if tmp_index < rule.index(tmp[i]):
            tmp_index = rule.index(tmp[i])
        # tmp와 rule을 비교하여 불가능이면 append('불가능')
        else:
            is_ok = False
            break
    if is_ok == True:
        availability.append('가능')
    else:
        availability.append('불가능')

print(availability)