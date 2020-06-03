T = int(input())
for x in range(1, T+1):
    N = int(input())
    count = 0
    
    zero_to_nine = [str(i) for i in range(10)]
    while zero_to_nine:
        count += 1
        room = N * count
        room = str(room)

        for c in room:
            if c in zero_to_nine:
                zero_to_nine.remove(c)

    print('#{} {}'.format(x, room))