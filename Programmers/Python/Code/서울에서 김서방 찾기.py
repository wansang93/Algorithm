# 풀이1
def solution(seoul):
    answer = ''

    for index, name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 " + str(index) + "에 있다"

    return answer

# 풀이2
def solution2(seoul):
    i = seoul.index('Kim')
    answer = '김서방은 {}에 있다'.format(i)
    
    return answer