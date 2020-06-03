# 풀이1: 노가다 풀이(ㅜㅜ)
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

# 풀이2
T = int(input())
for t in range(1, T+1):
    N = int(input())
    KRW_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    KRW_dict = dict.fromkeys(KRW_list, 0)
    # KRW_dict = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}

    for i in KRW_list:
        KRW_dict[i] += N // i
        N %= i
    
    print(f'#{t}')
    for i in KRW_list:
        print(KRW_dict[i], end=' ')
    print()
