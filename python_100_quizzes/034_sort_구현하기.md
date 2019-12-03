# [문제34 : sort 구현하기](https://www.notion.so/34-sort-3c7374965a1549d59b17d15c32eba8f5)

민주는 체육부장으로 체육시간이 되면 반 친구들이 제대로 키 순서대로 모였는지를 확인해야 한다. 그런데 요즘 민주는 그것이 너무 번거롭게 느껴져 한 번에 확인하고 싶어한다. 

민주를 위해 **키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램**을 작성해보자.

**입출력 예시**

입력 : 176 156 155 165 166 169
출력 : NO


# 풀이34-1
``` python
mylist = input().split()
newlist = sorted(mylist)
if mylist != newlist:
    print("NO")
```
