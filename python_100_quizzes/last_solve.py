mystr = input()
restr = mystr[::-1]
newstr = ""
if len(restr) > 3:
    for i, c in enumerate(restr):
        if i % 3 == 0:
            newstr = c + "," + newstr
        else:
            newstr = c + newstr
else:
    newstr = mystr + ","

print(newstr[:-1])