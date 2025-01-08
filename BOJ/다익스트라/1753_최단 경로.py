from heapq import *
from collections import defaultdict

total_node_count, total_edge_count = map(int,input().split(" "))

visited = [False for _ in range(total_node_count+1)]
distance_table = [int(1e9) for _ in range(total_node_count+1)]
link_table = defaultdict(lambda: defaultdict(lambda : int(1e9)))

start_node = int(input())
distance_table[start_node] = 0

for _ in range(total_edge_count):
    node1, node2, weight = map(int, input().split(" "))
    link_table[node1][node2] = min(link_table[node1][node2],weight)

heap = [[0,start_node]]

while heap:
    now_distance, now_node = heappop(heap)
    visited[now_node] = True

    for link_node in link_table[now_node]:
        if visited[link_node] == True:
            continue

        if distance_table[link_node] > now_distance + link_table[now_node][link_node] :
            distance_table[link_node] = now_distance +link_table[now_node][link_node]

            heappush(heap,[distance_table[link_node],link_node])

for distance in distance_table[1:]:
    if distance == int(1e9):
        print("INF")
        continue

    print(distance)