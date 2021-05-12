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
