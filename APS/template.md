# CodingTest is Template

## 0. Basic

### 0-1. I/O

```python
# 문자 받기
string_ = input()

# int형 1개 받기
int_ = int(input())

# 문자열 띄어쓰기 기준으로 받기
string_ = input().split()

# int형 띄어쓰기 기준으로 3개 받기
a, b, c = map(int, input().split())

# int형 1줄을 리스트로 받기
lst = list(map(int, input().split()))

# 2차원 리스트 만들어서 넣기
"""Input
3 4
0 1 2 3 
4 5 6 7
8 9 10 11
"""
R, C = map(int, input().split())
lst2d = [list(map(int, input().split()) for _ in range(R))]
```

### 0-2. Condition

### 0-3. For Loop

```python
# 10개 출력

# 1~N까지 출력

# 17~8까지 출력

# Z부터 A까지 출력

# 별 1, 2, 3, 4, 5 찍기

# 구구단 찍기
```

### 0-4. While Loop

### 0-5. Recursive Fuction
