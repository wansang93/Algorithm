T = 10

for tc in range(1, T+1):
    answer = 1
    N = int(input())
    bracket = input()
    stack = []

    for b in bracket:
        if b in ['(', '[', '{', '<']:
            stack.append(b)
        elif b == ')':
            if stack and stack.pop() == '(':
                continue
            else:
                answer = 0
                break
        elif b == ']':
            if stack and stack.pop() == '[':
                continue
            else:
                answer = 0
                break
        elif b == '}':
            if stack and stack.pop() == '{':
                continue
            else:
                answer = 0
                break
        elif b == '>':
            if stack and stack.pop() == '<':
                continue
            else:
                answer = 0
                break

    if stack:
        answer = 0

    print(f'#{tc} {answer}')
