for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort(reverse=True)
    x, y = 0, -1  # max_cur, min_cur
    
    for _ in range(dump):
        # do not need to find it when the difference between max and min is 1
        if boxes[x] - 1 == boxes[y]:
            break
        # find max_height
        while True:
            if boxes[x] == boxes[x+1]:
                x += 1
            elif boxes[x] > boxes[x+1]:
                break

        # find min_height
        while True:
            if boxes[y-1] == boxes[y]:
                y -= 1
            elif boxes[y-1] > boxes[y]:
                break

        # move high to low
        boxes[x] -= 1
        boxes[y] += 1
        x -= 1
        y += 1

        # check out of index
        if x == -1:
            x = 0
        if y == 0:
            y = -1

    answer = boxes[x] - boxes[y]
    print(f'#{t} {answer}')
