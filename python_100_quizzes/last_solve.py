# 18234 = 1+8+2+3+4 이고 정답은 18 입니다.
# 3849 = 3+8+4+9 이고 정답은 24입니다.
num = input()
sum = 0
for i in num:
    sum += int(i)
print(sum)