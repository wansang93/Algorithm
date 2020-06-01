p, k = list(map(int, input().split(' ')))
answer = 0

while k <= p:
    answer += 1
    k += 1

print(answer)