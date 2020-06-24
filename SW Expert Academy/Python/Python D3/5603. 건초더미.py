T = int(input())
for t in range(1, T+1):
    N = int(input())

    haystack = [int(input()) for _ in range(N)]
    min_move_count = 0
    
    avg_haystack = sum(haystack) // N
    for i in haystack:
        if i > avg_haystack:
            min_move_count += i - avg_haystack

    print(f'#{t} {min_move_count}')