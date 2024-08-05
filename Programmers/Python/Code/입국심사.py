def solution(n, times):
    l, r = 1, max(times) * n
    while l <= r:
        m = (l + r) // 2
        total = 0
        for time in times:
            total += m // time
        if total >= n:
            r = m - 1
        else:
            l = m + 1
    return l
