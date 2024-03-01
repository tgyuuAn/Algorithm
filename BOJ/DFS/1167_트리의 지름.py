import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def input(): return sys.stdin.readline()

N = int(input())
graph = defaultdict(list)
table = [int(1e9) for x in range(N+1)]
table[1] = 0

def dfs(now, visited, table):
    stack = [now]

    while stack:
        now = stack.pop()
        for next, cost in graph[now]:
            if next in visited: continue
            
            visited.add(next)
            table[next] = table[now] + cost
            stack.append(next)

for _ in range(N-1):
    start, destination, cost = map(int,input().split())
    graph[start].append([destination, cost])
    graph[destination].append([start, cost])

# 임의의 점으로 가가장 먼 점 구하기
visited = {1,}
dfs(1, visited, table)

# 가장 먼 점을 구했음.
max_value = -1
max_idx = 0
for idx, value in enumerate(table):
    if idx == 0: continue
    if max_value < value:
        max_value = value
        max_idx = idx

# 가장 먼 점으로 부터 다시 DFS 돌리기기
visited = {max_idx,}
table = [int(1e9) for x in range(N+1)]
table[max_idx] = 0
dfs(max_idx, visited, table)

# 또 다른 먼 점 구하기
max_value = -1
another_max_idx = 0
for idx, value in enumerate(table):
    if idx == 0: continue

    if max_value < value:
        max_value = value
        another_max_idx = idx

answer = -1
for idx, value in enumerate(table):
    if idx == 0: continue
    if idx == another_max_idx: continue

    if answer < value:
        answer = value
        
# 또 다른 먼점으로 부터 거리 구하기
visited = {another_max_idx, max_idx}
table = [int(1e9) for x in range(N+1)]
table[another_max_idx] = 0
dfs(another_max_idx, visited, table)

for idx, value in enumerate(table):
    if idx == 0: continue
    if idx == max_idx: continue
    if answer < value: answer = max(answer,value)
        
print(answer)