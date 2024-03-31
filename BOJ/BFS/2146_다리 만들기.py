import sys
from collections import deque
from copy import deepcopy

def input(): return sys.stdin.readline().rstrip()

N = int(input())
board = []
for _ in range(N):
    _input = input().split()
    board.append(_input)

visited = set()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def make_bridge(bridge, board, visited):
    next_bridge = set()

    for row, col in bridge:
        board[row][col] = "1"

        for dir in range(4):
            new_row = row + dx[dir]
            new_col = col + dy[dir]

            if new_row < 0 or new_row >= N: continue
            if new_col < 0 or new_col >= N: continue
            if (new_row, new_col) in visited: continue

            if board[new_row][new_col] == "0":
                next_bridge.add((new_row, new_col))
                visited.add((new_row, new_col))

            if board[new_row][new_col] == "1":
                return None, True

    return next_bridge, False

answer = 10_001
for row in range(N):
    for col in range(N):
        if board[row][col] == "1":
            if ((row, col)) in visited: continue
        
            visited.add((row,col))
            deq = deque([(row, col)])
            bridge_visited = {(row,col),}
            next_bridge = set()

            # 초기 섬을 파악
            while deq:
                now_row, now_col = deq.popleft()

                for dir in range(4):
                    new_row = now_row + dy[dir]
                    new_col = now_col + dx[dir]

                    if new_row < 0 or new_row >= N: continue
                    if new_col < 0 or new_col >= N: continue
                    if (new_row, new_col) in visited: continue

                    if board[new_row][new_col] == "0":
                        next_bridge.add((new_row, new_col))
                        bridge_visited.add((new_row, new_col))

                    if board[new_row][new_col] == "1":
                        deq.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        bridge_visited.add((new_row, new_col))

            count = 1
            new_board = deepcopy(board)
            while True:
                next_bridge, result = make_bridge(next_bridge, new_board, bridge_visited)

                if result:
                    answer = min(answer, count)
                    break

                count += 1
