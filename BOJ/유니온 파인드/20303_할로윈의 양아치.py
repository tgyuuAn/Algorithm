from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

def find_parent(graph, element):
    if graph[element] == element: return element
    parent = graph[element]
    graph[element] = find_parent(graph, parent)
    return graph[element]

def union(graph, first, second):
    x = find_parent(graph, first)
    y = find_parent(graph, second)

    x, y = min(x, y), max(x, y)
    graph[y] = x
    return x

N, M, K = map(int, input().split())
C = list(map(int,input().split()))
parent = [x for x in range(N+1)]

for _ in range(M):
    first, second = map(int, input().split())
    union(parent, first, second)

candies = defaultdict(list)

for idx, key in enumerate(parent[1:]):
    key = find_parent(parent, key)
    
    if len(candies[key]) == 0:
        candies[key] = [1, C[idx]]
        continue
    
    candies[key][0] += 1
    candies[key][1] += C[idx]

DP = [0 for _ in range(K)]

for need_count, candy_count in candies.values():
    
    for idx in range(K-1, need_count-1, -1):
        DP[idx] = max(DP[idx], DP[idx-need_count] + candy_count)
        
print(max(DP))