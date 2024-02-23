import sys

V, E = map(int,sys.stdin.readline().split())

def find_parent(element, graph):
    if element == graph[element]: return element

    parent = find_parent(graph[element], graph)
    graph[element] = parent
    return parent

def union_find(first, second, graph):
    x = find_parent(first, graph)
    y = find_parent(second, graph)

    if x == y: return False

    x, y = max(x, y), min(x,y)
    graph[x] = y
    return True

edges = []

for _ in range(E):
    start, destination, cost = map(int,sys.stdin.readline().split())
    edges.append([cost,start,destination])  

edges.sort(key = lambda x:x[0])
parent_graph = [x for x in range(V+1)]
answer = 0

for edge in edges:
    cost, start, destination = edge
    if union_find(start, destination, parent_graph):
        answer += cost
    
print(answer)