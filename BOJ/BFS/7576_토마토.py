from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

M, N = map(int ,input().split())

tomato_box = []
ripe_tomatoes = deque()
visited = set()
for row in range(N):
    row_tomato = list(map(int, input().split()))

    for col, tomato in enumerate(row_tomato):
        if tomato == 1: 
            visited.add((row, col))
            ripe_tomatoes.append((row, col, 0))

    tomato_box.append(row_tomato)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
while ripe_tomatoes:
    now_row, now_col, now_day = ripe_tomatoes.popleft()
    answer = now_day
    
    for dir in range(4):
        new_row = now_row + dy[dir]
        new_col = now_col + dx[dir]
        
        if new_row < 0 or new_row >= N: continue
        if new_col < 0 or new_col >= M: continue
        if (new_row, new_col) in visited: continue
        if tomato_box[new_row][new_col] != 0: continue
    
        tomato_box[new_row][new_col] = 1
        visited.add((new_row, new_col))
        ripe_tomatoes.append((new_row, new_col, now_day+1))

flag = False
for row in range(N):
    for col in range(M):
        if tomato_box[row][col] == 0:
            flag = True
            break
    
    if flag: break
    
print(-1) if flag == True else print(answer)