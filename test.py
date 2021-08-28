# I/O template
import sys
file_path = (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin = open(file_path, 'r')

# Solve here

def solution(number, k):
    answer = []
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    
    answer = ''.join(answer[:len(answer)-k])

    return answer

print(solution("1924", 2))
