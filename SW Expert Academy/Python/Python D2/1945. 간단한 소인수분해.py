# N = 2 3 5 7 11

T = int(input())

for i in range(T):
    a, b, c, d, e = 0, 0, 0, 0, 0
    num = int(input())
    
    while num % 2 == 0:
        a += 1
        num //= 2
    while num % 3 == 0:
        b += 1
        num //= 3
    while num % 5 == 0:
        c += 1
        num //= 5
    while num % 7 == 0:
        d += 1
        num //= 7
    while num % 11 == 0:
        e += 1
        num //= 11
        
    print('#{} {} {} {} {} {}'.format(i+1, a, b, c, d, e))