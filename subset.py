# I/O template
import sys

FILE_INPUT_PATH = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(FILE_INPUT_PATH, 'r')

# Solve here


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

def subset(n, start):
    if (n == N//2):
        print(visited)
        return
    
    for i in range(start, N):
        visited[i] = True
        subset(n+1, i+1)
        visited[i] = False

subset(0, 0)