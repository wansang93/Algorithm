# 입력
# 탑 = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
# 규칙 = "ABD"

# 출력
# ["가능","불가능","가능","가능]

tower = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]  # input().split()
rule = "ABD"  # input()
availability = []

for s in tower:
    for c in s:
        if c in rule:
            print(c)


print(availability)