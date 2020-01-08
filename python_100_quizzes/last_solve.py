a = [1,2,3,4]
b = ['a','b','c','d']
mylist = []

for i, j in zip(a, b):
    mylist.append([i, j])

mylist = [[i, j] for i, j in zip(a, b)]
print(mylist)