import sys

cities_count = int(sys.stdin.readline())
target = int(sys.stdin.readline())
graph = [x for x in range(cities_count+1)]

def union_find(first, second, graph):
    x = find_parent(first, graph)
    y = find_parent(second, graph)

    x, y = max(x,y), min(x,y)
    graph[x] = y
    return

def find_parent(element, graph):
    if element == graph[element]: return element
    parent = find_parent(graph[element], graph)
    graph[element] = parent
    return parent

for start_idx in range(1,cities_count+1):
    travel_info = list(map(int,sys.stdin.readline().split()))

    for idx, info in enumerate(travel_info):
        if info == 1: union_find(start_idx, idx+1, graph)
        
travel_plan = list(map(int,sys.stdin.readline().split()))
group = -1
for plan in travel_plan:
    if group == -1:
        group = find_parent(plan,graph)
        continue
    
    if group != find_parent(plan,graph):
        print("NO")
        break
    
else: print("YES")