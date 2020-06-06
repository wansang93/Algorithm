# 모의테스트 해설강의

링크: [https://programmers.co.kr/learn/courses/18](https://programmers.co.kr/learn/courses/18)

기간: 2020.06.05 ~ 2020.06.06

### 파트1. 자릿수 더하기 문제

- 문제

    자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.

    예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

- 풀이

    1. 각 자리수의 숫자를 글자로 만든다.
    2. 글자로 만든 것을 리스트로 만든다.
    3. 리스트의 글자들을 숫자로 바꾼뒤 더한다.

    ``` python
    def solution(n):
        answer = sum(map(int, list(str(n))))

        return answer
    ```

    1. 숫자는 10진법으로 되어있기 때문에 각 자릿수의 값을 구하면 된다.
    2. 숫자를 10으로 나눈 나머지를 정답에 더하고 몫을 다시 숫자에 넣는다.
    3. 숫자가 0보다 클 때 까지 반복한다.
    ``` python
    def solution(n):
        answer = 0
        while n > 0:
            answer += n % 10
            n //= 10
        return answer
    ```

### 파트2. 순열 검사 문제

- 문제

    길이가 n인 배열에 1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는지를 확인하려고 합니다.

    1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는 경우 true를, 아닌 경우 false를 반환하도록 함수 solution을 완성해주세요.

- 풀이

    1. 체크 리스트를 만든다.
    2. 배열에 숫자를 하나씩 꺼내서 체크리스트의 칸에 True로 바꾼다.
    3. 단, 꺼낸 숫자가 체크리스트의 길이보다 크면 False를 리턴한다.
    4. 또는 꺼낸 숫자가 이미 체크리스트에 True로 있으면 False를 리턴한다.
    5. True를 리턴한다.
    ``` python
    def solution(arr):

        check = [False] * (len(arr)+1)

        for i in arr:
            if i > len(arr) or check[i]:
                return False
            check[i] = True

        return True
    ```

    1. 배열을 정렬한다.
    2. 정렬한 배열과 1부터 n까지 배열을 하나씩 꺼내 비교한다.
    3. 비교한 부분이 다르면 False를 리턴한다.
    4. 아니면 True를 리턴한다.

    ``` python
    def solution(arr):
        arr.sort()
        
        for i, j in zip(arr, [i for i in range(1, len(arr)+1)]):
            if i != j:
                return False

        return True
    ```

    1. 배열을 정렬한다.
    2. 정렬한 배열에 값을 하나씩 꺼내 1부터 순서대로 있는지 확인한다.
    3. 순서대로 없을 때 False로 리턴한다.
    4. 끝까지 탐색하여 성공하면 True를 리턴한다.
    ``` python
    def solution(arr):
        arr.sort()
        
        for i in range(len(arr)):
            if arr[i] != i+1:
                return False

        return True
    ```

### 파트3. 나머지 한 점 문제

- 문제

    직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다.
    
    점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요.
    
    단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.

- 풀이

    조건문을 이용한 풀이

    ``` python
    def solution(v):
    answer = v[0]

    if v[0][0] == v[1][0]:
        answer[0] = v[2][0]

    elif v[0][0] == v[2][0]:
        answer[0] = v[1][0]

    if v[0][1] == v[1][1]:
        answer[1] = v[2][1]

    elif v[0][1] == v[2][1]:
        answer[1] = v[1][1]

    return answer
    ```

    XOR 원리를 이용한 풀이
    
    ``` python
    def solution(v):
    x2 = v[0][0] ^ v[1][0] ^ v[2][0]
    y2 = v[0][1] ^ v[1][1] ^ v[2][1]
    return [x2, y2]
    ```

### 파트4. 가장 큰 정사각형 찾기 문제

- 문제

    1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
    
    표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요.(단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

    예를 들어 다음과 같은 표가 있다면, 가장 큰 정사각형의 넓이는 9가 되므로 9를 반환해 주면 됩니다.

    | 1 | 2 | 3 | 4 |
    |:-:|:-:|:-:|:-:|
    | 0 | 1 | 1 | 1 |
    | 1 | 1 | 1 | 1 |
    | 1 | 1 | 1 | 1 |
    | 0 | 0 | 1 | 0 |

- 풀이


``` python

```


### 파트5. 땅따먹기 문제

- 문제

    땅따먹기 게임을 하려고 합니다.
    
    땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다.
    
    1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
    
    단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

- 풀이

    ``` python
    def solution(land):
        land.insert(0, [0, 0, 0, 0])

        for i in range(1, len(land)):
            for j in range(4):
                first, second, third = [i for i in range(4) if i != j]      
                land[i][j] += max(land[i-1][first], land[i-1][second], land[i-1][third])

        answer = max(land[len(land)-1])
        return answer
    ```
 
    1. 결국 가장 중요한 것은 마지막 줄이다. 마지막 줄을 계속 갱신해 나가면 정답을 출력할 수 있다.
    2. 먼저 마지막 줄을 [0] * 4 로 만든다.
    3. 한 줄씩 읽어와 마지막 줄과 읽어온 줄을 비교하며 계산한다. 비교 방법은 다음과 같다.
    4. 마지막 줄에 들어갈 숫자는 자기자신 + 이전 자신의 위를 제외한 숫자들의 최댓값이다.
    ``` python
    def solution2(land):
        sum_list = [0]*4
        
        for row in land:
            tmp = sum_list.copy()
            for i in range(4):
                sum_list[i] = row[i] + max(tmp[:i] + tmp[i+1:])

        return max(sum_list)
    ```

### 파트6. 스티커 모으기 문제

- 문제

    N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.

    ![스티커](./data/스티커.jpg)

    원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다.
    
    단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

    예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다.
    
    스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요.
    
    원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.
    
``` python

```

### 파트7. 단어 퍼즐 문제

``` python

```
