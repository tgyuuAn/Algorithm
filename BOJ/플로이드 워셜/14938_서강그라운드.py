vertex_count, search_range, edge_count = map(int,input().split())
items = [0]
items.extend(list(map(int,input().split())))

graph = [[int(1e9) for _ in range(vertex_count+1)] for _ in range(vertex_count+1)]

for _ in range(edge_count):
    start, destination, items_count = map(int,input().split())
    graph[start][destination] = items_count
    graph[destination][start] = items_count
    
for idx in range(1,vertex_count+1):
    graph[idx][idx] = 0
    
for mid in range(1,vertex_count+1):
    for start in range(1,vertex_count+1):
        for destination in range(1,vertex_count+1):
            graph[start][destination] = min(graph[start][destination], graph[start][mid] + graph[mid][destination])

max_items_count = 0
for landing_idx in range(1,vertex_count+1):
    temp_items_count = 0
    
    for neighbor_idx, neighbor_distance in enumerate(graph[landing_idx]):
        if neighbor_distance <= search_range:
            temp_items_count += items[neighbor_idx]
            
    if temp_items_count > max_items_count:
        max_items_count = temp_items_count
        
print(max_items_count)