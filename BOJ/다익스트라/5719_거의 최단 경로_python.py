from collections import defaultdict, deque
from heapq import *
from sys import stdin

while True:
    total_node_count, total_edge_count = map(int,stdin.readline().split())
    
    if(total_node_count == 0 and total_edge_count == 0):
        break

    start, destination = map(int,stdin.readline().split())
    table = [int(1e9) for _ in range(total_node_count)]
    prev = [[] for _ in range(total_node_count)]
    graph = defaultdict(lambda : defaultdict(lambda : int(1e9)))

    for _ in range(total_edge_count):
        start_node, next_node, cost = map(int,stdin.readline().split())
        graph[start_node][next_node] = cost

    table[start] = 0
    heap = [[0,start]]

    while heap:
        now_cost, now_start = heappop(heap)

        if table[now_start] < now_cost:
            continue
        
        for now_destination, cost in graph[now_start].items():

            new_cost = now_cost + cost

            if table[now_destination] < new_cost: continue

            elif table[now_destination] > new_cost:
                heappush(heap,[new_cost,now_destination])
                table[now_destination] = new_cost
                prev[now_destination] = [now_start]

            elif table[now_destination] == new_cost:
                prev[now_destination].append(now_start)

    print(table[destination])
    print(prev)

    visited = [False for _ in range(total_node_count)]
    deq = deque([destination])
    print()

    while deq:
        print(deq)
        now = deq.popleft()
        print(now)
        
        if visited[now] == True:
            continue
        print()

        for prev_node in prev[now]:
            print(prev_node)
            deq.append(prev_node)
            print(deq)
            graph[prev_node][now] = int(1e9)

        visited[now] = True

    for key in graph:
        print(key, graph[key])

    table = [int(1e9) for _ in range(total_node_count)]
    table[start] = 0
    heap = [[0,start]]

    print()
    while heap:
        now_cost, now_start = heappop(heap)
        if table[now_start] < now_cost:
            continue

        for now_destination, cost in graph[now_start].items():
            new_cost = now_cost + cost

            if table[now_destination] > new_cost:
                heappush(heap,[new_cost,now_destination])
                table[now_destination] = new_cost

    if table[destination] >= int(1e9): print("-1")
    else: print(table[destination])
    