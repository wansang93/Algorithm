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
