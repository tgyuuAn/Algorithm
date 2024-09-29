from collections import defaultdict
from heapq import *

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    
    for path in paths:
        x, y, cost = path
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    gates = set(gates)
    summits = set(summits)
    table = [int(1e9) for _ in range(n+1)]
    
    heap = []
    for gate in gates:
        heappush(heap, (0, gate))
        table[gate] = 0
    
    temp_heap = []
    while heap:
        now_intensity, now = heappop(heap)
        if now in summits: continue
        if table[now] < now_intensity: continue
        
        for neighbor, cost in graph[now]:
            if neighbor in gates: continue
            if table[neighbor] <= max(now_intensity, cost): continue
            
            table[neighbor] = max(now_intensity, cost)
            heappush(temp_heap, (max(now_intensity, cost), neighbor))

        if len(heap) == 0:
            heap = temp_heap

    answer = []
    for node, intensity in enumerate(table):
        if node == 0: continue
        
        if node in summits:
            if len(answer) == 0: 
                answer = [node, intensity]
                continue
                
            if answer[1] > intensity:
                answer = [node, intensity]
                
            elif answer[1] == intensity and answer[0] > node:
                answer = [node, intensity]
                
    return answer