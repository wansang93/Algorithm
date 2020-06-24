T = int(input())
for t in range(1, T+1):
    info_cards = input()
    cards = {'S': [1 for _ in range(13)],
            'D': [1 for _ in range(13)],
            'H': [1 for _ in range(13)],
            'C': [1 for _ in range(13)],
            }

    is_ok = True
    for i in range(0, len(info_cards), 3):
        suit = info_cards[i]
        num = int(info_cards[i+1:i+3]) - 1
        if cards[suit][num] == 1:
            cards[suit][num] -= 1
        elif cards[suit][num] == 0:
            is_ok = False
            break

    answer = []
    for i in cards.values():
        answer.append(str(sum(i)))

    if not is_ok:
        print(f'#{t} {"ERROR"}')
    else:
        print(f'#{t} {" ".join(answer)}')