T = 10
for t in range(1, T+1):
    N = int(input())
    magnets = []
    for i in range(N):
        magnets.append([i for i in input().split()])
    
    amount = 0
    for y in range(N):
        stack = []
        for x in range(N):
            temp = magnets[x][y]
            if not stack and temp == '1':
                stack.append(temp)
            elif stack and temp == '2':
                amount += 1
                stack.pop()

    print(f'#{t} {amount}')
