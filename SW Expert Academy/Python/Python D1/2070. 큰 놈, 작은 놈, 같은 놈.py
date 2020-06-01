num = int(input())
for i in range(num):
    x = list(map(int, input().split()))
    result = ''
    if x[0] > x[1]:
        result = '>'
    elif x[0] == x[1]:
        result = '='
    else:
        result = '<'
    print('#{} {}'.format(i+1, result))