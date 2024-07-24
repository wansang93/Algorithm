def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_list(arr):
    res = arr[0]
    for v in arr[1:]:
        res = gcd(res, v)
    return res

def solution(arrayA, arrayB):
    gcd_a = find_gcd_of_list(arrayA)
    gcd_b = find_gcd_of_list(arrayB)
    
    gcd_a_available = all(b % gcd_a != 0 for b in arrayB)
    gcd_b_available = all(a % gcd_b != 0 for a in arrayA)
    
    answer = 0
    if gcd_a_available:
        answer = max(answer, gcd_a)
    if gcd_b_available:
        answer = max(answer, gcd_b)
    
    return answer
