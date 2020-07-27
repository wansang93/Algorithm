import sys
sys.stdin = open(r'C:/Users/wansang/Desktop/Gitrep/Algorithm/SW Expert Academy/Python/Python D3/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    check_ship = []
    for i in range(N):
        value = int(input())
        value -= 1
        if check_ship:
            for i in check_ship:
                if value % i == 0:
                    break
            else:
                check_ship.append(value)
        else:
            if value != 0:
                check_ship.append(value)

    answer = len(check_ship)
    print(f'#{t} {answer}')


# # 실패한 시간 초과 풀이
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())

#     happy_day_list = []
#     check_ship = []
#     for i in range(N):
#         value = int(input())
#         happy_day_list.append(value)
#         for now_idx in range(i-1, -1, -1):
#             cal_day = value - happy_day_list[now_idx]
#             if cal_day in check_ship:
#                 break
#             else:
#                 if now_idx == 0:
#                     check_ship.append(cal_day)

#     answer = len(check_ship)
#     print(f'#{t} {answer}')