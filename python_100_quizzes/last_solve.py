
#    aaabbbbcdddd

mystr = input()
newstr = mystr[0]

count = 0
for c in mystr:
    if newstr[-1] == c:
        count += 1
    else:
        newstr += str(count)+c
        count = 1

newstr += str(count)

print(newstr)