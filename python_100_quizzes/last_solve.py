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

# 풀이2

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

# 풀이3

# num = int(input('2보다 큰 짝수를 입력해주세요 : '))
# ans = []

# def chk(n): #소수구하는 함수
#     for i in range(2,n):
#         if n%i==0: #2부터 n-1까지 나누어지는 수가 있다면
#             break #break
#     if i==(n-1): #위의 break에 걸리지 않았다면 소수
#         return n #n을 리턴
#     else:
#         return False #아니라면 False

# for j in range(3, num//2+1): # 3부터 입력받은 수의 절반까지 for문
#     if chk(j): # 만약 j가 소수라면
#         if chk(num-j): # 입력받은 수 - j가 소수라면
#             ans.append([j, num-j]) # 답 집어넣기

# print(ans)