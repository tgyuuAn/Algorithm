import sys
from heapq import *

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
DP = [[[int(1e9) for _ in range(2)] for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

heap = []
heappush(heap, (1,0,0,1))
DP[0][0][1] = 1
while heap:
    now_time, now_x, now_y, now_remain = heappop(heap)
    
    if DP[now_y][now_x][now_remain] < now_time: continue
    
    for direction in range(4):
        new_x = now_x + dx[direction]
        new_y = now_y + dy[direction]
        
        if new_x < 0 or new_x >= M: continue
        if new_y < 0 or new_y >= N: continue
        
        if board[new_y][new_x] == "1":
            if now_remain == 0: continue
            if DP[new_y][new_x][now_remain-1] <= now_time+1: continue
                
            heappush(heap, (now_time+1, new_x, new_y, now_remain-1))
            DP[new_y][new_x][now_remain-1] = now_time+1
            
        else:
            if DP[new_y][new_x][now_remain] <= now_time+1: continue
                
            heappush(heap, (now_time+1, new_x, new_y, now_remain))
            DP[new_y][new_x][now_remain] = now_time+1
            
print(min(DP[N-1][M-1]) if min(DP[N-1][M-1]) != int(1e9) else -1)