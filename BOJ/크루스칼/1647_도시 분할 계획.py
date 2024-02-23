import sys

V, E = map(int,sys.stdin.readline().split())
edges = []

for _ in range(E):
    start, destination, cost = map(int,sys.stdin.readline().split())
    edges.append([cost, start, destination])

def union_find(first, second, graph):
    x = find_parent(first, graph)
    y = find_parent(second, graph)

    if x==y: return False

    x, y = max(x, y), min(x, y)
    graph[x] = y
    return True

def find_parent(element, graph):
    if element == graph[element]: return element
    
    parent = find_parent(graph[element], graph)
    graph[element] = parent
    return parent

graph = [x for x in range(V+1)]
edges.sort(key = lambda x : x[0])
answer = 0
max_cost = 0
for edge in edges:
    cost, start, destination = edge
    if find_parent(start,graph) != find_parent(destination,graph):
        union_find(start, destination, graph)
        answer += cost
        max_cost = max(max_cost, cost)

print(answer-max_cost)