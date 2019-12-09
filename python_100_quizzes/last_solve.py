num = int(input())
mystr = ""
while num:
    print(num)
    mystr += str(num % 2)
    num = int(num / 2)
print(int(mystr))