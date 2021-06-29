def solution(param0):
    lst = []
    for param in param0:
        # 파일 이름 찾기
        raw_file_name = param.split('/')[-1]
        # 파일 버전 제거
        f_name, e_name = raw_file_name.split('.')
        if '_' in f_name:
            f_name = f_name[:f_name.find('_')]
        file_name = f_name + '.' + e_name
        # 파일별 갯수 찾기
        if file_name not in lst:
            lst.append(file_name)
            lst.append(1)
        else:
            lst[lst.index(file_name)+1] += 1

    # 갯수가 2개 이상이면 정답에 넣기
    answer = []
    for i in range(1, len(lst), 2):
        if 2 <= lst[i]:
            answer.append(lst[i-1])
            answer.append(str(lst[i]))

    return answer

params = ["/a/a_v2.x", "/b/a.x", "/c/t.z", "/d/a/t.x", "/e/z/t_v1.z", "/k/k/k/a_v9.x"]
print(solution(params))


def solution2(param0):
    COUNT = {
        "BOOL": 1,
        "SHORT": 2,
        "FLOAT": 4,
        "INT": 8,
        "LONG": 16
    }

    memory = ''
    MAX_MEMORY = 128
    for param in param0:
        count = COUNT[param]
        len_memory = len(memory)
        if count == 1:
            pass
        elif count == 2:
            if len_memory % 2 == 1:
                memory += '.'
        elif count == 4:
            if len_memory % 4 != 0:
                memory += '.' * (4 - len_memory % 4)
        else:
            if len_memory % 8 != 0:
                memory += '.' * (8 - len_memory % 8)
        memory += count * '#'
    
        if len(memory) > MAX_MEMORY:
            return "HALT"

    if len(memory) % 8 != 0:
        memory += '.' * (8 - len_memory % 8)
    
    length = 8
    return ','.join([memory[i:i+length] for i in range(0, len(memory), length)])


params = ["INT", "SHORT", "FLOAT", "INT", "BOOL", "LONG"]
print(solution2(params))

def solution(n, delivery):
    # a[0] = 'O', '?', 'X'
    a = ['?'] * n
    delivery = list(sorted(delivery, key=lambda x: x[2], reverse=True))
    for l in delivery:
        if l[2] == 1:
            a[l[0]-1] = 'O'
            a[l[1]-1] = 'O'
        else:
            if a[l[0]-1] == 'O':
                a[l[1]-1] = 'X'
            elif a[l[1]-1] == 'O':
                a[l[0]-1] = 'X'
    
    answer = ''.join(a)
    return answer

print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))  # "O?O?X?"
print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))  # "O?O?XXO"

def solution(encrypted_text, key, rotation):
    answer = ''
    
    # rotation 복구하기
    if rotation < 0:
        rotation = abs(rotation) % len(encrypted_text)
        encrypted_text = encrypted_text[-rotation:] + encrypted_text[:-rotation]
    else:
        rotation = rotation % len(encrypted_text)
        encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]

    for i, v in enumerate(encrypted_text):
        # v, key[i] 관계 설명하기
        difference = ord(v) - ord(key[i])
        if difference < 0:
            answer += chr(ord('z') + difference)
        else:
            answer += chr(ord('a') + difference - 1)

    return answer

print(solution('qyyigoptvfb', 'abcdefghijk', 3))  # 'hellopython'

def solution(v):
    global check_list, n, answer
    n = len(v)
    answer = [0, 0, 0]

    for y in range(n):
        for x in range(n):
            check_list = []
            temp = v[y][x]
            if temp == 0:
                answer[0] += 1
            elif temp == 1:
                answer[1] += 1
            elif temp == 2:
                answer[2] += 1
            else:
                continue
            

    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))  # [2,1,2]
print(solution([[0,0,1],[2,2,1],[0,0,0]]))  # [2,1,1]
