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