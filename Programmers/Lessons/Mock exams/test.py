def solution(arr):

    check_list = [0 for _ in range(len(arr))]
    
    for i in arr:
        if i > len(check_list):
            return False
        check_list[i-1] += 1

    for i in check_list:
        if i != 1:
            return False

    return True


def solution2(arr):
    arr.sort()
    
    for i, j in zip(arr, [i for i in range(1, len(arr)+1)]):
        if i != j:
            return False

    return True


def solution3(arr):
    arr.sort()
    
    for i in range(len(arr)):
        if arr[i] != i+1:
            return False
    return True

print(solution([4, 1, 3, 2]))