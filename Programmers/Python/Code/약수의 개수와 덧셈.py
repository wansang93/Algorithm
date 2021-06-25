# 약수의 갯수가 홀수인 경우는 제곱수뿐만인 경우를 고려해서 품
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i ** (1/2) == int(i ** (1/2)):
            answer -= i
        else:
            answer += i
    return answer


# 약수 구하기
def solution2(left, right):
    answer = 0
    for i in range(left, right+1):
        divisor = []
        for j in range(1, i + 1):
            if i % j == 0:
                divisor.append(j)
        if len(divisor) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer
