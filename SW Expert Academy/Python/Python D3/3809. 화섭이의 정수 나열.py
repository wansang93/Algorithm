# 참고 URL  [https://jksk0115.tistory.com/25]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = []
    while len(nums) < N: 
        nums += list(input().split())
    # print(nums)

    answer = -1
    check_nums = [False] * 10000
    len_nums = len(nums)

    for digit in range(1, 5):
        for i in range(N-(digit-1)):
            check_nums[int(''.join(nums[i:i+digit]))] = True
            # print(nums[i:i+digit])
        
        start = 0 if digit == 1 else 10 ** (digit - 1)
        end = 10 ** digit

        for i in range(start, end):
            if not check_nums[i]:
                answer = i
                break
        else:
            continue
        break

    print(f'#{t} {answer}')