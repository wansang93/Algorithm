T = int(input())
for t in range(1, T+1):
    string = input()

    string1 = '.'
    string2 = '.'
    string3 = '#'

    for c in string:
        string1 += '.#..'
        string2 += '#.#.'
        string3 += f'.{c}.#'

    print(string1)
    print(string2)
    print(string3)
    print(string2)
    print(string1)