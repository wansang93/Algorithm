import sys
sys.stdin = open(r'C:/Users/wansang/Desktop/Gitrep/Algorithm/SW Expert Academy/Python/Python D3/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    word = input()
    N = int(input())
    locate = list(map(int, input().split()))
    locate.sort()

    cur = 0
    for i in locate:
        word = word[:i+cur] + '-' + word[i+cur:]
        cur += 1

    print(f'#{t} {word}')