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