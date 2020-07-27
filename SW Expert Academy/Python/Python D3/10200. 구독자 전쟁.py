T = int(input())
for t in range(1, T+1):
    N, A, B = map(int, input().split())
    
    minimum = 0 if A+B-N < 0 else A+B-N
    maximum = min(A, B)
    print(f'#{t} {maximum} {minimum}')
