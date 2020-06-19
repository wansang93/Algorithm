T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())
    answer = 0

    if A > B:
        A, B = B, A

    answer += C // A
    answer += (C % A) // B

    print(f'#{t} {answer}')