def solution(plans):
    _plans = []
    for name, start, play_time in plans:
        h, m = map(int, start.split(":"))
        start = h * 60 + m
        play_time = int(play_time)
        _plans.append([name, start, play_time])
    _plans.sort(key=lambda x: x[1])

    finished = []
    stopped = []
    now = 0
    for name, start, play_time in _plans:
        while stopped and now < start:
            pre_name, pre_play_time = stopped.pop()
            if now + pre_play_time <= start:
                now += pre_play_time
                finished.append(pre_name)
            else:
                stopped.append([pre_name, pre_play_time - (start - now)])
                now = start

        stopped.append((name, play_time))
        now = start

    while stopped:
        finished.append(stopped.pop()[0])

    return finished

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
plans2 = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
print(solution(plans2))
