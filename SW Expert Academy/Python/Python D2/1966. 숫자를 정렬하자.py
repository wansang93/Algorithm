T = int(input())
for t in range(1, T+1):
    N = int(input())
    mylist = sorted(list(map(int, input().split())))
    
    print(f'#{t}', end=' ')
    for i in mylist:
        print(i, end=' ')
    print()