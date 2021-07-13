########## 카카오페이 채용연계형 인턴 ###############

# 1번 문제
def solution(money, minratio, maxratio, ranksize, threshold, months):

    now_money = money
    for _ in range(months):
        if now_money < threshold:
            return now_money
        소유가정금액 = (now_money // 100) * 100
        idx = 0
        for now_ratio in range(minratio, maxratio+1):
            if now_ratio >= maxratio:
                now_money -= 소유가정금액 * now_ratio // 100
                break
            if threshold + idx * ranksize <= 소유가정금액 < threshold + (idx+1) * ranksize:
                now_money -= 소유가정금액 * now_ratio // 100
                break
            now_ratio += 1
            idx += 1

    return now_money


money = 1000000000
minratio = 50
maxratio = 99
ranksize = 100000
threshold = 0
months = 6
print(solution(money, minratio, maxratio, ranksize, threshold, months))

# 2번 문제
def solution(rows, columns, swipes):
    answer = []
    
    # 메트릭스 생성
    matrix = [[0] * columns for i in range(rows)]
    idx = 1
    for x in range(rows):
        for y in range(columns):
            matrix[x][y] = idx
            idx += 1
    # print(matrix)
 
    for swipe in swipes:
        d = swipe[0]
        r1, c1, r2, c2 = map(lambda x: x-1, swipe[1:])
        overflow = []

        if d == 1:
            for c in range(c1, c2+1, 1):
                temp = 0
                for r in range(r1, r2+1, 1):
                    temp, matrix[r][c] = matrix[r][c], temp
                matrix[r1][c] = temp
                overflow.append(temp)
        
        elif d == 2:
            for c in range(c2, c1-1, -1):
                temp = 0
                for r in range(r2, r1-1, -1):
                    temp, matrix[r][c] = matrix[r][c], temp
                matrix[r2][c] = temp
                overflow.append(temp)

        elif d == 3:
            for r in range(r1, r2+1, 1):
                temp = 0
                for c in range(c1, c2+1, 1):
                    temp, matrix[r][c] = matrix[r][c], temp
                matrix[r][c1] = temp
                overflow.append(temp)

        elif d == 4:
            for r in range(r2, r1-1, -1):
                temp = 0
                for c in range(c2, c1-1, -1):
                    temp, matrix[r][c] = matrix[r][c], temp
                matrix[r][c2] = temp
                overflow.append(temp)

        # print(matrix)
        answer.append(sum(overflow)) 

    return answer

rows = 4
columns = 3
swipes = [
    [1, 1, 2, 4, 3],
    [3, 2, 1, 2, 3],
    [4, 1, 1, 4, 3],
    [2, 2, 1, 3, 3]
]
print(solution(rows, columns, swipes))

# 3번 문제
def solution(line1, line2):
    answer = 0

    return answer

line1 = 'abbbcbbb'
line2 = 'bbb'
print(solution(line1, line2))


# 4번 문제
import heapq

def solution(ages, wires):
    answer = []
    l = len(ages)

    # 그래프 생성, 발전기 정보 생성
    generators = [(age, idx+1) for idx, age in enumerate(ages)]
    graph = [[] for _ in range(l+1)]
    for wire in wires:
        start, end, length = wire
        graph[start].append((end, length))
    print(graph)  # [[], [(2, 5), (3, 2)], [(1, 5)], [(4, 2), (5, 20)], [(5, 1)], []]
    print(generators)  # [(35, 1), (25, 2), (3, 3), (8, 4), (7, 5)]


    return answer

ages = [35, 25, 3, 8, 7]
wires = [[1, 2, 5], [2, 1, 5], [1, 3, 2], [3, 4, 2], [3, 5, 20], [4, 5, 1]]
print(solution(ages, wires))






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
