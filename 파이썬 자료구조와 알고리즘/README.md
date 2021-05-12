# 파이썬 자료구조와 알고리즘

2021-04-24 ~ 2021-04-25

우재남 선생님

# 코드 리뷰

## 3장 선형 리스트

### Code 03-01 선형 리스트 생성

```python
katok = []

def add_data(friend):
    # 리스트 끝에 빈칸 추가하기
    katok.append(None)
    # 리스트 길이 받아오기
    k_len = len(katok)
    # 리스트의 마지막에 친구 추가하기
    katok[k_len-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
# ['다현', '정연', '쯔위', '사나', '지효']
```

### Code 03-02 선형 리스트 수정

```python
katok = ['다현', '정연', '쯔위', '사나', '지효']

def insert_data(position, friend):
    # 리스트 끝에 빈칸 추가하기
    katok.append(None)
    k_len = len(katok)
    for i in range(k_len-1, position, -1):
        katok[i] = katok[i-1]
    katok[position] = friend

insert_data(3, '솔라')

print(katok)
# ['다현', '정연', '쯔위', '솔라', '사나', '지효']
```

### Code 03-03 선형 리스트 삭제

```python
katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position):
    # 리스트 끝에 빈칸 추가하기
    k_len = len(katok)
    katok[position] = None
    for i in range(position+1, k_len):
        katok[i-1] = katok[i]
        katok[i] = None
    
    del(katok[k_len-1])

delete_data(3)
delete_data(1)

print(katok)
# ['다현', '쯔위', '지효']
```

## 4장 연결 리스트의 CUD(Create, Read, Delete)

연결리스트는 순서도 있으면서 선형 리스트보다 수정 작업이 더 원활하다.

### 04-01 연결 리스트 기본 생성 

```python
class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정현'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5
```

출력

```python
print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')
# 다현 정현 쯔위 사나 지효
```

### Code 04-02 연결 리스트 기본 출력 개선

```python
current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')
```

### Code 04-03 연결 리스트 기본 수정(삽입)

```python
newNode = Node()
newNode.data = "완상"
newNode.link = node2.link   # 정연의 링크
node2.link = newNode
```

### Code 04-04 연결 리스트 기본 삭제

```python
node2.link = node4
del(node3)
```

### Code 04-05 연결 리스트 일반적인 구현

```python
class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


# 전역 변수
memory = []
head, current, pre = [None] * 3
# 데이터베이스에서 불럴왔다고 생각하면 됨
data_array = ['다현', '정연', '쯔위', '사나', '지효']

# 메인 코드
if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
    print_nodes(head)
```

### Code 04-06 연결 리스트 일반적인 삽입 구현

```python
# 삽입
def insert_node(find_data, insert_data):
    global memory, head, current, pre
    node = Node()
    node.data = insert_data

    # 첫 노드 앞 삽입
    if head.data == find_data:
        node.link = head
        head = node
        return
    
    # 중간 노드 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node.link = current
            pre.link = node
            return

    # 마지막 노드까지 find_data가 없으면 끝에 삽입
    current.link = node
```

### Code 04-07 연결 리스트 일반적인 삭제 구현

```python
# 삭제
def delete_node(delete_data):
    global memory, head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del(current)
            return
```

## 5장 원형 연결 리스트

원형 리스트는 생성 시 첫 노드를 건드리면 마지막 노드의 링크를 바뀐 첫 노드로 바꿔주어야 한다.

그 외에는 원형과 선형 연결 리스트의 구현이 비슷하다

```python
last = head
while last.link != head:
    last = last.link
last.link = node
head = node
```