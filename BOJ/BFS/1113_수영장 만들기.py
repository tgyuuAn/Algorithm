from collections import deque, defaultdict
import sys

def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
pool = [[0 for _ in range(M+2)]]
for _ in range(N):
    row = [0]
    row.extend(list(map(int,list(input()))))
    row.append(0)
    pool.append(row)
pool.append([0 for _ in range(M+2)])

def is_boundary(row, col):
    if (row == 0) or (row == (N+1)): return True
    if (col == 0) or (col == (M+1)): return True
    return False

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

water_height = [[0 for _ in range(M+2)] for _ in range(N+2)]

for height in range(2,10):
    visited = set()
    
    for row in range(1, N+2):
        for col in range(1, M+2):
            if (row, col) in visited: continue
            if pool[row][col] >= height: continue

            deq = deque()
            deq.append((row, col))
            visited.add((row, col))
            is_contain_boundary = False
            temp_visited = {(row, col),}
            while deq:
                now_row, now_col = deq.popleft()
                
                for dir in range(4):
                    new_row = now_row + dy[dir]
                    new_col = now_col + dx[dir]

                    if new_row < 0 or new_row >= N+2: continue
                    if new_col < 0 or new_col >= M+2: continue
                    if (new_row, new_col) in visited: continue
                    if pool[now_row][now_col] >= height: continue
                    if is_boundary(new_row, new_col): is_contain_boundary = True

                    visited.add((new_row, new_col))
                    deq.append((new_row, new_col))
                    temp_visited.add((new_row, new_col))

            # 경계가 포함되어있을경우 그냥 넘어감
            if is_contain_boundary: continue
            for r, c in temp_visited:
                water_height[r][c] = max(water_height[r][c], height-pool[r][c])

answer = 0
for row in range(N+2):
    for col in range(M+2):
        answer += water_height[row][col]

print(answer)