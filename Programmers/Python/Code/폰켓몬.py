def solution(nums):
    species = len(set(nums))
    N = len(nums) // 2
    if N <= species:
        return N
    return species

# 다른 사람 풀이
def solution(nums):
    return min(len(set(nums)), len(nums)//2)