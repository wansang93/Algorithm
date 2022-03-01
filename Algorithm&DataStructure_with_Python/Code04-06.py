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
    insert_node('다현', '화사')  # 처음 해드
    print_nodes(head)
    insert_node('사나', '솔라')  # 중간에
    print_nodes(head)
    insert_node('재남', '문별')  # 없을 때 마지막에
    print_nodes(head), print()

    delete_node('쯔위')  # 중간에 삭제
    print_nodes(head)
    delete_node('화사')  # 처음 해드 삭제
    print_nodes(head)
    delete_node('완상')  # 없는 거 삭제
    print_nodes(head)
