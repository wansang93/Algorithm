# 풀이1
def solution(a, b):
    answer = ''
    count = 4
    date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    dal_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    
    answer = date[(sum(dal_day[0:a]) + b + count) % 7]
    return answer