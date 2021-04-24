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
