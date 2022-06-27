import math

def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
    k -= 1
    while nums:
        index = k // math.factorial(n-1)
        answer.append(nums.pop(index))
        
        k %= math.factorial(n-1)
        n -= 1

    return answer

data1 = 3, 5
print(solution(*data1))
