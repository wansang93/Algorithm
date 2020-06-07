# 풀이1: using a for loop
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        i = i.capitalize()
        answer += i + ' '
    return answer[:-1]


# 풀이2: using list comprehension
def solution2(s):
    answer = ' '.join([i.capitalize() for i in s.lower().split(' ')])   
    return answer

# 실패한 풀이: 정답률(43.8%) 런타임 에러
# test case -> ' 1//cdf dfasdfc FFDSDF dsafDFfndf '
# 시작이나 끝이 ' '(공백)일 경우 에러 발생
def solution3(s):
    string = s.lower().split(' ')
    jd = []
    for ss in string:
        print(ss)
        if len(ss) > 1:
            jd.append(ss[0].upper() + ss[1:])
        else:
            jd.append(ss[0].upper())
    answer = ' '.join(jd)
    return answer