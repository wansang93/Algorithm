def solution(cards1, cards2, goal):
    i, j = 0, 0
    for v in goal:
        if i < len(cards1) and v == cards1[i]:
            i += 1
        elif j < len(cards2) and v == cards2[j]:
            j += 1
        else:
            return 'No'
    return 'Yes'
