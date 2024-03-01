import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def input(): return sys.stdin.readline()

N = int(input())
graph = defaultdict(list)
table = [int(1e9) for _ in range(N+1)]
table[1] = 0

def dfs(now, visited, table):
    for next, cost in graph[now]:
        if next in visited: continue
        
        visited.add(next)
        table[next] = table[now] + cost
        dfs(next, visited, table)
    

for _ in range(N-1):
    start, destination, cost = map(int,input().split())
    graph[start].append([destination, cost])
    graph[destination].append([start, cost])

visited = {1,}
dfs(1, visited, table)

max_value = -1
max_idx = 0
for idx, value in enumerate(table):
    if idx == 0: continue

    if max_value < value:
        max_value = value
        max_idx = idx

visited = {max_idx,}
table = [int(1e9) for _ in range(N+1)]
table[max_idx] = 0
dfs(max_idx, visited, table)
print(max(table[1:]))