def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = change(n, k)
    lst = num.split('0')
    for i in lst:
        if i != '':
            if is_prime_number(int(i)):
                answer += 1

    return answer

data1 = 437674
data11 = 3

data2 = 110011
data22 = 10

print(solution(data1, data11))  # 3
print(solution(data2, data22))  # 2