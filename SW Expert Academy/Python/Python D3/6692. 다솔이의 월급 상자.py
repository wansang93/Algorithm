T = int(input())
for x in range(1, T+1):
    N = int(input())
    expected_value = 0

    for i in range(N):
        p, wage = input().split()
        expected_value += float(p) * int(wage)

    print(f'#{x} {expected_value:.6f}')