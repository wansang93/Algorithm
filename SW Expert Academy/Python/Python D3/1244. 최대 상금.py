import sys
sys.stdin = open(r'C:/Users/wansang/Desktop/Gitrep/Algorithm/SW Expert Academy/Python/Python D3/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    price, num = input().split()
    change = int(num)
    price = list(map(int, [i for i in price]))
    cur = 0
    maximum = 0
    l = len(price)

    # 바꿀 횟수가 0 이면 종료
    while change > 0:

        # 뒤에서 2번째이면(즉, 커서가 앞부분을 다 탐색함) 뒤에 두개만 계속 교환하는 경우
        if cur >= l-2:
            if change % 2 == 1:
                price[-1], price[-2] = price[-2], price[-1]
            break

        # 커서 이후부터 최댓값과 인덱스 찾기
        maximum = price[cur]
        maximum_index = []
        for i in range(cur, l):
            if maximum < price[i]:
                maximum = price[i]
                maximum_index = [i]
            elif maximum == price[i]:
                maximum_index.append(i)
        len_maximum = len(maximum_index)
        
        # 커서가 가르키는 값이 max 값이면 cur만 이동
        if price[cur] == maximum and len_maximum == 1:
            cur += 1
            continue
        else:
            # 최댓값 갯수가 바꿀 횟수보다 많으면
            if len_maximum >= change:
                # 수정 횟수만큼 수정 후 종료
                for i in range(change):
                    pass
                break
            # 최댓값 갯수가 횟수보다 적으면

        break


    print(f'#{t} {price}')