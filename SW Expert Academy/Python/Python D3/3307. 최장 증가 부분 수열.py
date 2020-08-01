import sys
sys.stdin = open(r'C:/Users/wansang/Desktop/Gitrep/Algorithm/SW Expert Academy/Python/Python D3/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    len_lst = len(lst)
    dp = [0] * (len_lst + 1)
    last_minimum = lst[0]
            
    answer = dp[-1]
    print(f'#{t} {answer}')

# 실패한 풀이1 제한시간 초과(재귀 사용)
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