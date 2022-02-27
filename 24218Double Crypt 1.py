s = int(input())
p = input()  # plaintext
c2 = input()

# k1, k2를 구해라
# c2 = E(E(p, k1), k2)

# D(c2, k2) = D(E(E(p, k1), k2), k2)
# D(c2, k2) = E(p, k1)

# D(D(c2, k2), k1) = D(E(p, k1), k1)
# D(D(c2, k2), k1) = p
