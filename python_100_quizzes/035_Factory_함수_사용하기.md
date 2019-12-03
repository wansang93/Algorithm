# [문제35 : Factory 함수 사용하기](https://www.notion.so/35-Factory-cd9fdd4e7e694cb5b0f57761c90e4e04)

2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수를 만들려고 합니다. 

- <pass>에 코드를 작성하여 two함수를 완성하세요.

    def one(n):
        def two(m):
            <pass>
        return two
    
    a = one(2)
    b = one(3)
    c = one(4)
    print(a(10))
    print(b(10))
    print(c(10))


# 풀이35-1

``` python
def one(n):
    def two(m):
        squar = m ** n
        return squar
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))
```

- 순서
    - a = one(2) 실행
    - one함수 호출 및 파라마타 n=2
    - one함수안의 return 값인 two 함수를 불러오고 종료
    - a = two 함수의 정의로 저장
    - b, c 도 a와 같이 실행
    
    - print(a(10)) 실행
    - a(10)을 실행할 때 two(10)을 실행한거와 마찬가지
    - 파라마타 m=10, 이전에 n=2 가 저장되어있음
    - squar = 10 ** 2 실행
    - squar값 반환하고 프린트
    - b, c 도 a와 같이 실행