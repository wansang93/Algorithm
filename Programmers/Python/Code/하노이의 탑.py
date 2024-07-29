def hanoi_tower(n, pre, mid, to, answer):
    if n == 0:
        return
    
    hanoi_tower(n-1, pre, to, mid, answer)
    answer.append([pre, to])
    hanoi_tower(n-1, mid, pre, to, answer)


def solution(n):
    answer = []
    hanoi_tower(n, 1, 2, 3, answer)
    return answer
