def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        bin_num = '0' + bin(number)[2:]
        idx = bin_num.rfind('0')
        lst_bin_num = list(bin_num)
        lst_bin_num[idx] = '1'
        lst_bin_num[idx+1] = '0'
        answer.append(int(''.join(lst_bin_num), 2))

    return answer


# 바이너리로 풀기
"""
1. val + 1비트를 더한다.
2. val + (var + 1비트를 더한 값)을 xor을 한 것을 >> 2만큼 쉬프트한다.
    (왜그런지는 모르겠다.)
3. 1 + 2 를 더한다.
"""
def solution2(numbers):
    answer = []
    for val in numbers:
        answer.append(((val ^ (val+1)) >> 2) + val + 1)

    return answer


print(solution2([2, 7]))
