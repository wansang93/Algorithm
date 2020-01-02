# 데이터 입력(1), 프로그램 종료(2) : 1
# 데이터를 입력하세요: 3 + 5
# True

# 데이터 입력(1), 프로그램 종료(2) : 1
# 데이터를 입력하세요: 5 + 7) * (3 * 5)
# False

def math(e):
    mylist =[]
    is_ok = True

    for c in e:
        if c in '({[':
            mylist.append(c)
        elif c == ')':
            if '(' == mylist.pop():
                pass
            else:
                is_ok = False
                break
        elif c == '}':
            if '{' == mylist.pop():
                pass
            else:
                is_ok = False
                break
        elif c == ']':
            if '[' == mylist.pop():
                pass
            else:
                is_ok = False
                break
    if mylist == [] and is_ok == True:
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
