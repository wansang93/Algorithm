# 풀이1
def right(p):
    stack = []
    for i in p:
        if i == ')' and stack == []:
            return False
        if i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()  

    return True

def seperate(p):
    u = ''
    v = ''
    count = 0
    for i in p:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        u += i
        if count == 0:
            break
    
    for i in range(len(u), len(p)):
        v += p[i]

    return u, v

def solution(p):
    if p == '':
        return ''

    if right(p) == True:
        return p

    u, v = seperate(p)

    v = solution(v)
    if right(u):
        return u + v
    else:
        temp = '(' + v + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                temp += ')'
            elif i == ')':
                temp += '('
        return temp

print(solution('()))((()'))

# 풀이2

# right 함수를 스택을 사용하지 않고 카운트로 판단하여 참거짓 하기
# 스택보다 효율이 많이 올란간다.
def right2(p):
    count = 0
    for i in p:
        if i == ')' and count == 0:
            return False
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1  

    return count == 0


# 나누기에서 리스트 인덱싱을 활용하여 나누기
def seperate2(p):
    l = r = 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        elif p[i] == ')':
            r += 1
        if l == r and l > 0:
            return p[:i+1], p[i+1:]