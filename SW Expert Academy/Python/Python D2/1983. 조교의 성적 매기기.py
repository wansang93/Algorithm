T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split(' '))
    for n in range(N):
        midterm, final, assignment = map(int, input().split())
