# 팩토리얼(Factorial)과 이항 계수(Binomial Coefficient)

## 팩토리얼(Factorial)

### 1. 0이 아닌 마지막 수(Last Non Zero Digit in a Factorial)

TODO: 업데이트

### 2. N!의 0의 갯수

[백준 3474](https://www.acmicpc.net/problem/3474)

```python
N = int(input())

ans = 0
i = 5
while i <= N:
    ans += N // i
    i *= 5

print(ans)
```

## 이항 계수(Binomial Coefficient)
