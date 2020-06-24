from itertools import combinations

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))

    sums = []
    for i in combinations(numbers, r=3):
        sums.append(sum(i))
    
    sums.sort(reverse=True)
    answer = list(set(sums))[4]

    print(f'#{t} {answer}')