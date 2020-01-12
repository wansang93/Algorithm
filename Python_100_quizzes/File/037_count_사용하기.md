# [문제37 : count 사용하기](https://www.notion.so/37-count-dc0e13c631da440cba8fa057bb9549b0)

새 학기를 맞아 호준이네 반은 반장 선거를 하기로 했습니다.  그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 **학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램**을 작성하기로 하였습니다.

**입력**
원범 원범 혜원 혜원 혜원 혜원 유진 유진
    
**출력**
혜원(이)가 총 4표로 반장이 되었습니다.

# 풀이37-1

``` python
mylist = input().split()
newlist = list(set(mylist))

leader = newlist[0]
for i in range(len(newlist)):
    if mylist.count(newlist[i-1]) < mylist.count(newlist[i]):
        leader = newlist[i]

print(leader + "(이)가 총 " + str(mylist.count(leader)) + "표로 반장이 되었습니다.")
```

set 함수를 이용해 자료의 중복성을 제거하고 후보명단을 만들어 후보명단 중에 가장 많은 득표의 사람을 반장으로 선정한다.

# 풀이37-2

``` python
mylist = list(map(str, input().split()))
num = 0
for i in range(len(mylist)):
	if mylist.count(mylist[i-1]) < mylist.count(mylist[i]):
		num = i
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(mylist[num], mylist.count(mylist[num])))
```

리스트 안의 요소의 순서대로 자료를 조회해보고 가장 많은 득표의 사람을 반장으로 선정한다.

# 풀이37-3

collections의 Counter를 사용해서 푸는 방법

``` python
from collections import Counter
mylist = list(map(str, input().split()))

def maxword(words):
	counter = Counter(words)
	max_count = -1
	for letter in counter:
		if counter[letter] > max_count:
			max_count = counter[letter]
			max_letter = letter
	return max_letter, max_count

name, num = maxword(mylist)
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(name, num))
```

collections의 Counter 예시

``` python
mylist = [1, 3, 3, 2, 2, 5]
counterlist = Counter(mylist)  # Counter 객체 생성
print(counterlist)  # Counter({'3': 2, '2': 2, '1': 1, '5': 1})
print(dir(counterlist))  # 객체에서 사용가능한 함수들
# '_keep_positive', 'clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys',
# 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'update', 'values'
```
