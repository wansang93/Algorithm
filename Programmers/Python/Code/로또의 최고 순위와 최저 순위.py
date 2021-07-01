def solution(lottos, win_nums):
    unknown = 0
    hit = 0
    count_hit_to_rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    for my_num in lottos:
        if my_num == 0:
            unknown += 1
        elif my_num in win_nums:
            hit += 1
    answer = [count_hit_to_rank[(hit+unknown)], count_hit_to_rank[hit]]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
