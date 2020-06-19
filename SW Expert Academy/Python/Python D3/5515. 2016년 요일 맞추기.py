T = int(input())
for t in range(1, T+1):
    m, d = map(int, input().split())
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    past_days = d + sum(days[:m]) - 1
    date = (past_days + 4) % 7

    print(f'#{t} {date}')
