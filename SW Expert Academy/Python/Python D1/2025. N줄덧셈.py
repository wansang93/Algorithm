# 1부터 주어진 숫자만큼 더하시오

num = int(input())
answer = 0

for i in range(1, num+1):
    answer += i

print(answer)


# 개선

i = int(input())
print((i * (i+1)) // 2)