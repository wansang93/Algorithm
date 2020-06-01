T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split(' ')))
    answer = 0
    
    count_dic = {}
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1





    print('#{} {}'.format(test_number, answer))