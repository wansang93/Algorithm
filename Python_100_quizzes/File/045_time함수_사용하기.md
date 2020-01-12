# [문제45 : time함수 사용하기](https://www.notion.so/45-time-9b547ab4cc47431f9111f0e38a61d647)

python의 모듈 중 하나인 time 모듈은

``1970년 1월 1일 0시 0분 0초``

이후로부터 지금까지 흐른 시간을 초단위로 반환합니다

이를 이용하여 현재 연도(2019)를 출력해보세요

# 풀이45-1

``` python
now_time = time.time()
now_time -= 12*60*60*24  # 1970년부터 2019년까지는 윤달이 12번 있었다.

now_year = int(now_time//(60*60*24*365)+1970)
print(now_year)
```

# 풀이45-2

현재 년도 구하기, 현재 날짜 구하기
``` python
# 현재 년도 구하기
LEAP_YEAR = 12  # 1970년부터 2019년까지는 윤년이 12번 있었다.
set_time = now_time - LEAP_YEAR*60*60*24  # 윤년의 날짜만큼의 초를 빼주어 1년을 365일로 하였다.
past_year = int(set_time//(60*60*24*365))  # 지나간 시간(초) // 1년(초) = 지나간 연도(년)
print("지나간 해: {}년".format(past_year))
now_year = int(past_year+1970)
print("현재 년도: {}년".format(now_year))

# 현재 날짜 구하기
check_days = (set_time - (past_year*(60*60*24*365)))
# 지나간 시간(초) - 현재까지 지나간 연도만(초) = 현재까지의 일수(초)
print("2019년 1월 1일부터 현재까지 날짜는: {}초".format(check_days))
past_days = int(check_days // (60*60*24))  # 현재까지의 일수(일)
print("지나간 일수: {}일".format(past_days))
# 2019년 1월 1일부터 현재(2019년 12월 11일)까지는 344일이다.
A_DAY = 333  # 2019년 1월 1일부터 12월 전날(2019년 11월 30일)까지는 333일이다.
now_days = int((check_days - 60*60*24*A_DAY) // (60*60*24))
print("현재 날짜: {}일".format(now_days))
```