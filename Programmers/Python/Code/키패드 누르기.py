def solution(numbers, hand):
    answer = ''
    location = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    l_loc = (3, 0)
    r_loc = (3, 2)
    is_left = False
    if hand == 'left':
        is_left = True

    for i in numbers:
        if i in location[0]:
            answer += 'L'
            l_loc = (location[0].index(i), 0)
        elif i in location[2]:
            answer += 'R'
            r_loc = (location[2].index(i), 2)
        else:
            x, y = (location[1].index(i), 1)
            l_distance = abs(l_loc[0] - x) + abs(l_loc[1] - y)
            r_distance = abs(r_loc[0] - x) + abs(r_loc[1] - y)
            if l_distance < r_distance:
                l_loc = (x, y)
                answer += 'L'
            elif l_distance > r_distance:
                r_loc = (x, y)
                answer += 'R'
            else:
                if is_left:
                    l_loc = (x, y)
                    answer += 'L'
                else:
                    r_loc = (x, y)
                    answer += 'R'
            
    return answer

