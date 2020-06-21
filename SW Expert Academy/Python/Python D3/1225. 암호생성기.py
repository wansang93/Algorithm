for t in range(1, 11):
    T = int(input())
    passwords = list(map(int, input().split()))

    cur = 0
    cycle = 1
    while True:
        passwords[cur] -= cycle
        if passwords[cur] <= 0:
            passwords[cur] = 0
            break
        
        cycle += 1
        if cycle > 5:
            cycle = 1

        cur += 1
        if cur > 7:
            cur = 0

    passwords = passwords[cur:]+passwords[:cur]
    passwords.pop(0)
    passwords.append(0)

    answer = ' '.join(map(str, passwords))
    print(f'#{t} {answer}')