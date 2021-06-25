def solution(s):
    stack = []
    
    # s 탐색
    for i in s:
        # s가 ( 일때
        if i == '(':
            stack.append('(')
        # s가 ) 일때
        elif i == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
                
    if not stack:
        return True
    return False