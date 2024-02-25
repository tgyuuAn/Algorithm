import sys

computers_count = int(sys.stdin.readline())
connections_count = int(sys.stdin.readline())

computers = [x for x in range(1,computers_count+1)]

def union_find(first, second, graph):
    x = find_parent(first, graph)
    y = find_parent(second, graph)

    x, y = max(x, y), min(x, y)
    graph[x] = y
    return

def find_parent(element, graph):
    if element == graph[element]: return element
    parent = find_parent(graph[element],graph)
    graph[element] = parent
    return parent

for _ in range(computers_count):
    start, destination = map(int,sys.stdin.readline().split())
    union_find(start,destination,computers)

sum([computers == 1])