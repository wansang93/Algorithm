T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    
    answer = a + b

    print(f'#{t} {answer}')