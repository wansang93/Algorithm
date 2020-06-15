# 풀이1
for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    i = 2
    # 해당 값까지 반복문으로 돌린다.
    while True:
    # 해당 값에 간다.
        select_building = buildings[i]
    # 왼쪽 두개 탐색, 오른쪽 두개 탐색한다.
        temp = []
        for s in buildings[i-2:i] + buildings[i+1:i+3]:
    # 차이를 계산한다.
            difference = select_building - s
    # 차이가 음수면 탐색 종료
            if difference < 0:
                break
    # 음수값이 안나오면 임시 변수에 넣는다.
            else:
                temp.append(difference)
    # 임시 변수의 길이가 4이면 최솟값을 정답에 더한다.
        if len(temp) == 4:
            answer += min(temp)
    
    # i를 증가시킨다.
        if difference < 0:
            i += 1
        else:
            i += 2

        if i > N-1:
            break
            
    print(f'#{t} {answer}')

# 풀이2
for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        minimum = 0
        for j in buildings[i-2:i] + buildings[i+1:i+3]:
            temp = buildings[i] - j
            if temp <= 0:
                minimum = 0
                break
            else:
                if minimum == 0:  # 이걸 생각 못하다니ㅜㅜ
                    minimum = temp
                elif temp < minimum:
                    minimum = temp 
        answer += minimum
    
    print(f'#{t} {answer}')