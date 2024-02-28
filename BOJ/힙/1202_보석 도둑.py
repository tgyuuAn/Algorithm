from heapq import *
import sys

def input():
    return sys.stdin.readline()

N, K = map(int,input().split())
heap = []
for _ in range(N):
    cost, value = map(int,input().split())

    heappush(heap,[cost, -1*value])

backpack = []
for _ in range(K):
    backpack.append(int(input()))

backpack.sort()
answer = 0
temp = []
for maximum_weight in backpack:
    while heap:
        now_wegiht, now_value = heap[0]
        if now_wegiht > maximum_weight: break
        heappop(heap)
        heappush(temp, now_value)

    if len(temp)>0:
        answer += -1*heappop(temp)

print(answer)