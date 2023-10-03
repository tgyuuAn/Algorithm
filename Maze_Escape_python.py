from collections import deque

def solution(maps):
    answer = 0
    len_row = len(maps)
    len_col = len(maps[0])
    start_row, start_col = 0,0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    flag = [[ True for _ in range(len_col)] for _ in range(len_row)]
    
    for row in range(len_row):
        for col in range(len_col):
            if maps[row][col] == "X":
                flag[row][col] = False
                
            if maps[row][col] == "S":
                start_row, start_col = row, col
    
    #레버 먼저 당기기
    deq = deque([[start_row,start_col,0]])
    flag[start_row][start_col] = False
    
    while deq:
        now = deq.popleft()
        now_row, now_col, now_time = now[0], now[1], now[2]
        
        if maps[now_row][now_col] == "L":
            answer += now_time
            start_row = now_row
            start_col = now_col
            break
        
        for idx in range(4):
            new_row = now_row + dx[idx]
            new_col = now_col + dy[idx]
            
            if new_row < 0 or new_row >= len_row:
                continue
                
            if new_col < 0 or new_col >= len_col:
                continue
                
            if flag[new_row][new_col] == False:
                continue
                
            #만약 위의 if문에서 걸리지 않았을 경우,
            deq.append([new_row,new_col,now_time+1])
            flag[new_row][new_col] = False
    else:
        return -1

    #레버 당겼으므로 레버 위치를 시작으로 출구 찾기
    flag = [[ True for _ in range(len_col)] for _ in range(len_row)]
    
    for row in range(len_row):
        for col in range(len_col):
            if maps[row][col] == "X":
                flag[row][col] = False

    deq = deque([[start_row,start_col,0]])
    flag[start_row][start_col] = False
    
    while deq:
        now = deq.popleft()
        now_row, now_col, now_time = now[0], now[1], now[2]
        
        if maps[now_row][now_col] == "E":
            answer += now_time
            break
        
        for idx in range(4):
            new_row = now_row + dx[idx]
            new_col = now_col + dy[idx]
            
            if new_row < 0 or new_row >= len_row:
                continue
                
            if new_col < 0 or new_col >= len_col:
                continue
                
            if flag[new_row][new_col] == False:
                continue
                
            #만약 위의 if문에서 걸리지 않았을 경우,
            deq.append([new_row,new_col,now_time+1])
            flag[new_row][new_col] = False
    else:
        return -1

    return answer


'''
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/159993#

BFS에서 deque popleft()한 지점에서 visited Flag를 False로 주게되면 중복이 발생할 수 있어 매우 시간이 오래걸림.

그렇기 때문에 new_row, new_col을 deque에 append시키는 시점에서 flag도 True에서 False로 갱신시켜줘야함.

중요!!
'''