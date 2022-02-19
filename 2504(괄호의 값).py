# I/O template
import sys

FILE_INPUT_PATH =  (
    r'C:/Users/wansang/Desktop/Gitrep/Algorithm/' +
    r'test_input.txt'
)
sys.stdin  =  open(FILE_INPUT_PATH, 'r')

'''
m = {
    ')': '(',
    '}': '{',
    ']': '[',
}
stack = []
for i in e:
    if i in '({[':
        stack.append(i)
    elif i in m:
        if len(stack) == 0:
            break
        else:
            t = m[i]
            if t != stack.pop():
                break
'''
bracket = {
    '(': ')',
    '[': ']',
}

_string = input()
stack = []
answer = 0

now_value = 1
for c in _string:
    # 열기
    if c == '(':
        stack.append(c)
        now_value *= 2
    elif c == '[':
        stack.append(c)
        now_value *= 3
    
    # 닫기
    if not stack:
        answer = 0
        break

    last = stack.pop()
    if bracket[c] != last:
        break

    if last == '(':
        answer += now_value
        now_value //= 2
    elif last == '[':
        answer += now_value
        now_value //= 3

if stack:
    answer = 0

print(answer)