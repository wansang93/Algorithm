# 풀이2: dp를 이용한 풀이
# 참고 https://www.youtube.com/watch?v=td8JCnqt-JI
T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    dp = [1] * N
    # # count 변수는 lis의 숫자를 나타냄
    # count = [1] * N
    
    for i in range(N):
        for j in range(i):
            if lst[i] > lst[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    # count[i] = count[j]
                # elif dp[j] + 1 == dp[i]:
                    # count[i] += count[j]
    
    answer = max(dp)
    # sum([count[i] for i in range(N) if dp[i] == answer])
    print(f'#{t} {answer}')

# # 실패한 풀이1: 제한시간 초과(재귀 사용)
# answer = 0
# def solve(last_max, count, cur):
#     global answer
#     if answer < count:
#         answer = count
#     if len_lst <= cur:
#         return

#     value = lst[cur]
#     new_last_max = last_max
#     new_count = count
#     if last_max <= value:
#         new_last_max = value
#         new_count += 1

#     cur += 1
#     solve(last_max, count, cur)
#     solve(new_last_max, new_count, cur)

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     len_lst = len(lst)

#     solve(0, 0, 0)
#     print(f'#{t} {answer}')
#     answer = 0
