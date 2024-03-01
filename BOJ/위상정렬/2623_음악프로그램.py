import sys
from collections import defaultdict, deque

def input(): return sys.stdin.readline()

N, M = map(int,input().split())
indegrees = [0 for _ in range(N+1)]
graph = defaultdict(set)

for _ in range(M):
    sequence = list(map(int,input().split()))

    for prev_idx in range(1,len(sequence)-1):
        prev = sequence[prev_idx]
        for next_idx in range(prev_idx+1, len(sequence)):
            next = sequence[next_idx]
            if next not in graph[prev]:
                indegrees[next] += 1
                graph[prev].add(next)

visited = set()
deq = deque()
answer = []
break_flag = False
for idx, indegree in enumerate(indegrees):
    if idx == 0: continue

    if indegree == 0:
        deq.append(idx)
        answer.append(idx)
        visited.add(idx)

while deq:
    now = deq.popleft()

    for next in graph[now]:
        if next in visited:
            print(0)
            break
        indegrees[next] -= 1
        
        if indegrees[next] == 0:
            answer.append(next)
            visited.add(next)
            deq.append(next)
    
    if break_flag: break

if len(answer) == N:
    for x in answer:
        print(x)
        
else: print(0)