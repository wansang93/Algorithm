T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = sorted(list(map(int, input().split())))
    
    answer = 'Impossible'
    for nums, time in enumerate(customers):
        if time // M * K < nums+1:  # 만든 갯수 < 먹은 갯수
            break
    else:
        answer = 'Possible'

    print(f'#{t} {answer}')