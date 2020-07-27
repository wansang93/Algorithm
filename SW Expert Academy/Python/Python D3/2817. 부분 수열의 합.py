answer = 0
def solve(idx, sums):
    global answer
    if idx >= N:
        return
    now_sum = sums + A[idx]
    if now_sum == K:
        answer += 1
    
    solve(idx+1, sums)
    solve(idx+1, now_sum)

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    solve(0, 0)
    print(f'#{t} {answer}')
    answer = 0
