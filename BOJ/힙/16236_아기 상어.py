from heapq import *
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
board = []
start = None
for row_idx in range(N):
    row = list(map(int, input().split()))
    if 9 in row: start = row_idx, (row.index(9))
    board.append(row)

board[start[0]][start[1]] = 0
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

deq = []
heappush(deq,(-2, 0, 0, start[0], start[1]))
visited = set(start)
answer = 0
max_stack = 0
max_size = 2
while deq:
    now_size, now_stack, now_time, now_y, now_x = heappop(deq)
    now_size *= -1
    now_stack *= -1
    
    if max_size >= now_size and max_stack > now_stack: continue
    if max_size > now_size: continue

    if board[now_y][now_x] != 0 and board[now_y][now_x] < now_size:
        board[now_y][now_x] = 0
        visited = set()
        
        if now_stack + 1 == now_size: 
            now_size += 1
            now_stack = 0

        else: now_stack += 1
    
        max_size = now_size
        max_stack = now_stack
        answer += now_time
        now_time = 0
        
    for dir in range(4):
        new_y = now_y + dy[dir]
        new_x = now_x + dx[dir]

        if new_x < 0 or new_x >= N: continue
        if new_y < 0 or new_y >= N: continue
        if (new_x, new_y) in visited: continue
        if board[new_y][new_x] > max_size: continue
    
        heappush(deq,(now_size * -1, now_stack * -1, now_time + 1, new_y, new_x))
        visited.add((new_x, new_y))
    
print(answer)
