# 풀이1
def solution(s):
    s = s.upper()
    answer = ''
    num = 0  # 홀짝 판별기
    for i in s:
        if i == ' ':  # 단어 공백 판별기
            answer += i
            num = 0
        elif i != ' ':
            if num % 2 == 0:
                answer += i
                num += 1
            else:
                answer += i.lower()
                num += 1
    
    return answer

# 풀이2
def solution2(s):
    answer = ''
    for c in s.lower().split(' '):
        n = 0
        for i in c:
            if n % 2 == 0:
                answer += i.upper()
                n += 1
                continue
            else:
                answer += i
                n += 1
        answer += ' '
    answer = answer[0:-1]
    return answer

print(solution2('try hello world'))

# 풀이3
def solution3(s):
    answer = []
    s = s.lower().split(' ')
    for c in s:
        word = ''
        for i, l in enumerate(c):
            if i % 2 == 0:
                l = l.upper()
            word += l
        answer.append(word)
    answer = ' '.join(answer)
    return answer