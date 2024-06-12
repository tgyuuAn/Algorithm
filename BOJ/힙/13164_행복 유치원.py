from heapq import *
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
children = list(map(int, input().split()))

gap = []
prev = 0
for idx, child in enumerate(children):
    if idx == 0:
        prev = child
        continue

    heappush(gap,(-1*abs(child-prev), idx))
    prev = child

link = [N]
for _ in range(M-1):
    value, idx = heappop(gap)
    heappush(link, idx)

answer = 0
prev = 0
while link:
    now_idx = heappop(link)

    if prev == now_idx-1:
        prev = now_idx
        continue

    else:
        answer += children[now_idx-1] - children[prev]
        prev = now_idx

print(answer)