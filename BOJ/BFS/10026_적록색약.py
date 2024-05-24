from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

idx = 0
board = []
for _ in range(N):
    board.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = set()
deq = deque()
normal_answer = 0
for row in range(N):
    for col in range(N):
        if (row, col) in visited: continue
    
        normal_answer += 1
        visited.add((row, col))
        deq.append((row, col))

        while deq:
            now_row, now_col = deq.popleft()

            for dir in range(4):
                new_row = now_row + dy[dir]
                new_col = now_col + dx[dir]

                if new_row < 0 or new_row >= N: continue
                if new_col < 0 or new_col >= N: continue
                if (new_row, new_col) in visited: continue

                if board[row][col] == board[new_row][new_col]:
                    deq.append((new_row, new_col))
                    visited.add((new_row, new_col))

visited = set()
deq = deque()
color_blindness_answer = 0
for row in range(N):
    for col in range(N):
        if (row, col) in visited: continue

        color_blindness_answer += 1
        visited.add((row, col))
        deq.append((row, col))

        while deq:
            now_row, now_col = deq.popleft()

            for dir in range(4):
                new_row = now_row + dy[dir]
                new_col = now_col + dx[dir]

                if new_row < 0 or new_row >= N: continue
                if new_col < 0 or new_col >= N: continue
                if (new_row, new_col) in visited: continue

                if board[row][col] in ("R", "G") and board[new_row][new_col] in ("R", "G") or board[row][col] == board[new_row][new_col] == "B":
                    deq.append((new_row, new_col))
                    visited.add((new_row, new_col))

print(normal_answer, color_blindness_answer)