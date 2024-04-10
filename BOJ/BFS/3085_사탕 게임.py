from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
board = []

for _ in range(N):
    board.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = set()
answer = 1
for col in range(N):
    for row in range(N):
        for dir in range(4):
            new_col = col + dy[dir]
            new_row = row + dx[dir]

            if new_col < 0 or new_col >= N: continue
            if new_row < 0 or new_row >= N: continue
            if ((col, row, new_col, new_row)) in visited: continue
            if ((new_col, new_row, col, row)) in visited: continue

            visited.add(((col, row, new_col, new_row)))
            board[col][row], board[new_col][new_row] = board[new_col][new_row], board[col][row]
            
            temp = 0
            is_connect = False
            for check_col in range(N):
                if check_col == col:
                    is_connect = True
                    
                if board[check_col][row] == board[col][row]:
                    temp+=1
                    
                else: 
                    if is_connect: 
                        answer = max(answer, temp)
                        break
                    temp=0
            
            if is_connect: 
                answer = max(answer, temp)
            
            temp = 0
            is_connect = False
            for check_row in range(N):
                if check_row == row:
                    is_connect = True
                    
                if board[col][check_row] == board[col][row]:
                    temp+=1
                    
                else: 
                    if is_connect: 
                        answer = max(answer, temp)
                        break
                    temp=0
            
            if is_connect: 
                answer = max(answer, temp)
            
            temp = 0
            is_connect = False
            for check_col in range(N):
                if check_col == new_col:
                    is_connect = True
                    
                if board[check_col][new_row] == board[new_col][new_row]:
                    temp+=1
                    
                else: 
                    if is_connect: 
                        answer = max(answer, temp)
                        break
                    temp=0
            
            if is_connect: 
                answer = max(answer, temp)
            
            temp = 0
            for check_row in range(N):
                if check_row == new_row:
                    is_connect = True
                    
                if board[new_col][check_row] == board[new_col][new_row]:
                    temp+=1

                else: 
                    if is_connect: 
                        answer = max(answer, temp)
                        break
                    temp=0
            
            if is_connect: 
                answer = max(answer, temp)
                    
            board[col][row], board[new_col][new_row] = board[new_col][new_row], board[col][row]   
            
print(answer)