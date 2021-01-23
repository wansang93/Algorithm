T = int(input())
for t in range(1, T+1):

    # 두 숫자가 인풋일 때, 여러 숫자가 리스트 일 때
    N, M = map(int, input().split())

    count = 0
    for i in bin(M)[2:][::-1]:
        if int(i) == 0:
            break
        else:
            count += 1
    
    answer = 'OFF'
    if count >= N:
        answer = 'ON'

    print(f'#{t} {answer}')
