def solution2(n):
    bi = list(bin(n)[2:])
    for i in range(len(bi)-2, -1, -1):
        if bi[i] == "0" and bi[i+1] == "1":
            bi[i], bi[i+1] = "1", "0"
            # print(i+1, end=' ')
            lo = i+1
            break
    else:
        lo = 2
        bi = list("10") + bi[1:]

    hi = len(bi) - 1
    while lo < hi:
        if bi[lo] == "0":
            lo += 1
        else:
            if bi[hi] == "0":
                print(lo, hi)
                bi[lo], bi[hi] = "0", "1"
                lo += 1
            hi -= 1
    return int(''.join(bi), 2)

def solution(n):
    bi = bin(n).count("1")
    while True:
        n += 1
        if bi == bin(n).count("1"):
            return n

print(solution(110))
print(solution(6))
