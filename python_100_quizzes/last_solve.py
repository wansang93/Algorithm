graph = {1: [2, 3, 4],
    2: [1, 3, 4, 5, 6],
    3: [1, 2, 7],
    4: [1, 2, 5, 6],
    5: [2, 4, 6, 7],
    6: [2, 4, 5, 7],
    7: [3, 5, 6]}

# 입력 1 7
# 출력 6

# a, b = map(int, input().split())

# def solution(start, end, graph):
#     count = 0
#     MAX_COUNT = 0
#     stack = [start]

#     while stack:
#         n = stack.pop()
#         stack += graph[n] - set(visited)
#         count += 1
#         if end == n:
#             if count > MAX_COUNT:
#                 MAX_COUNT = count


#     return MAX_COUNT


# print(solution(a, b, graph))


start, end = [int(i) for i in input().split()]
queue = [start]
visited = []

def sol(n, visited):
	if n[-1] == end:
		return len(visited)
	
	if n[-1] in visited:
		return len(visited)
	
	visited.append(n[-1])
	length = 0
	
	for next_node in graph[n[-1]]:
		n.append(next_node)
		length = max(length, sol(n, visited))
		queue.pop(-1)
	return length

print(sol(queue, visited))