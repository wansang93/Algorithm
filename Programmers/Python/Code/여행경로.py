from collections import defaultdict

def init_graph(tickets):
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    return routes


def dfs(routes):
    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))
    return path[::-1]


def solution(tickets):
    routes = init_graph(tickets)
    for r in routes:
        routes[r].sort()
    print(routes)

    answer = dfs(routes)
    return answer

data = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(data))
