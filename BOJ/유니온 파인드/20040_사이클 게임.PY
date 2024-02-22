N, M = map(int,input().split())

graph = [x for x in range(N+1)]

def union_find(first, second, graph):
    x = find(first, graph)
    y = find(second, graph)
    if x == y: return True
    x, y = min(x,y), max(x,y)
    graph[y] = x
    return False

def find(element, graph):
    if element == graph[element]: return element
    graph[element] = find(graph[element], graph)
    return graph[element]

for round in range(1,M+1):
    first, second = map(int,input().split())
    if union_find(first, second, graph):
        print(round)
        break

else: print(0)