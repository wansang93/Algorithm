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
