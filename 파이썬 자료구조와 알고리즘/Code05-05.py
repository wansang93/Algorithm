class Node():
    def __init__(self) -> None:
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current.link == None:
        return
    
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global memory, head, current, pre

    if head.data == find_data:
        node = Node()
        node.data = insert_data
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node
    node.link = head




memory = []
head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == "__main__" :
    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
    
    print_nodes(head)

    insert_nodes('다현', '화사')  # 제일 처음에 삽입
    print_nodes(head)

    insert_nodes('사나', '솔라')  # 중간에 삽입
    print_nodes(head)

    insert_nodes('완상', '문별')  # 없을 때
    print_nodes(head)