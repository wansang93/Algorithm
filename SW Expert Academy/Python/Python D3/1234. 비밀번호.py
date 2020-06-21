for t in range(1, 11):
    N, string = input().split()

    stack = []
    for c in string:   
        if stack != [] and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    answer = ''.join(stack)
    print(f'#{t} {answer}')