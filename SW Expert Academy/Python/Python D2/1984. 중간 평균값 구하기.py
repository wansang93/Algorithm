# 풀이1: 탐색을 2번한다.
T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    avg = round((sum(nums)-min(nums)-max(nums))/(len(nums)-2))

    print('#{} {}'.format(i, avg))

# 풀이2: 탐색을 1번한다.
T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    max_num = 0
    min_num = 10000
    for j in nums:
        if max_num < j:
            max_num = j
        if min_num > j:
            min_num = j
    
    avg = round((sum(nums)-max_num-min_num)/8)

    print('#{} {}'.format(i, avg))
