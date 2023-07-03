def dfs(depth):
    global ans
    if depth == time:
        ans = max(ans, int(''.join(lst)))
        return
    
    for i in range(N-1):
        for j in range(i+1, N):
            lst[i], lst[j] = lst[j], lst[i]
            v = ''.join(lst)
            if (v, depth) not in visit:
                visit.add((v, depth))
                dfs(depth+1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for test_case in range(1, T+1):
    num, time = map(int, input().split())
    lst = list(str(num))
    N = len(lst)

    visit = set()
    ans = 0
    dfs(0)

    print(f'#{test_case} {ans}')
