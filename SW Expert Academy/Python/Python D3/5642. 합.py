T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    for i in range(1, N):
        lst[i] = max(lst[i], lst[i]+lst[i-1])
    
    print(f'#{test_case} {max(lst)}')
