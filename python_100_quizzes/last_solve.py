
input_data = '''0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0'''

# output_data = '''* f * 0 0
# 0 * 0 * 0
# 0 0 * f *
# 0 * f * 0
# 0 0 * 0 0'''

# flag = [] #지뢰 없이 깃발만 있는 리스트
# minesweeper = [] #지뢰를 찾은 리스트
# for i in range(5):
#     flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))

# minesweeper = [[str(0) for i in range(len(flag))] for i in range(len(flag[0]))]

# for i in range(len(flag)):
#     for j in range(len(flag[i])):
#         if flag[i][j] == '1':
#             minesweeper[i][j] = 'f'
#             if j-1 >= 0:
#                 minesweeper[i][j-1] = '*'
#             if j+1 <= len(flag[i]):
#                 minesweeper[i][j+1] = '*'
#             if i-1 >= 0:
#                 minesweeper[i-1][j] = '*'
#             if i+1 <= len(flag[i+1]):
#                 minesweeper[i+1][j] = '*'

# for i in minesweeper:
#     print(' '.join(i))


# 풀이81-2

# value ='''0 1 0 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 0 0 1 0 0
# 0 0 0 0 0'''
# print(value.split('\n'))
# sp = value.split('\n')
# count = 0
# for i in sp:
#     sp[count] = i.replace('1', 'f').split(' ')
#     count += 1
# print(sp)
# count = 0
# search = 0
# for s in sp:
#     for i in s:
#         if i == 'f':
#             search = s.index(i)
#             if search > 0:
#                 s[search-1] = '*'
#             if search < 4:
#                 s[search+1] = '*'
#             if count > 0:
#                 sp[count-1][search] = '*'
#             if count < 4:
#                 sp[count+1][search] = '*'
#     count += 1
# for i in sp:
#     print(i)

# 풀이81-3

inputList = []
for i in range(5):
    inputList.extend(input().split())
for i in range(25):
    if inputList[i] == "1":
        inputList[i] = "f"
        if i // 5 != 0:
            inputList[i - 5] = "*"
        if i // 5 != 4:
            inputList[i + 5] = "*"
        if i % 5 != 0:
            inputList[i - 1] = "*"
        if i % 5 != 4:
            inputList[i + 1] = "*"
for i in range(25):
    if i % 5 != 4:
        print(inputList[i], end = " ")
    else:
        print(inputList[i], " ")