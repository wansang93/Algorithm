# I/O template
import sys

FILE_INPUT_PATH = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(FILE_INPUT_PATH, 'r')

# Solve here

from collections import deque

N = int(input())
lst = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]

q = deque()

for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        q.append((y, x))
        while q:
            y, x = 
