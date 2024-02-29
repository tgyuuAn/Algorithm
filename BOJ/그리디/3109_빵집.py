import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

R,C = map(int,input().split())

dx = [1,1,1]
dy = [-1,0,1]

board = [list(input()) for _ in range(R)]
answer = 0

def dfs(now_y, now_x):
    global answer

    for dir in range(3):
        new_y = now_y + dy[dir]
        new_x = now_x + dx[dir]

        if new_y < 0 or new_y >= R: continue
        if board[new_y][new_x] == "x": continue

        board[new_y][new_x] = "x"

        # 끝 자리에 도달하면 탈출
        if new_x == C-1: return True
        if dfs(new_y, new_x): return True

for idx in range(R):
    board[idx][0] = "x"
    if dfs(idx, 0): answer += 1

print(answer)