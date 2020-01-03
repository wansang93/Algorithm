# [17,12,13,72,73,23]
# 73

from itertools import permutations

newdata = input()
num = int(input())

print(permutations(newdata, num))
# <itertools.permutations object at 0x00000237FE147DC8>
print(list(permutations(newdata, num)))
# [('1', '7'), ('1', '2'), ('1', '3'), ('7', '1'), ('7', '2'), ('7', '3'),
# ('2', '1'), ('2', '7'), ('2', '3'), ('3', '1'), ('3', '7'), ('3', '2')]
print(map(''.join, (permutations(newdata, num))))
# <map object at 0x00000237FE15A848>
print(list(map(''.join, (permutations(newdata, num)))))
# ['17', '12', '13', '71', '72', '73', '21', '27', '23', '31', '37', '32']
print(max(list(map(''.join, (permutations(newdata, num))))))
# 73

# 풀이84-3

def permutation(arr, r):
    result = []
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            result.append(''.join(map(str, chosen)))
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    print(result)
    print(max(result))


permutation('ABCD', 2)
permutation([1, 2, 3, 4, 5], 3)

# 풀이84-2

from itertools import permutations

user_input = input()
k = int(input())
l = [i for i in user_input]

print(max(list(map(''.join, permutations(l, k)))))