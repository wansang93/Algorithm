# 예)
# 100 == 47 + 53
# 56 == 19 + 37
# 2보다 큰 짝수 n이 주어졌을 때, 골드바흐 파티션을 출력하는 코드를 작성하세요. 

n = int(input())

def prime(n):
    primes =[]
    tmplist = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if tmplist[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                tmplist[j] = False
    
    return primes

def solution(n):
    mylist = []
    primes = prime(n)
    for i in primes:
        a = i
        b = n - a
        if b in primes:
            mylist.append([a, b])
    return mylist

print(solution(n))

# #골드바흐의 추측
# def cal():
#     n=10000*2
#     primes=[]    
#     a = [False,False] + [True]*(n-1)

#     for i in range(2,n+1):
#       if a[i]:
#         primes.append(i)
#         for j in range(2*i, n+1, i):
#             a[j] = False
            
#     return primes


# a = cal()

# #골드바흐파티션
# n = int(input())
# l = []
# k = []	

# for i in range(2, n//2+1):    
#     if i in a and n-i in a:
#         l.append(i)
#         l.append(n-i)

# for i in range(0,len(l)-1,2):
#     k.append(l[i+1]-l[i])
    
# index = k.index(min(k))*2
# print(l[index], l[index+1])