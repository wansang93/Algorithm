# [문제42 : 2020년(datetime 모듈 사용)](https://www.notion.so/42-2020-datetime-777b02bc144b4b1f82b7cf8cdd935c43)

2020년 1월 1일은 수요일입니다. 2020년 a월 b일은 무슨 요일일까요?
두 수 a, b를 입력받아 2020년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN, MON, TUE, WED, THU, FRI, SAT 입니다.

예를 들어 a = 5, b = 24라면 5월 24일은 일요일이므로 문자열 "SUN"를 반환하세요.

제한 조건
2020년은 윤년입니다.
2020년 a월 b일은 실제로 있는 날입니다. 
(13월 26일이나 2월 45일 같은 날짜는 주어지지 않습니다.)
datetime 모듈을 사용하세요.

# 풀이42-1

``` python
# print(dir(datetime))
# ['date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# print(dir(datetime.date))
# ['ctime', 'day', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'isocalendar', 'isoformat',
# 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 'today',
# 'toordinal', 'weekday', 'year']

import datetime

a, b = map(int, input().split())

def find_date(m, d):
    date = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return date[datetime.date(2020, m, d).weekday()]

print(find_date(a, b))
```