mystr = input()
newstr = ''

if len(mystr) < 50: 
    newstr = (50 - len(mystr)) // 2 * '='
    newstr += mystr
    newstr += (50 - len(newstr)) * '='
else:
    newstr = mystr

print(newstr)