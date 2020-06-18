T = int(input())
for t in range(1, T+1):
    memory = input()
    count = 0

    is_one = False
    for i in memory:
        if i == '0':
            if is_one:
                count += 1
                is_one = False

        elif i == '1':
            if not is_one:
                count += 1
                is_one = True

    print(f'#{t} {count}')
