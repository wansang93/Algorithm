    # 입력
    # 1
    # 5 3
    # 1 0 0 1 0
    # 0 1 0 0 1
    # 0 0 0 1 0
    # 0 0 0 0 0
    # 0 0 1 0 0

    # 출력
    # 3

test = int(input())
a, b = map(int, input().split())
graph = []
for i in range(a):
    graph.append(list(map(int, input().split())))

print(graph)

def solution(b, graph):
    answer = 0
    c = a-b+1
    for x in range(c):
        for y in range(c):
            sum = 0
            for i in range(b):
                for j in range(b):
                    sum += graph[i+x][j+y]
            if answer < sum:
                answer = sum

    return answer

print(solution(b, graph))