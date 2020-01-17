def solution(dartResult):
    answer = 0
    scorelist = [str(i) for i in range(1, 10)]
    newlist = ['0']
    for i in dartResult:
        if i in scorelist:  # 1~9까지의 수
            newlist.append('+')
            newlist.append(i)
        elif i == '0':  # 0일 때
            if newlist[-1] == '1':
                newlist.append(i)
            else:
                newlist.append('+')
                newlist.append(i)
        elif i in ['S', 'D', 'T']:  # S, D, K 일때
            if i == 'S':
                newlist.append('**1')
            elif i == 'D':
                newlist.append('**2')
            elif i == 'T':
                newlist.append('**3')
        elif i in ['*', '#']:  # *, # 일때
            if i == '*':
                if newlist[-3] == '+':
                    newlist[-3] = '*2+'
                newlist.append('*2')
            elif i == '#':
                newlist.append('*(-1)')
    answer = eval(''.join(newlist))
    return answer

# dartResult = '1D2S#10S'
# print(solution(dartResult))