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
    