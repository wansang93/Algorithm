T = int(input())
for x in range(1, T+1):
    N = int(input())
    count = 0
    
    mylist = [str(i) for i in range(10)]
    while mylist != []:
        count += 1
        room = N * count
        room = str(room)

        for c in room:
            if c in mylist:
                mylist.remove(c)

    print('#{} {}'.format(x, room))