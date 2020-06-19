T = int(input())
for t in range(1, T+1):
    # 처음 입력값
    N = int(input())

    # 행렬이 input일 때
    matrix = []
    for i in range(N):
        matrix.append(list(input()))

    # 두 숫자가 인풋일 때, 여러 숫자가 리스트 일 때
    n, m = list(map(int, input().split()))
    

    answer = 0
    print(f'#{t} {answer}')