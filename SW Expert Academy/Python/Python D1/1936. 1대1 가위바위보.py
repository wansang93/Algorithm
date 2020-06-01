a, b = list(map(int, input().split()))
# scissor: 1, rock: 2, paper: 3
if a == 1:
    if b == 3:
        print('A')
    elif b == 1:
        print('B')
elif a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')
elif a == 3:
    if b == 2:
        print('A')
    elif b == 1:
        print('B')