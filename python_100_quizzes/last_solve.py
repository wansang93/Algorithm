# 입력 : 'ABCDEFGH' 4
# 출력 : 'EFGHIJKL', 'EFGHIJKM', 'EFGHIJKZ' 등 4개의 요소가 같은 약품 전부

import random as r

# medicine = []  # ex) [['S', 'K', 'O', 'A', 'D', 'Y', 'L', 'F'], ...]

# for i in range(8):
#     medicine.append(r.choice(l))

l = [chr(i) for i in range(65, 91)]
total_medicine = []  # ex) ['Y', 'J', 'K', 'U', 'A', 'T', 'F', 'V']
for i in range(100):
    total_medicine.append(r.sample(l, 8))

medicine = input().split()
result = []

for i in total_medicine:
    if len(set(i) & set(medicine[0])) == int(medicine[1]):
        result.append(i)

print(len(result))