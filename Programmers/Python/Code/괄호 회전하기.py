def solution(s):
    answer = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        stack = []
        for j in new_s:
            if j in ('(', '{', '['):
                stack.append(j)
            elif j == ')':
                if not stack:
                    break
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    break
            elif j == ']':
                if not stack:
                    break
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    break
            elif j == '}':
                if not stack:
                    break
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
    return answer
