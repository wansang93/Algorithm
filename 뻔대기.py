# I/O template
import sys
from tkinter.messagebox import YES

FILE_INPUT_PATH = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(FILE_INPUT_PATH, 'r')

# Solve here

"""
#################### 풀이중 ####################
Input Data
4
6
1
"""

A = int(input())
T = int(input())
C = int(input())

lst = []

while True:
    for i in range(4):
        if i % 2 == 0:
            lst.append(0)
        elif i % 2 == 1:
            lst.append(1)


    break

"""
List를 1만개로 잡고 ㄱㄱ

뻔 = 0 / 데기 = 1
0101 00 11

an = n + 3

시그마an = n/2 * (2a+(n-1)d)
시그마an = n/2 * (2*4+n-1)
         = n/2 * (7+n)

a1 = 1/2 * 8+1-1 = 4, T가 같거나 작으면 break
a2 = 2/2 * 8+2-1 = 9
a3 = ...
an = 

n/2 * (7+n) > T
n * (7+n) > 2T
n * (7+n)
n = 1 

1 2 3 4
"""
