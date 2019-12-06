# 입력

# 50 무게제한
# 5  사람 수
# 20
# 20
# 20
# 20
# 20

limit = int(input())
num = int(input())
mylist = []
for i in range(num):
    mylist.append(int(input()))

count = 0
sum = 0
for i in mylist:
    sum += i
    count += 1
    if sum > limit:
        count -= 1
        break

print(count)
