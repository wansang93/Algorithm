T = int(input())
for t in range(1, T+1):
    scores = list(map(int, input().split()))
    sum_scores = 0
    for i in scores:
        if i < 40:
            sum_scores += 40
        else:
            sum_scores += i

    mean = sum_scores // 5
    print(f'#{t} {mean}')