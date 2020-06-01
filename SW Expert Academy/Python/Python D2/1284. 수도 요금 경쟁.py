T = int(input())
for t in range(1, T+1):
    # P: A사 1L당 요금
    # Q: B사 RL이하 사용시 기본요금
    # S: B사 RL이상 사용시 SL당 요금
    # R: B사 기본요금 경계량
    # W: 사용량
    P, Q, R, S, W = map(int, input().split())

    cost_A = W * P 
    cost_B = Q
    if R < W:
        cost_B += S * (W-R)

    cost = min(cost_A, cost_B)

    print('#{} {}'.format(t, cost))