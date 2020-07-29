T = int(input())
for t in range(1, T+1):
    people = list(map(int, input()))

    answer = 0
    now_applause = 0
    for idx, num in enumerate(people):
        now_applause += num
        if now_applause < idx+1:
            answer += 1
            now_applause += 1

    print(f'#{t} {answer}')