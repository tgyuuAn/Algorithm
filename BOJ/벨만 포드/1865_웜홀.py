import sys
from collections import defaultdict

for _ in range(int(sys.stdin.readline())):
    vertex_count, edge_count, minus_edge_count = map(int,sys.stdin.readline().split())
    edge_information = [[int(1e9) for _ in range(vertex_count+1)] for _ in range(vertex_count+1)]

    for _ in range(edge_count):
        start, destination, cost = map(int,sys.stdin.readline().split())
        edge_information[start][destination] = min(edge_information[start][destination],cost)
        edge_information[destination][start] = min(edge_information[destination][start],cost)

    for _ in range(minus_edge_count):
        start, destination, cost = map(int,sys.stdin.readline().split())
        cost *= -1
        edge_information[start][destination] = min(edge_information[start][destination],cost)

    cost_table = [int(1e9) for _ in range(vertex_count+1)]
    cost_table[1] = 0


    for _ in range(vertex_count-1):
        for start in range(1,vertex_count+1):
            for destination in range(1,vertex_count+1):
                cost_table[destination] = min(cost_table[destination], cost_table[start] + edge_information[start][destination])
    cycle_flag = False

    for start in range(1,vertex_count+1):
        for destination in range(1,vertex_count+1):
            if cost_table[start] + edge_information[start][destination] < cost_table[destination]:
                cycle_flag = True
                break
        if cycle_flag: break
    
    if cycle_flag: print("YES")
    else: print("NO")