# 풀이1
def solution(n):
    answer = 0
    for i in range(2, n+1, 1):
        tmp = 0
        for j in range(1, i+1, 1):
            if i % j == 0:
                tmp += 1
                if tmp > 2:
                    break
        if tmp == 2:
            answer += 1
    
    return answer

# 풀이2
def solution2(n):
    answer = 0
    prime = [i for i in range(3, n+1, 2)]
    for i in range(3, int(n**(1/2))+1, 2):
        if i in prime:
            for k in range(i*2, n+1, i):
                if k in prime:
                    prime.remove(k)
    
    answer = len(prime) + 1
    return answer

# 풀이3
def solution3(n):
    num = [True for i in range(n+1)]
    num[0], num[1] = False, False

    for i in range(2, int(n**(1/2)+1)):
        if num[i] == True:
            for k in range(i*2, n+1, i):
                num[k] = False
                
    return num.count(True)

# 풀이4
def solution4(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)