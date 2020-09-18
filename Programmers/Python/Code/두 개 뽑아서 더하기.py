# 내 풀이
def solution(numbers):
    answer = []
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers):
            if i != j:
                if numbers[i]+numbers[j] not in answer:
                    answer.append(numbers[i]+numbers[j])
    answer.sort()

    return answer

# 다른 사람 풀이
def solution2(numbers):
    answer = []
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(i+1, len_numbers):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))