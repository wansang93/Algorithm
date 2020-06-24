T = int(input())
for t in range(1, T+1):
    D, H, M = map(int, input().split())
    wating_time = 0

    by_11D_11H_11M = 11 * 24 * 60 + 11 * 60 + 11
    realized = D * 24 * 60 + H * 60 + M
    wating_time = realized - by_11D_11H_11M

    if wating_time < 0:
        wating_time = -1

    print(f'#{t} {wating_time}')