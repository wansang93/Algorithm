T = int(input())
for t in range(1, T+1):
    N = int(input())

    income = list(map(int, input().split()))
    average = sum(income) / N
    
    answer = 0
    for i in income:
        if i <= average:
            answer += 1

    print(f'#{t} {answer}')
