from collections import defaultdict

answer = 0

def dfs(info, graph, linked, visited, sheep, wolf):
    global answer
    answer = max(answer, sheep)

    for neighbor in linked:
        if neighbor in visited: continue

        # 양
        if info[neighbor] == 0:
            visited.add(neighbor)
            new_linked = linked | graph[neighbor]
            dfs(info, graph, new_linked, visited, sheep+1, wolf)
            visited.discard(neighbor)

        # 늑대
        else:
            if sheep > wolf+1:
                visited.add(neighbor)
                new_linked = linked | graph[neighbor]
                dfs(info, graph, new_linked, visited, sheep, wolf+1)
                visited.discard(neighbor)

    return

def solution(info, edges):
    global answer

    graph = defaultdict(set)
    visited = {0,}
    for edge in edges:
        x, y = edge
        graph[x].add(y)
        graph[y].add(x)
    
    linked = graph[0]
    dfs(info, graph, linked, visited, 1, 0)

    return answer