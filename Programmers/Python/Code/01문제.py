T = '0123456789ABCDEF'
def num_system(num, base):
    q, r = divmod(num, base)
    n = T[r]
    return num_system(q, base) + n if q else n

def solution(n):
    answer = 0
    ternary_num = str(num_system(n, 3))
    for i, v in enumerate(ternary_num):
        answer += int(v) * 3 ** i
    return answer
