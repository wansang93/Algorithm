T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split()))
    
    count_dic = {}
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1

    mode = 0
    max_count = 0
    for key, value in count_dic.items():
        if max_count < value:
            max_count = value
            mode = key
        elif max_count == value:
            if mode < key:
                mode = key

    print('#{} {}'.format(test_number, mode))