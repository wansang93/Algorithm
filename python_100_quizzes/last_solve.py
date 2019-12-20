# solution(59)
# [4, 12]

def solution(n):
    shake = 0
    num = 0
    tmp = 0
    while tmp <= n:
        tmp = int(num*(num+1)/2)
        num += 1

    shake = int(n - ((num-2)*(num-1)/2))
    return [shake, num]

def solution2(n):
    people = 0
    total = 0
    while(True):
        total = people*(people-1)/2
        if n<total:
            break
        people+=1
    times = int(people-(total-n)-1)
    return [times,people]

print(solution(55))
print(solution2(55))