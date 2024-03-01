import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def input(): return sys.stdin.readline()

N = int(input())
graph = defaultdict(list)
table = [[int(1e9),x] for x in range(N+1)]
table[1] = [0, 1]

def dfs(now, visited, table):
    for next, cost in graph[now]:
        if next in visited: continue
        
        visited.add(next)
        table[next][0] = table[now][0] + cost
        dfs(next, visited, table)
    

for _ in range(N-1):
    start, destination, cost = map(int,input().split())
    graph[start].append([destination, cost])
    graph[destination].append([start, cost])

visited = {1,}
dfs(1, visited, table)
table.sort(key = lambda x:x[0], reverse=True)

max_idx = table[1][1]

visited = {max_idx,}
table = [[int(1e9),x] for x in range(N+1)]
table[max_idx][0] = 0
dfs(max_idx, visited, table)

table.sort(key = lambda x:x[0], reverse=True)
answer = table[2][0]

max_idx = table[1][1]

visited = {max_idx,}
table = [[int(1e9),x] for x in range(N+1)]
table[max_idx][0] = 0
dfs(max_idx, visited, table)

table.sort(key = lambda x:x[0], reverse=True)
answer = max(answer, table[2][0])
print(answer)
