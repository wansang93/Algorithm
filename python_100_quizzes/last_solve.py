# ["12:30", "13:20", "14:13"]
# "12:40"
# 출력
# ['지나갔습니다', '0시간 40분', '1시간 33분']

time_bus = ["12:30", "13:20", "14:13"]
now_time = "12:40"
answer = []

def solution(bus, nowtime):
    nowlist = list(map(int, nowtime.split(':')))
    sub = []
    for time in time_bus:
        time = list(map(int, time.split(':')))
        for i, j in zip(time, nowlist):
            sub.append(i-j)
    print(sub)  # [0, -10, 1, -20, 2, -27]

    for i in range(1, len(sub)+1, 2):
        if sub[i] < 0:
            sub[i] += 60
            sub[i-1] -= 1
        if sub[i-1] < 0:
            answer.append('지나갔습니다.')
        else:
            answer.append('{}시간 {}분'.format(sub[i-1], sub[i]))
    return answer

print(solution(time_bus, now_time))