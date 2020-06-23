T = int(input())
for t in range(1, T+1):
    p, q = map(int, input().split())

    # base_lst = [1, 3, 6, 10 ... 1+2+3+...+N(400)->20100]
    base_lst = []
    c = 0
    for i in range(1, 401):
        c += i
        base_lst.append(c)

    # q 와 p 의 좌표 구하기
    coordinate = [[], []]
    for x in range(len(base_lst)):
        if not coordinate[0] and p <= base_lst[x]:
            gap_p = base_lst[x] - p
            coordinate[0] = [1+x-gap_p, 1+gap_p]
        if not coordinate[1] and q <= base_lst[x]:
            gap_q = base_lst[x] - q
            coordinate[1] = [1+x-gap_q, 1+gap_q]
        if coordinate[0] and coordinate[1]:
            break
    
    # 넣은 좌표로 새 좌표 구하기
    new_x = coordinate[0][0] + coordinate[1][0]
    new_y = coordinate[0][1] + coordinate[1][1]  

    # 좌푯값으로 x값 계산
    p_star_q = base_lst[new_x-1]

    # 좌푯값으로 y값 계산
    for i in range(new_y-1):
        p_star_q += new_x + i

    print(f'#{t} {p_star_q}')
