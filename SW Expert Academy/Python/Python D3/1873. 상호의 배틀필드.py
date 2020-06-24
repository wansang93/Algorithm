T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    field = [[c for c in input()] for _ in range(H)]
    N = int(input())
    string = input()

    # tank_location
    h, w = 0, 0
    for y in range(H):
        for x in range(W):
            if field[y][x] in ['^', 'v', '<', '>']:
                h, w = y, x
                break
        else:
            continue
        break

    for c in string:
        # shell_location
        if c == 'S':
            shell_h, shell_w = h, w
            new_h, new_w = 0, 0
            if field[h][w] == '^':
                new_h, new_w = -1, 0
            elif field[h][w] == 'v':
                new_h, new_w = 1, 0
            elif field[h][w] == '<':
                new_h, new_w = 0, -1
            elif field[h][w] == '>':
                new_h, new_w = 0, 1
            while True:
                shell_h += new_h
                shell_w += new_w
                # 범위에 벗어나면 종료
                if shell_h < 0 or shell_h >= H or shell_w < 0 or shell_w >= W:
                    break
                # 강철을 만나면 종료
                elif field[shell_h][shell_w] == '#':
                    break
                # 벽돌을 만나면 평지화 하고 종료
                elif field[shell_h][shell_w] == '*':
                    field[shell_h][shell_w] = '.'
                    break

        # tank_move
        else:
            # 방향전환 및 새 커서 설정
            new_h, new_w = h, w
            if c == 'U':
                field[h][w] = '^'
                new_h -= 1
            elif c == 'D':
                field[h][w] = 'v'
                new_h += 1
            elif c == 'L':
                field[h][w] = '<'
                new_w -= 1
            elif c == 'R':
                field[h][w] = '>'
                new_w += 1
            # 이동이 가능한지 체크
            if 0 <= new_h < H and 0 <= new_w < W and field[new_h][new_w] == '.':
                field[new_h][new_w] = field[h][w]
                field[h][w] = '.'
                h, w = new_h, new_w
            

    print(f'#{t}', end=' ')
    for lst in field:
        print(''.join(lst))