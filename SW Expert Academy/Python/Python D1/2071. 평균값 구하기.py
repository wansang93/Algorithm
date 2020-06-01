num = int(input())
for i in range(1, num+1):
    j = list(map(int, input().split(' ')))
    avg = 0
    for k in j:
        avg += k
    avg /= len(j)
    
    print('#{} {}'.format(i, round(avg)))
