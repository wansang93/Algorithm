a = input()
b = ""

for c in a:
    if c.islower() == 1:
        b += c.upper()
    elif c.isupper() == 1:
        b += c.lower()

print(b)