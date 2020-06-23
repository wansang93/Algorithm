T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    cards1 = cards[:(len(cards)-1)//2+1]
    cards2 = cards[(len(cards)-1)//2+1:]
    
    perfect_shuffle = []
    for i in range(len(cards2)):
        perfect_shuffle.append(cards1[i])
        perfect_shuffle.append(cards2[i])

    if N % 2 == 1:
        perfect_shuffle.append(cards1[-1])

    print(f'#{t} {" ".join(perfect_shuffle)}')