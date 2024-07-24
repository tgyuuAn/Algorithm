import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent_graph = [x for x in range(N+1)]

def find_parent(element, parent_graph):
    if element == parent_graph[element]: return element
    parent = parent_graph[element]
    parent_graph[element] = find_parent(parent, parent_graph)
    return parent_graph[element]

def union(first, second, parent_graph):
    x = find_parent(first, parent_graph)
    y = find_parent(second, parent_graph)

    x, y = min(x, y), max(x, y)
    parent_graph[y] = x
    return

for _ in range(M):
    query, node1, node2 = map(int, input().split())

    if query == 0:
        union(node1, node2, parent_graph)

    if query == 1:
        find_parent(node1, parent_graph)
        find_parent(node2, parent_graph)
        if parent_graph[node1] == parent_graph[node2]: print("YES")
        else: print("NO")