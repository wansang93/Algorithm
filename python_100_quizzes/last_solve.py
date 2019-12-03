
mylist = input().split()
newlist = mylist[::-1]
for i in range(len(newlist)):
    print(newlist[i], end=" ")