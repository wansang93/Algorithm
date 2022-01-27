# I/O template
import sys
file_path = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here

# A = int(input())
# T = int(input())
# status = int(input())

# 1 01010011(4+4)
# 2 0101000111(4+6)
# 3 010100001111(4+8)
# 4 01010000011111(4+10) ...
# n (4+2+2*n)

num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")