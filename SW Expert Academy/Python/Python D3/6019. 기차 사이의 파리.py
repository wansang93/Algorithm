T = int(input())
for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    
    answer = D * F / (A+B)
    print(f'#{t} {answer}')