best_score = 0
def solve(cur, score, calorie):
    global best_score
    if calorie > L or cur >= N:
        return

    new_score = score + scores[cur]
    new_calorie = calorie + calories[cur]
    if new_calorie <= L and new_score > best_score:
        best_score = new_score

    solve(cur+1, score, calorie)
    solve(cur+1, new_score, new_calorie)


T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    scores, calories = [], []
    for _ in range(N):
        s, c = map(int, input().split())
        scores.append(s)
        calories.append(c)

    solve(0, 0, 0)

    print(f'#{t} {best_score}')
    best_score = 0