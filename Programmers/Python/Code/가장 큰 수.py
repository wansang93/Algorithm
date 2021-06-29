# 풀이1
def solution(numbers):
    num = sorted(map(str, numbers), key=lambda x: x*3 ,reverse=True)
    return str(int(''.join(num)))
    
# 1. 문자열로 바꾼다.
# 2. 정렬한다. 정렬할 때 *3을 하는 이유는 3자리 수이기 때문
# 2-1. 예시) 332, 333, 334 -> 332332332, 333333333, 3343334334 변경후 값 비교
# 3. 내림차순으로 하고 문자열로 이어준다.


# 잘못된 풀이(시간 초과)
from itertools import permutations
def solution2(numbers):
    permute = list(permutations(numbers))
    permute_lst = [''.join(map(str, i)) for i in permute]
    return max(permute_lst)

print(solution([3, 30, 34, 5, 9]))
print(solution2([3, 30, 34, 5, 9]))
