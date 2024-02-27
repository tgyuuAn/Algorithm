from heapq import *
import sys

N = int(sys.stdin.readline())
stars = []

for _ in range(N):
    x, y = map(float,sys.stdin.readline().split())
    stars.append([x,y])

graph = [[0 for _ in range(N)] for _ in range(N)]
parent_graph = [x for x in range(N)]
edge = []

def union_find(first, second, graph):
    x = find_parent(first, graph)
    y = find_parent(second, graph)

    x, y = max(x, y), min(x, y)
    graph[x] = y
    return graph[x]

def find_parent(element, graph):
    if element == graph[element]: return element
    parent = find_parent(graph[element], graph)
    graph[element] = parent
    return parent

for start_idx, [start_x, start_y] in enumerate(stars):
    for destination_idx, [destination_x, destination_y] in enumerate(stars):
        distance = (abs(destination_x - start_x)**2 + abs(destination_y - start_y)**2)**0.5
        graph[start_idx][destination_idx] = distance
        graph[destination_idx][start_idx] = distance

        heappush(edge,[distance, start_idx, destination_idx])

answer = 0
while edge:
    now_distance, now_start, now_destination = heappop(edge)

    if find_parent(now_start, parent_graph) == find_parent(now_destination, parent_graph): continue

    union_find(now_start, now_destination, parent_graph)
    answer += now_distance

print(round(answer,2))