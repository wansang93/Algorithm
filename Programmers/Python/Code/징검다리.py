def solution(distance, rocks, n):
    rocks.extend([0, distance])
    rocks.sort()
    
    l, r = 0, distance
    while l <= r:
        m = (l+r) // 2
        pre, cnt = 0, 0
        for now in rocks[1:]:
            v = now - pre
            if v < m:
                cnt += 1
                if cnt > n:
                    break
            pre = now
        
        if cnt <= n:
            r = m - 1
        else:
            l = m + 1
    
    return r
