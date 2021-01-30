# 2447 별 찍기 - 10

# # 규칙1. N == 1일때
#     # 빈공간 없음 return
# # 규칙2. N == 3일때
#     # x % 3 == 1 and y % 3 == 1
# # 규칙3. N == 9일때 빈공간 찾기
#     # (x/3) % 3 == 1 and y 도 똑같이
# # 규칙4. N == 27일때 빈공간 찾기
#     # (x/3/3) % 3 == 1 and y도 똑같이
# # 일반화
#     # (x / 3**(n-1)) % 3 == 1: 일때마다 빈 공간 생성

# # 입력값 받기 3의 몇승인지 체크
# # ex) 입력값이 3이면 3의 1승
# # ex) 입력값이 9이면 3의 2승
# # ex) 입력값이 27이면 3의 3승


# # for 문 작성 코드
# N = 81  # int(input())
# base = N
# e = 0
# while 1 < base:
#     base //= 3
#     e += 1


# star = [['*'] * N for _ in range(N)]

# for x in range(N):
#     for y in range(N):
#         if x % 3 == 1 and y % 3 == 1:
#             star[x][y] = ' '
#         elif (x//3) % 3 == 1 and (y//3) % 3 == 1:
#             star[x][y] = ' '
#         elif (x//3//3) % 3 == 1 and (y//3//3) % 3 == 1:
#             star[x][y] = ' '
#         elif (x//3//3//3) % 3 == 1 and (y//3//3//3) % 3 == 1:
#             star[x][y] = ' '

# print('\n'.join(star))

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a

print('\n'.join(star10(int(input()))))
