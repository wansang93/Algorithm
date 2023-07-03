T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    s1 = N * (N+1) // 2
    s2 = s1 * 2 - N
    s3 = s1 * 2
    print(f'#{test_case} {s1} {s2} {s3}')
