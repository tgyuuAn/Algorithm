from collections import defaultdict
from heapq import *
import sys

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
target_floor = list(map(int,sys.stdin.readline().split()))
out_degree = defaultdict(int)
in_degree = defaultdict(int)
visited = {x for x in range(1,N+1)}

for idx, target in enumerate(target_floor):
    out_degree[idx+1] = target
    in_degree[target] += 1

stack = []
stack.append(out_degree[1])
answer = []

while stack:
    if len(stack) == 0: break
    if len(visited) == 0: 
        if len(stack) > 0:
            answer.append(stack[0])
        break

    answer.append(stack[-1])
    now = stack.pop()

    if out_degree[now] != 0 and out_degree[now] in visited:
        in_degree[out_degree[now]] -= 1
        visited.discard(out_degree[now])
        stack.append(out_degree[now])

    else:
        min_idx = 0
        min_cost = int(1e9)
        for idx in visited:
            if min_cost > in_degree[idx]:
                min_idx = idx
                min_cost = in_degree[idx]

        stack.append(min_idx)
        visited.discard(min_idx)
        in_degree[out_degree[min_idx]] -= 1

print(len(answer))
print(*answer)