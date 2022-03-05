month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

def solution(purchase):
    global month
    # 365일 배열 생성
    all_day = [0] * (365+1)
    # 파싱
    for pur in purchase:
        date, cost = pur.split()
        _, M, D = map(int, date.split('/'))
        now_day = sum(month[:M]) + D
        # 날짜 + (날짜+30)까지 금액 추가
        for i in range(30):
            if now_day + i > 365:
                break
            all_day[now_day+i] += int(cost)

    bronze, silver, gold, platinum, diamond = [0, 0, 0, 0, 0]
    for c in all_day[1:]:
        if 0 <= c < 10000:
            bronze += 1
        elif 10000 <= c < 20000:
            silver += 1
        elif 20000 <= c < 50000:
            gold += 1
        elif 50000 <= c < 100000:
            platinum += 1
        elif 100000 <= c:
            diamond += 1

    return [bronze, silver, gold, platinum, diamond]

data = ["2019/01/31 5000", "2019/01/20 15000", "2019/02/09 90000"]
data2 = ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]
data3 = ""
print(solution(data))
print(solution(data2))
