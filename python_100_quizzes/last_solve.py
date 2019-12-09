x = int(input())
for i in range(2, int(x**1/2)+1 + 1):
    if x == 1:                # x가 1이면
        print('NO')           # 1은 소수가 아님으로 NO
        break
    if x == 2:                # x가 2이면
        print('YES')          # 소수이므로 YES
        break
    if x % i == 0:            # 어떤 수(x)가 루트x + 1보다 작은수로 나눠지면
        print('NO')           # 약수가 있으므로 NO
        break
else:
    print('YES')              # 그 외에는 약수가 없으므로 YES