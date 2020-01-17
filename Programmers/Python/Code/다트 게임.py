def solution(dartResult):
    answer = 0
    newlist = ['0']
    for i in dartResult:
        if i in ['1', '2', '3']:
            newlist.append('+%c' % i)
        elif i in ['S', 'D', 'T']:
            if i == 'S':
                newlist.append('**1')
            elif i == 'D':
                newlist.append('**2')
            elif i == 'T':
                newlist.append('**3')
        elif i in ['*', '#']:
            if i == '*':
                newlist.append('*2')
            elif i == '#':
                newlist.append('*(-1)')

    newstr = ''.join(newlist)
    print(int(newstr))

    return answer

dartResult = '1S2D*3T'
print(solution(dartResult))