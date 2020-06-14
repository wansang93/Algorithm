T = int(input())
for t in range(1, T+1):
    N = input()
    answer = 'Odd'
    if int(N[-1]) % 2 == 0:
        answer = 'Even'

    print(f'#{t} {answer}')