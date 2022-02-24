# C언어 Python으로 연습하기

# 본인 이름 13번 출력하기

for i in range(13):
    print("김완상", end=" ")
print()

"""
for를 사용하는 이유
1. n번 반복 for i in range(N)
2. a~b까지 출력 for i in range(a, b+1)
"""

# 첫 줄 1~5까지 출력
# 둘 줄 9~3까지 출력

for i in range(5):
    print(i+1, end=" ")
print()

for i in range(9, 2, -1):
    print(i, end=" ")
print()

"""다음 출력하기
5
4
3
2
1
발사 발사 발사 발사 발사 발사 발사
"""

for i in range(5, 0, -1):
    print(i)

for i in range(7):
    print("발사", end=" ")
print()


# 0부터 5까지 리스트 생성
lst = [i for i in range(6)]
print(lst)  # [0, 1, 2, 3, 4, 5]

# 5부터 11까지 리스트 생성
lst = [i for i in range(5, 12)]
print(lst)  # [5, 6, 7, 8, 9, 10, 11]

# 가독성 별로 안좋은 방법(C++ 기준)
lst = [0] * 7
for i in range(7):
    lst[i] = i + 5
print(lst)

# 가독성 좋은 방법(C++ 기준)

lst = [0] * 7
t = 5
for i in range(7):
    lst[i] = t
    t += 1
print(lst)

# 15~11까지 list 생성
lst = [0] * 5
t = 15
for i in range(5):
    lst[i] = t
    t -= 1
print(lst)

# 20, 15, 10, 5, 0, -5 배열 생성
lst = [i for i in range(20, -6, -5)]
print(lst)

lst = [0] * 6
t = 20
for i in range(6):
    lst[i] = t
    t -= 5
print(lst)

# Swap
a, b = 1, 2
a, b = b, a

# Swap(c++기준)
temp = a
a = b
b = temp

a, b = 1, 35
temp = a
a = b
b = temp

####################################################################################################

# Count 3갯수 출력하기
lst = [3, 5, 3, 3, 7, 9]

cnt = 0
for i in range(6):
    if lst[i] == 3:
        cnt += 1
print(cnt)


# 1 또는 5면 카운트
lst = [1, 5, 1, 5, 1, 3, 7]
cnt = 0
for i in range(7):
    if lst[i] in (1, 5):
        cnt += 1
print(cnt)

lst = ['K', 'A', 'B', 'A', 'A', 'C', 'H']
cnt = 0
for i in range(7):
    if 'A' <= lst[i] <= 'H':
        cnt += 1
print(cnt)

######################### Character #########################

# A를 소문자 A로 변환
a = 'A'
print(chr(ord(a) + 32))

# A~Z까지 출력
for i in range(26):
    print(chr(ord('A') + i), end = " ")
    print(chr(65 + i), end = " ")
print()

# z부터 h까지 출력
i = 0
while True:
    temp = chr(ord('z') - i)
    print(temp, end=" ")
    if temp == 'h':
        break
    i += 1
print()

# c가 소문자? 대문자? 숫자?
c = '1'
if 'A' <= c <= 'Z':
    print("large")
elif 'a' <= c <= 'z':
    print("small")
elif '0' <= c <= '9':
    print("num")

vect = [4, 2, 5, 5, 1, 3, 7]

for i in range(len(vect)):
    for j in range(i, len(vect)):
        print(vect[j], end="")
    print()

# 함수 주고 받기
# pass


lst = [3, 5, 3, 3, 2, 3]

isthree = False
for i in lst:
    if i == 3:
        isthree = True
        break
print('O' if isthree else 'X')

lst = ['A', 'B', 'A', 'A', 'Q']
islarge = False
for i in lst:
    if 'A' <= i <= 'Z':
        islarge = True

print('O' if islarge else 'X')

##### 2중 for문 #####

for i in range(3):
    print(*[i for i in range(1, 6)])

n = 3
for i in range(n):
    for j in range(3, 10, 2):
        print(j, end="")
    print()

# NxN 배열 출력
for i in range(n):
    for j in range(n):
        print('#', end="")
    print()

# 10 7 4 1 출력 * 6번
for i in range(6):
    for j in range(10, 0, -3):
        print(j, end= " ")
    print()

# ABAKA 출력 * 3번
lst = ['A', 'B', 'A', 'K', 'A']
for i in range(3):
    for j in range(len(lst)):
        print(lst[j], end="")
    print()

