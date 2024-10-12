from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)

for idx in range(1,N+1):
    graph[idx] = list(map(int, input().split()))[1:]

matches_n = [0 for _ in range(N+1)]
matches_m = [0 for _ in range(M+1)]

def dfs(now, visited, graph):
    visited[now] = True
    
    for _next in graph[now]:
        if matches_m[_next] == 0:
            matches_m[_next] = now
            matches_n[now] = _next
            return True
            
        elif visited[matches_m[_next]] == False and dfs(matches_m[_next], visited, graph):
            matches_n[now] = _next
            matches_m[_next] = now
            return True
        
    return False

answer = 0
for idx in range(1, N+1):
    if matches_n[idx] == 0:
        visited = [0 for _ in range(N+1)]
        if dfs(idx, visited, graph):
            answer += 1
    
print(answer)