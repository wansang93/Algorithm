T = int(input())
for t in range(1, T+1):
    N = int(input())
    KRW50000 = 0
    KRW10000 = 0
    KRW5000 = 0
    KRW1000 = 0
    KRW500 = 0
    KRW100 = 0
    KRW50 = 0
    KRW10 = 0

    KRW50000 += N//50000
    N %= 50000
    KRW10000 += N//10000
    N %= 10000

    KRW5000 += N//5000
    N %= 5000
    KRW1000 += N//1000
    N %= 1000

    KRW500 += N//500
    N %= 500
    KRW100 += N//100
    N %= 100

    KRW50 += N//50
    N %= 50
    KRW10 += N//10
    N %= 10
    

    print('#{}\n{} {} {} {} {} {} {} {}'.format(
        t, KRW50000, KRW10000, KRW5000, KRW1000, KRW500, KRW100, KRW50, KRW10))
