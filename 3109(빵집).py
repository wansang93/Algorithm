# I/O template
import sys

FILE_INPUT_PATH =  (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin  =  open(FILE_INPUT_PATH, 'r')

# Solve here

R, C = map(int, input().split())
lst = [list(input()) for _ in range(R)]
dc = (-1, 0, 1)
answer = 0

for i in range(R):
    nowc = i
    for j in range(C-1):
        # 현재 좌표 방문
        lst[nowc][j] = str(i)

        # 위로 방문 가능?
        nextc = nowc - 1
        if 0 <= nextc < R and lst[nextc][j+1] == '.':
            nowc = nextc
            continue

        # 중간 방문 가능?
        nextc = nowc + 0
        if 0 <= nextc < R and lst[nextc][j+1] == '.':
            nowc = nextc
            continue

        # 아래 방문 가능?
        nextc = nowc + 1
        if 0 <= nextc < R and lst[nextc][j+1] == '.':
            nowc = nextc
            continue
        
        # 다 못가? 응 너 안돼~
        break
    else:
        answer += 1

for row in lst:
    print(*row)

print(answer)
