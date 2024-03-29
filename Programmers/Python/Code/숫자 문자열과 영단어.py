def solution(s):
    str_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    answer = s
    for key, value in str_to_num.items():
        answer = answer.replace(key, str(value))

    return int(answer)
