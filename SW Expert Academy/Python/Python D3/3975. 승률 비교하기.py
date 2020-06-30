T = int(input())
winner = []
for t in range(1, T+1):
    A, B, C, D = map(int, input().split())
    alice_win_rate = A / B
    bob_win_rate = C / D

    if alice_win_rate > bob_win_rate:
        winner.append('ALICE')
    elif alice_win_rate == bob_win_rate:
        winner.append('DRAW')
    else:
        winner.append('BOB')

for idx, val in enumerate(winner):
    print(f'#{idx+1} {val}')