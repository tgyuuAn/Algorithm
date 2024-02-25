import sys
from heapq import *

max_row, max_col = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(max_row)]

start = [0,0]
target = [0,0]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = set()

for row_idx, board_row in enumerate(board):
    for col_idx, board_col in enumerate(board_row):
        if board_col == "S": start = [col_idx, row_idx]
        if board_col == "F": target = [col_idx, row_idx]
        if board_col == "g": 
            for dir in range(4):
                new_col = col_idx + dy[dir]
                new_row = row_idx + dx[dir]

                if new_col < 0 or new_col >= max_col: continue
                if new_row < 0 or new_row >= max_row: continue

                if board[new_row][new_col] == "." :
                    board[new_row][new_col] = "펑"

heap = []
heappush(heap,[0,0,start])
visited.add(tuple(start))

while heap:
    now_garbage, now_펑, [now_x, now_y] = heappop(heap)
    
    if [now_x, now_y] == target:
        print(now_garbage, now_펑)
        break
    
    for dir in range(4):
        new_x = now_x + dx[dir]
        new_y = now_y + dy[dir]
        
        if new_y < 0 or new_y >= max_row: continue
        if new_x < 0 or new_x >= max_col: continue
        if (new_x, new_y) in visited: continue
        
        if board[new_y][new_x] == "g":
            heappush(heap,[now_garbage+1, now_펑, [new_x, new_y]])
        
        elif board[new_y][new_x] == "펑":
            heappush(heap,[now_garbage, now_펑+1, [new_x, new_y]])
        
        else:
            heappush(heap,[now_garbage, now_펑, [new_x, new_y]])
            
        visited.add((new_x, new_y))