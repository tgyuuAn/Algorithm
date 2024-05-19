from collections import deque, defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

START = 1
TARGET = 100
N, M = map(int,input().split())
ledder = defaultdict(int)
special = set()

for _ in range(N+M):
    start, destination = map(int,input().split())
    ledder[start] = destination
    special.add(start)

deq = deque([(0,START)])
visited = {START,}
while deq:
    now_count, now_position = deq.popleft()

    if now_position == TARGET:
        print(now_count)
        break

    for dice in range(1,7):
        new_position = now_position + dice
        if new_position in special: new_position = ledder[new_position]
        if new_position in visited: continue
        if new_position > 100: continue
    
        deq.append((now_count+1, new_position))
        visited.add(new_position)