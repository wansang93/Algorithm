# 풀이1
def solution(n):
    answer = 0
    print(n**(1/2))
    if int(n**(1/2)) == n**(1/2):
        answer = (n**(1/2)+1)**2
    else:
        answer = -1
    # sqrt(n) % 1 == 0 -> 정수 판별법
    return answer

# 풀이2
def solution2(n):
    answer = -1
    if n // (n**(1/2)) == (n**(1/2)):
        answer = ((n**(1/2))+1)**2
    return answer

# 풀이3
def solution3(n):
    answer = -1
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        answer = (sqrt+1)**2
    return answer