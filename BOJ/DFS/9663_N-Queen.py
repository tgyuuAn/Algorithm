chess_count = int(input())

board = [None for _ in range(chess_count)]
visited = [False for _ in range(chess_count)]
answer = 0

def dfs(board, idx, visited):
    global answer
    
    if idx == len(board):
        if all(visited):
            answer += 1
        return

    for num in range(len(visited)):
        if visited[num] == True:
            continue

        for prev_idx, prev_num in enumerate(board[:idx]):
            if prev_num == num - (idx - prev_idx) or prev_num == num + (idx - prev_idx):
                break
        else:
            board[idx] = num
            visited[num] = True
            dfs(board, idx+1, visited)
            board[idx] = None
            visited[num] = False

for idx in range(chess_count):
    board[0] = idx
    visited[idx] = True
    dfs(board, 1, visited)
    visited[idx] = False

print(answer)