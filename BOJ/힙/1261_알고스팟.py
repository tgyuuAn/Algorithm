import sys
from heapq import *

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []
for _ in range(M): 
    board.append(list(input()))

heap = [(0, 0, 0)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = set()
visited.add((0,0))

while heap:
    now_cost, now_x, now_y = heappop(heap)

    if (now_x, now_y) == (N-1, M-1): 
        print(now_cost)
        break

    for dir in range(4):
        new_x = now_x + dx[dir]
        new_y = now_y + dy[dir]

        if new_x < 0 or new_x >= N: continue
        if new_y < 0 or new_y >= M: continue
        if (new_x, new_y) in visited: continue
        
        if board[new_y][new_x] == "1": heappush(heap, (now_cost+1, new_x, new_y))
        else: heappush(heap, (now_cost, new_x, new_y))
        visited.add((new_x, new_y))
