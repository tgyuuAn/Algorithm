from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()
INF = int(1e9)

N, M = map(int, input().split())

floyd = [[INF for _ in range(N+1)] for _ in range(N+1)]
for init in range(N+1):
    if init == 0: continue
    floyd[init][init] = 0
    
for _ in range(M):
    first, second = map(int, input().split())
    floyd[first][second] = 1
    floyd[second][first] = 1

for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
            floyd[start][end] = min(floyd[start][end], floyd[start][mid] + floyd[mid][end])

min_value = INF
min_idx = -1
for idx, info in enumerate(floyd):
    if idx == 0: continue

    temp = sum(info[1:])
    if temp < min_value:
        min_value = temp
        min_idx = idx
        
print(min_idx)