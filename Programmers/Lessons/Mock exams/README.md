# 모의테스트 해설강의

링크: [https://programmers.co.kr/learn/courses/18](https://programmers.co.kr/learn/courses/18)

기간: 2020.06.05 ~ 2020.06.

### 파트1. 자릿수 더하기 문제

``` python

```


### 파트2. 순열 검사 문제

길이가 n인 배열에 1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는지를 확인하려고 합니다.

1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는 경우 true를, 아닌 경우 false를 반환하도록 함수 solution을 완성해주세요.

``` python
def solution(arr):

    check_list = [0 for _ in range(len(arr))]
    
    for i in arr:
        if i > len(check_list):
            return False
        check_list[i-1] += 1

    for i in check_list:
        if i != 1:
            return False

    return True
```

``` python
def solution(arr):
    arr.sort()
    
    for i, j in zip(arr, [i for i in range(1, len(arr)+1)]):
        if i != j:
            return False

    return True
```

``` python
def solution(arr):
    arr.sort()
    
    for i in range(len(arr)):
        if arr[i] != i+1:
            return False
    return True
```

### 파트3. 나머지 한 점 문제

``` python

```


### 파트4. 가장 큰 정사각형 찾기 문제

``` python

```


### 파트5. 땅따먹기 문제

``` python

```

### 파트6. 스티커 모으기 문제

``` python

```

### 파트7. 단어 퍼즐 문제

``` python

```
