import sys
from copy import *

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int,input().split())))


answer = 0
def check(board):
    global answer
    
    for col in range(N):
        for row in range(M):
            # 첫 번째 도형
            if col <= N-4: answer = max(answer, sum(board[row][col:col+4]))
        
            # 두 번째 도형
            if col <= N-2 and row <= M-2: 
                temp = sum(board[row][col:col+2])
                temp += sum(board[row+1][col:col+2])
                answer = max(answer, temp)
            
            # 세 번째 도형
            if col <= N-2 and row <= M-3: 
                temp = board[row][col]
                temp += board[row+1][col]
                temp += sum(board[row+2][col:col+2])
                answer = max(answer, temp)
                
            # 네 번째 도형
            if col <= N-2 and row <= M-3: 
                temp = board[row][col]
                temp += sum(board[row+1][col:col+2])
                temp += board[row+2][col+1]
                answer = max(answer, temp)
            
            # 다섯 번째 도형
            if col <= N-3 and row <= M-2: 
                temp = sum(board[row][col:col+3])
                temp += board[row+1][col+1]
                answer = max(answer, temp)
    import sys
from copy import *

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int,input().split())))

answer = 0
def check(board):
    global answer
    
    for row in range(N):
        for col in range(M):
            # 첫 번째 도형
            if col <= M-4: answer = max(answer, sum(board[row][col:col+4]))
        
            # 두 번째 도형
            if col <= M-2 and row <= N-2: 
                temp = sum(board[row][col:col+2])
                temp += sum(board[row+1][col:col+2])
                answer = max(answer, temp)
            
            # 세 번째 도형
            if col <= M-2 and row <= N-3: 
                temp = board[row][col]
                temp += board[row+1][col]
                temp += sum(board[row+2][col:col+2])
                answer = max(answer, temp)
                
            # 네 번째 도형
            if col <= M-2 and row <= N-3: 
                temp = board[row][col]
                temp += sum(board[row+1][col:col+2])
                temp += board[row+2][col+1]
                answer = max(answer, temp)
            
            # 다섯 번째 도형
            if col <= M-3 and row <= N-2: 
                temp = sum(board[row][col:col+3])
                temp += board[row+1][col+1]
                answer = max(answer, temp)
            
for horizontal_reverse in range(2):
    for vertical_reverse in range(2):
        new_board = deepcopy(board)
        
        if horizontal_reverse == 1:
            for row_idx in range(N):
                new_board[row_idx] = new_board[row_idx][-1::-1]
        
        
        if vertical_reverse == 1:
            for row_idx in range(int((N-0.1)/2)+1):
                for col_idx in range(M):
                    new_board[row_idx][col_idx], new_board[N-row_idx-1][col_idx] = new_board[N-row_idx-1][col_idx], new_board[row_idx][col_idx]
                
        for rotation_count in range(4):
            temp_board = []
            
            if rotation_count == 0: check(new_board)
            
            for i in range(rotation_count):
                for inner_col in range(M):
                    now_col = []
                    for inner_row in range(N-1,-1,-1):
                        now_col.append(new_board[inner_row][inner_col])
                        
                    temp_board.append(now_col)

                new_board = temp_board[:]
                temp_board.clear()
                N, M = M, N
                
            check(new_board)
    
print(answer)