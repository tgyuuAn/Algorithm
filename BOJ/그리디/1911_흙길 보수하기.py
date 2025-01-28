import sys
import math

def input(): return sys.stdin.readline()

N,L = map(int, input().split())

pools = []

for _ in range(N):
    start, end = map(int, input().split())
    pools.append((start, end))
    
pools.sort()

answer = 0
previous = 0
for pool in pools:
    start, end = pool
    start = max(start, previous)
    
    gap = (end - start)
    need = math.ceil(gap/L)
    previous = start + (L * need)
    answer += need
    
print(answer)