i = int(input())
answer = 0

while 0 < i:
    answer += i % 10
    i = i // 10

print(answer)