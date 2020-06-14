for i in range(10):
    t = input()
    N, M = map(int, input().split())
    answer = N ** M

    print(f'#{t} {answer}')