# lst 역순으로 출력하기 * 4
lst = [1, 9, 1, 4, 5]
for i in range(4):
    for j in range(len(lst)-1, -1, -1):
        print(lst[j], end="")
    print()

lst = [1, 1, 2, 5, 3, 7, 4]
for i in range(2):
    for j in range(1, 4):
        print(lst[j], end="")
    print()

for i in range(3):
    for j in range(2, 6):
        print(lst[j], end="")
    print()

# selecting sorting
lst = [2, 5, 3, 1, 7]

for x in range(len(lst)-1):
    for y in range(x+1, len(lst)):
        if lst[x] > lst[y]:
            lst[x], lst[y] = lst[y], lst[x]
print(lst)

##### 2d array

lst = [4, 2, 5, 5, 1, 3, 7]
for i in range(7):
    for j in range(7-i):
        print(lst[j], end=" ")
    print()

for i in range(7):
    for j in range(i, 7):
        print(lst[j], end="")
    print()

lst = ['A', 'B', 'a', 'b', 'c', 'Q', 'W', 'E']

for i in range(8):
    for j in range(7-i, 8):
        print(lst[j], end=" ")
    print()

for i in range(8):
    for j in range(i, -1, -1):
        print(lst[j], end="")
    print()

##### 2d array & for loop #####

# 3x5 array 생성 후 n으로 채워넣기
n = 3
lst = [[0] * 5 for _ in range(3)]
for i in range(3):
    for j in range(5):
        lst[i][j] = n

for i in range(3):
    for j in range(5):
        print(lst[i][j], end='')
    print()

lst = [[0] * 4 for _ in range(3)]
for i in range(2):
    for j in range(1, 4):
        lst[i][j] = 7

for i in range(1, 3):
    for j in range(3):
        lst[i][j] = 9

lst[0][0] = 999
lst[2][3] = 999

for i in range(3):
    for j in range(4):
        print(lst[i][j], end=" ")
    print()

# 5x5 1 2 3 4 5 0열에 역순으로 넣기
lst = [[0] * 5 for _ in range(5)]
t = 1
for i in range(4, -1, -1):
    lst[i][0] = t
    t += 1

for row in lst:
    print(*row)

t = 1
for i in range(4, -1, -1):
    lst[4][i] = t
    t += 1

for row in lst:
    print(*row)

t = 1
for i in range(5):
    lst[i][3] = t
    t += 1

for i in range(4, -1, -1):
    lst[2][i] = t
    t += 1

print()
for row in lst:
    print(*row)

t = 1
for i in range(5):
    lst[i][i] = t
    t += 1

for i in range(5):
    lst[i][4] = t
    t += 1

print()
for row in lst:
    print(*row)

# 369, 258, 147 배열로 출력하기
lst = [[0] * 3 for _ in range(3)]
t = 1
for i in range(3):
    for j in range(2, -1, -1):
        lst[j][i] = t
        t += 1

print()
for row in lst:
    print(*row)

t = 1
for i in range(3):
    for j in range(2, -1, -1):
        lst[i][j] = t
        t += 1

print()
for row in lst:
    print(*row)

t = 1
for i in range(2, -1, -1):
    for j in range(2, -1, -1):
        lst[j][i] = t
        t += 1

print()
for row in lst:
    print(*row)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 2, 4]
lst = [[0] * 4 for _ in range(3)]
t = 0
for i in range(3):
    for j in range(4):
        lst[i][j] = nums[t]
        t += 1

sum = 0
for i in range(2):
    for j in range(3):
        sum += lst[i][j]

print(sum)
sum = 0
for i in range(1, 3):
    for j in range(1, 4):
        sum += lst[i][j]
print(sum)

lst = [[1, 2, 3, 4], [5, 3, 4, 2]]
_min = int(10e9)
_max = 0
for i in range(2):
    for j in range(4):
        if _min > lst[i][j]:
            _min = lst[i][j]
        elif _max < lst[i][j]:
            _max = lst[i][j]

print(_min, _max)

# struct // class in python
class KFC:
    a, b = 0, 0

t = 10
x = KFC()
x.a = 10
x.b = 20

print(x.a, x.b)

class BHC:
    g = 0
    ch = ''

    def __init__(self, g, ch):
        self.g = g
        self.ch = ch

a = BHC(0, 'B')
b = BHC(15, 'A')
print(a, b)

# 5번 출력
i = 5
while i > 0:
    print('#')
    i -= 1

# 3~7까지 출력
i = 3
while i < 8:
    print(i, end=" ")
    i += 1
print()

# 10부터 1까지 출력
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
