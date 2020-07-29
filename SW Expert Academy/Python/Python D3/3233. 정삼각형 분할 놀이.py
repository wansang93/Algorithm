T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    answer = (A // B) ** 2

    print(f'#{t} {answer}')
