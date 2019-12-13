#    입력1
#     1 2 4 3 5

#     출력1
#     YES


#     입력2
#     1 4 2 6 3

#     출력2
#     NO

mylist = list(map(int, input().split()))

print(mylist)

first = mylist[0]
if mylist == [i for i in range(first, first+len(mylist))]:
    print("YES")
else:
    print("NO")