num = int(input())

for i in range(num):
    x = list(map(int, input().split(' ')))
    print('#{} {}'.format(i+1, max(x)))