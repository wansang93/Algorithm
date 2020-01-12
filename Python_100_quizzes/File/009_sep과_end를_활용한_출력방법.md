# [문제9 : sep과 end를 활용한 출력방법](https://www.notion.so/9-sep-end-024533faffe04f2bb1616dd2eb7a559f)

다음 소스 코드를 완성하여 날짜와 시간을 출력하시오.
``` python
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'
```
출력
``` python
2019/04/26 11:34:27
```

# 풀이9-1
``` python
print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")
```