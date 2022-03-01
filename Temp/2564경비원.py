# I/O template
import sys

FILE_INPUT_PATH = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(FILE_INPUT_PATH, 'r')

# Solve here

C, R = map(int, input().split())
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
dcd, dl = map(int, input().split())

answer = 0
for cd, l in lst:
    # 같은편
    if dcd == cd:
        answer += abs(dl-l)
    # 반대편
    elif dcd:
        pass
    # 옆쪽
    else:
        answer += dl
