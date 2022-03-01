# I/O template
import sys

FILE_INPUT_PATH = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(FILE_INPUT_PATH, 'r')

# Solve here

"""
Input example
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    stack = list(sorted(lst))
    print(stack, lst)
