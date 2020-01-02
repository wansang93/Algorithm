# 데이터 입력(1), 프로그램 종료(2) : 1
# 데이터를 입력하세요: 3 + 5
# True

# 데이터 입력(1), 프로그램 종료(2) : 1
# 데이터를 입력하세요: 5 + 7) * (3 * 5)
# False

def math(e):
    is_ok = True
    stack = 0

    for c in e:
        if c == '(':
            stack += 1
        elif c == ')':
            stack -= 1
        
        if stack == -1:
            is_ok = False
            break

    if stack == 0 and is_ok == True:
        return True
    else:
        return False

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2): ')
    if order == '1':
        ex = input('데이터를 입력하세요: ')
        print(math(ex))
    else:
        break