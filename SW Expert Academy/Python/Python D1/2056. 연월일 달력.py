num = int(input())
result = ''
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(num):
    x = input()
    month = int(x[4:6])
    day = int(x[6:8])
    if 1<= month <= 12 and 1 <= day <= days[month-1]:
        result = '{}/{}/{}'.format(x[0:4], x[4:6], x[6:8])
    else:
        result = '-1'
    print('#{} {}'.format(i+1, result))
