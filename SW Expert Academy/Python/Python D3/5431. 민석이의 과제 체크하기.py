T = int(input())
for t in range(1, T+1):
    # N은 수강생 수, K는 과제 제출자
    N, K = list(map(int, input().split()))
    K_list = list(map(int, input().split()))
    N_list = [i for i in range(1, N+1)]

    non_assignment = set(N_list) - set(K_list)

    print(f'#{t} {" ".join(list(map(str, non_assignment)))}')
