def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1):
            if i != j:
                num = numbers[i] + numbers[j]
                if num not in answer:
                    answer.append(num)

    answer.sort()

    return answer

print(solution([2,1,3,4,1]))