T = 10
for t in range(1, T+1):
    N = int(input())
    cipher = list(input().split())
    commands_number = int(input())
    commands = list(input().split())

    cur = 0
    for _ in range(commands_number):
        if commands[cur] == 'I':
            x, y = map(int, (commands[cur+1], commands[cur+2]))
            s = commands[cur+3:cur+3+y]
            for c in s:
                cipher.insert(x, c)
                x += 1
            cur += y + 3

        elif commands[cur] == 'D':
            x, y = map(int, (commands[cur+1], commands[cur+2]))
            for _ in range(y):
                cipher.pop(x)
            cur += 3
            
    print(f'#{t} {" ".join(cipher[:10])}')