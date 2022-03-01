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