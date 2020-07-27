import sys
sys.stdin = open(r'C:/Users/wansang/Desktop/Gitrep/Algorithm/SW Expert Academy/Python/Python D3/input.txt', 'r')

# define padovan_sequence
padovan_sequence = [1, 1, 1, 2, 2]
input_maximum = 100
for i in range(input_maximum-5):
    padovan_sequence.append(padovan_sequence[i] + padovan_sequence[i+4])

T = int(input())
for t in range(1, T+1):
    N = int(input())

    answer = padovan_sequence[N-1]
    print(f'#{t} {answer}')