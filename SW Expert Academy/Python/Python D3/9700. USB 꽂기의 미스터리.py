T = int(input())
for t in range(1, T+1):
    p, q = map(float, input().split())
    answer = 'NO'

    s1, s2 = (1-p) * q, p * (1-q) * q

    if s1 < s2:
        answer = 'YES'

    print(f'#{t} {answer}')