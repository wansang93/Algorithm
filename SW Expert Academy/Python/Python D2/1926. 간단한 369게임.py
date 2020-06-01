N = int(input())

for i in range(1, N+1):
    s = str(i)
    if '3' in s or '6' in s or '9' in s:
        count = s.count('3') + s.count('6') + s.count('9')
        print('-' * count, end=' ')
    else:
        print(i, end=' ')
