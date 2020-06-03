T = int(input())
for t in range(1, T+1):
    h, m, ah, am = map(int, input().split())
    rh, rm = h + ah, m + am
 
    if rm >= 60:
        rm -= 60
        rh += 1

    if rh >= 25:
        rh -= 23
    elif rh >= 13:
        rh -= 12

    print('#{} {} {}'.format(t, rh, rm))