from collections import deque

def solution(maps):
    answer = []
    
    col = len(maps)
    row = len(maps[0])
    
    flag = [[False if maps[y][x] =="X" else True for x in range(row)] for y in range(col)]
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
        
    
    for y in range(col):
        for x in range(row):
            if(flag[y][x] == False):
                continue
            
            deq = deque()
            flag[y][x] = False
            deq.append([x,y])
            temp = int(maps[y][x])
                
            while deq:
                now = deq.popleft()
                now_x, now_y= now[0], now[1]
                
                for i in range(4):
            
                    new_x = now_x + dx[i]
                    new_y = now_y + dy[i]
                    
                    if(new_x < 0 or new_y <0):
                        continue
                        
                    if(new_x >= row or new_y >= col):
                        continue
                    
                    if(flag[new_y][new_x] == False):
                        continue    
                
                    temp += int(maps[new_y][new_x])
                    flag[new_y][new_x] = False
                    deq.append([new_x,new_y])
            
            answer.append(temp)

    return sorted(answer) if len(answer) != 0 else [-1]