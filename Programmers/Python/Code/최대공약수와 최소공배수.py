# 풀이1
def gcd(n, m):
    mod = n % m
    while mod > 0:
        n = m
        m = mod
        mod = n % m
    return m

def lcm(n, m):
    return n * m // gcd(n, m)
    
def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer