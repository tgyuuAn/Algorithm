import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = set()
answer = int(1e9)

def dfs(board, str_start, prev_idx, depth):
    global visited, answer

    if depth == N//2 and str_start not in visited:
        team_start = 0        
        team_link = 0
        str_link = ""
        start = set(map(int,str_start.rstrip().split()))
        
        for row in range(N):
            if row not in start: str_link += f"{row} "

            for col in range(N):
                 if row in start and col in start: team_start += board[row][col]
                 elif row not in start and col not in start: team_link += board[row][col]
        
        answer = min(answer, abs(team_start - team_link))
        visited.add(str_start)
        visited.add(str_link)
        return
    
    for idx in range(prev_idx+1,N):
        new_str_start = str_start + f"{idx} "
        dfs(board, new_str_start, idx, depth+1)

    return

dfs(board, "", 0, 0)
print(answer)