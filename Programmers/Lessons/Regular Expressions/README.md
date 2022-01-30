# Regular Expressions

2020-06-11 ~ 2020-06-12 (2Days) Finished

Site Link -> [https://programmers.co.kr/learn/courses/11](https://programmers.co.kr/learn/courses/11)

## How to use Python

``` python
# 전화번호 찾는 방법
regex = r'\d{2,3}[- ]?\d{3,4}[- ]?\d{4}'

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드입니다.
import re
result = re.findall(regex, search_target)
print("\n".join(result))
```

## Another Sites

Site Link -> [https://cs.lmu.edu/~ray/notes/regex/](https://cs.lmu.edu/~ray/notes/regex/)

Practice Link -> [https://regexone.com/](https://regexone.com/)

### REGEXONE Problem

#### Problem 1: Matching a decimal numbers

```text
my answer: -?\d+[\.,]?\d+[\.,e]?\d*[^p]$

solution: ^-?\d+(,\d+)*(\.\d+(e\d+)?)?$
```

#### Problem 2: Matching phone numbers

```text
my answer: (\d{3})

solution: (\d{3})
```

#### Problem 3: Matching emails

```text
my answer: ^([a-z\.]*)

solution: ^([\w\.]*)
```

#### Problem 4: Matching HTML

```text
my answer: <(\w+).

solution: <(\w+)
```

#### Problem 5: Matching specific filenames

```text
my answer: (.*)\.(jpg|png|gif)$

solution: (\w+)\.(jpg|png|gif)$
```

#### Problem 6: Trimming whitespace from start and end of line

```text
my answer: ^[\s]*(.*)

solution: ^\s*(.*)\s*$
```

#### Problem 7: Extracting information from a log file

```text
my answer: (\w+)\(([\w\.]+):(\d+)\)

solution: (\w+)\(([\w\.]+):(\d+)\)
```

#### Problem 8: Parsing and extracting data from a URL

```text
my answer: (\w+)://([\w\-\.]+)(:(\d+))?

solution: (\w+)://([\w\-\.]+)(:(\d+))?
```
