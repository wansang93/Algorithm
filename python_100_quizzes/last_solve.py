graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(dfs(graph, 'E'))


tree = {
        'A': ['B', 'C', 'E'],
        'B': ['A'],
        'C': ['A'],
        'D': ['E', 'F'],
        'E': ['A', 'D'],
        'F': ['D']
}

# 왼쪽

def treedfs(tree, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += tree[n] - set(visited)

    return visited


print(treedfs(graph, 'E'))