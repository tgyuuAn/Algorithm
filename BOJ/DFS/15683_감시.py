import sys
import copy

sys.setrecursionlimit(10**5)

def input(): return sys.stdin.readline().rstrip()

def print_board(board): # for Test
    for row in board: print(row)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

camera_dirs = [
    [],
    [0],                # 1번 카메라: 한 방향
    [0, 2],             # 2번 카메라: 양쪽 방향
    [0, 1],             # 3번 카메라: 직각 방향
    [0, 1, 3],          # 4번 카메라: 세 방향
    [0, 1, 2, 3]        # 5번 카메라: 네 방향
]

def measure_reachable_zone(camera_type, rotate, board, now_x, now_y):
    new_board = copy.deepcopy(board)

    directions = [(d + rotate) % 4 for d in camera_dirs[camera_type]]
    for direction in directions:
        x, y = now_x, now_y
        while True:
            x += dx[direction]
            y += dy[direction]

            if not (0 <= x < len(board[0]) and 0 <= y < len(board)) or new_board[y][x] == 6:
                break

            if new_board[y][x] == 0:
                new_board[y][x] = "#"

    return new_board
    
def dfs(board, visited):
    global answer
    
    temp = 0
    for row in board:
        for col in row:
            if col == 0:
                temp += 1
    answer = min(answer, temp)
    
    for new_y in range(len(board)):
        for new_x in range(len(board[0])):
            if board[new_y][new_x] in {0, 6, "#"}: continue
            if (new_x, new_y) in visited: continue
            
            for rotate in range(4):
                new_board = measure_reachable_zone(board[new_y][new_x], rotate, board, new_x, new_y)
                visited.add((new_x, new_y))
                dfs(new_board, visited)
                visited.discard((new_x, new_y))
            return

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 64
dfs(board, set())
print(answer)