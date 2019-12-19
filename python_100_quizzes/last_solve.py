maximum = int(input())
count1 = maximum // 7
count2 = 0
while count1 >= 0:
    rest = maximum-(count1*7)
    if rest % 3 == 0:
        count2 = rest // 3
        print(count1, count2)
        break
    else:
        count1 -= 1

if count1 == -1:
    print(count1)