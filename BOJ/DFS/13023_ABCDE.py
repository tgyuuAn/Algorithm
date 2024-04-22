import sys
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)

def dfs(graph, now, depth, visited):
    if depth >= 5: return True

    for child in graph[now]:
        if child in visited: continue
        visited.add(child)
        result = dfs(graph, child, depth+1, visited)
        visited.discard(child)

        if result: return True

    return False

for _ in range(M):
    first, second = map(int, input().split())
    
    graph[first].append(second)
    graph[second].append(first)

for idx in range(N):
    result = dfs(graph, idx, 1, {idx,})

    if result: 
        print(1)
        break

else: print(0)