# 코드 업 기초 100제 파이썬 풀이

- 2020-01-17 ~ 2020-01-21 (5days) Finished

## [코드업 기초 100제 웹사이트 바로가기](https://codeup.kr/problemsetsol.php?psid=23)

## 내 풀이

``` python
# 코드업 100문제 파이썬 버전

# 1001
print('Hello')

# 1002
print('Hello World')

# 1003
print('Hello\nWorld')

# 1004
print("'Hello'")

# 1005
print('"Hello World"')

# 1006
print('"!@#$%^&*()"')

# 1007
print('"C:\\Download\\hello.cpp"')

# 1008
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print("\u250C\u252C\u2510")
print("\u251C\u253C\u2524")
print("\u2514\u2534\u2518")

# 1010
a = int(input())
print(a)

# 1011
char = input()
print(char)

# 1012
fnum = float(input())
print('%f' % fnum)

# 1013
a, b = map(int, input().split())
print('%d %d' % (a, b))

# 1014
a, b = input().split()
print(b, a)

# 1015
a = float(input())
print('%.2f' % a)

# 1017
a = int(input())
print('%d %d %d' % (a, a, a))

# 1018
s = input().split(':')
print(s[0]+':'+s[1])

# 1019
s = list(map(int, input().split('.')))
print('%04d.%02d.%02d' % (s[0], s[1], s[2]))

# 1020
s = input().split('-')
print(s[0]+s[1])

# 1021
s = print(input())

# 1022
s = print(input())

# 1023
s = input().split('.')
print(s[0])
print(s[1])

# 1024
l = input()
for i in l:
    print("'"+i+"'")
    # print("'%s'" % i)

# 1025
num = input()
for i, c in enumerate(num):
    print('[%s%s]' % (c, (len(num)-i-1)*'0'))

# 1026
s = input().split(':')
print('%d' % int(s[1]))

# 1027
s = list(map(int, input().split('.')))
print('%02d-%02d-%04d' % (s[2], s[1], s[0]))

# 1028
num = print(int(input()))

# 1029
a = int(input())
print(a)

# 1030
a = int(input())
print(a)

# 1031
a = int(input())
print('%o' % a)

# 1032
a = int(input())
print('%x' % a)

# 1033
a = int(input())
print('%X' % a)

# 1034
a = int(input(), 8)
print(a)

# 1035
a = int(input(), 16)
print('%o' % a)

# 1036
a = ord(input())
print(a)

# 1037
a = int(input())
print('%c' % a)

# 1038
a, b = [int(i) for i in input().split()]
print(a+b)

# 1039
a, b = [int(i) for i in input().split()]
print(a+b)

# 1040
a = int(input())
print(-a)

# 1041
a = ord(input())+1
print(chr(a))

# 1042
a, b = [int(i) for i in input().split()]
print(a//b)

1043
a, b = [int(i) for i in input().split()]
print(a%b)

# 1044
a = int(input())
a += 1
print(a)

# 1045
a, b = [int(i) for i in input().split()]
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print('%.2f' % (a/b))

# 1046
a, b, c = [int(i) for i in input().split()]
print(a+b+c)
print('%.1f' % ((a+b+c)/3))

# 1047
a = int(input())
print(a<<1)

# 1048
a, b = [int(i) for i in input().split()]
print(a<<b)

# 1049
a, b = [int(i) for i in input().split()]
print(int(a>b))

# 1050
a, b = [int(i) for i in input().split()]
print(int(a==b))

# 1051
a, b = [int(i) for i in input().split()]
print(int(b>=a))

# 1052
a, b = [int(i) for i in input().split()]
print(int(b!=a))

# 1053
a = int(input())
print(int(not a))

# 1054
a, b = [int(i) for i in input().split()]
print(int(a and b))

# 1055
a, b = [int(i) for i in input().split()]
print(int(a or b))

# 1056
a, b = [int(i) for i in input().split()]
print(int(a^b))

# 1057
a, b = [int(i) for i in input().split()]
print(int(not(a^b)))

# 1058
a, b = [int(i) for i in input().split()]
print(int(not int(a or b)))

# 1059
a = int(input())
print(~a)

# 1060
a, b = [int(i) for i in input().split()]
print(a & b)

# 1061
a, b = [int(i) for i in input().split()]
print(a | b)

# 1062
a, b = [int(i) for i in input().split()]
print(a ^ b)

# 1063
a, b = [int(i) for i in input().split()]
print(a if a>b else b)

# 1064
a, b, c = [int(i) for i in input().split()]
print(min(a, b, c))

# 1065
a = [int(i) for i in input().split()]
for i in a:
    if i % 2 == 0:
        print(i)

# 1066
a = [int(i) for i in input().split()]
for i in a:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

# 1067
a = int(input())
if a < 0:
    print('minus')
else:
    print('plus')

if a % 2 == 0:
    print('even')
else:
    print('odd')

# 1068
a = int(input())
if 90 <= a <= 100:
    print('A')
elif 70 <= a < 90:
    print('B')
elif 40 <= a < 70:
    print('C')
elif 0 <= a < 40:
    print('D')

# 1069
a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')

# 1070
a = int(input())
dic = {
12: 'winter',
1: 'winter',
2: 'winter',
3: 'spring',
4: 'spring',
5: 'spring',
6: 'summer',
7: 'summer',
8: 'summer',
9: 'fall',
10: 'fall',
11: 'fall',
}

if a in dic:
    print(dic[a])

# 1071
a = [int(i) for i in input().split()]
for i in a:
    if i == 0:
        break
    print(i)

# 1072
N = int(input())
mylist = [int(i) for i in input().split()]

for i in mylist:
    print(i)

# 1073
a = [int(i) for i in input().split()]
i = 0
x = a[0]
while x != 0:
    print(x)
    i += 1
    x = a[i]

# 1074
a = int(input())
while a > 0:
    print(a)
    a -= 1

# 1075
a = int(input())
while a > 0:
    a -= 1
    print(a)

# 1076
c = ord(input())
i = ord('a')
while i <= c:
    print(chr(i), end=' ')
    i += 1

# 1077
a = int(input())
for i in range(a+1):
    print(i)

# 1078
a = int(input())
k = 0
for i in range(0, a+1, 2):
    k += i
print(k)

# 1079
a = [i for i in input().split()]
for i in a:
    print(i)
    if i == 'q':
        break

# 1080
a = int(input())
hap = 0
i = 0
while hap < a:
    i += 1
    hap += i
print(i)

# 1081
a, b = [int(i) for i in input().split()]

for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)

# 1082
a = input()
for i in range(1, 16):
    print('{}*{:X}={:X}'.format(a.upper(), i, (int(a, 16)*i)))

# 1083
a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        print('X', end=' ')
    else:
        print(i, end=' ')

# 1084
a, b, c = [int(i) for i in input().split()]
num = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            num +=1
print(num)

# 1085
h, b, c, s = [int(i) for i in input().split()]
print('{:.1f} MB'.format(h*b*c*s/(8*1024*1024)))

# 1086
w, h, b = [int(i) for i in input().split()]
print('{:.2f} MB'.format(w*h*b/(8*1024*1024)))

# 1087
a = int(input())
sum = 0
i = 1
while sum < a:
    sum += i
    i += 1
print(sum)

# 1088
a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        pass
    else:
        print(i, end=' ')

# 1089
a, d, n = [int(i) for i in input().split()]
print(a+(n-1)*d)

# 1090
a, d, n = [int(i) for i in input().split()]
print(a*d**(n-1))

# 1091
a, m, d, n = [int(i) for i in input().split()]
result = a
for i in range(n-1):
    result = result * m + d
print(result)

# 1092
a, b, c = [int(i) for i in input().split()]
result = 1
while result % a != 0 or result % b != 0 or result % c != 0:
    result += 1
print(result)

# 1093
n = int(input())
num = [int(i) for i in input().split()]
mylist = [0] * 23
for i in num:
    mylist[i-1] += 1
    
for i in mylist:
    print(i, end=' ')

# 1094
n = int(input())
num = [int(i) for i in input().split()]
for i in range(len(num)):
    print(num[-i-1], end= ' ')

# 1095
n = int(input())
num = [int(i) for i in input().split()]
min = num[0]
for i in num:
    if i < min:
        min = i
print(min)

# 1096
n = int(input())
mylist = [0] * n
for i in range(n):
    mylist[i] = [int(i) for i in input().split()]

board = [[0 for i in range(19)] for i in range(19)]

for i in mylist:
    board[i[0]-1][i[1]-1] = 1

for i in board:
    for j in i:
        print(j, end=' ')
    print()

# 1097
board = []
for i in range(19):
    board.append([int(i) for i in input().split()])

n = int(input())
lines = []
for i in range(n):
    lines.append([int(i) for i in input().split()])

for line in lines:
    i, j = line[0]-1, line[1]-1
    for k in range(19):
        if board[i][k] == 1:
            board[i][k] = 0
        else:
            board[i][k] = 1
        
        if board[k][j] == 1:
            board[k][j] = 0
        else:
            board[k][j] = 1        

for i in board:
    for j in i:
        print(j, end=' ')
    print()

# 1098
w, h = [int(i) for i in input().split()]
board = []
for i in range(w):
    temp = []
    for j in range(h):
        temp.append(0)
    board.append(temp)

n = int(input())
stick = []
for i in range(n):
    stick.append([int(i) for i in input().split()])

for i in range(len(stick)):
    l, d, x, y = stick[i]
    x -= 1
    y -= 1
    if d == 0:
        for j in range(l):
            board[x][y+j] = 1
    else:
        for k in range(l):
            board[x+k][y] = 1

for i in board:
    for j in i:
        print(j, end=' ')
    print()

# 1099
board = []
for _ in range(10):
    board.append([int(i) for i in input().split()])

i, j = 1, 1
while True:
    if board[i][j] == 2:
        board[i][j] = 9
        break
    elif board[i][j] == 0:
        board[i][j] = 9
        if board[i][j+1] in [0, 2]:
            j += 1
        else:
            i += 1
    else:
        break

for i in board:
    for j in i:
        print(j, end=' ')
    print()
```