mylist = input().split()
newlist = sorted(mylist)
if mylist != newlist:
    print("NO")
else:
    print("OK")