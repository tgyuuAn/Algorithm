from collections import deque

def solution(places):
    
    answer = []
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for place in places:
        
        #거리 계산하는 board
        distance_board = [[int(1e9) for _ in range(5)] for _ in range(5)]
        
        #앉아있는 사람 간의 간격 계산하는 board
        gap_board = [[int(1e9) for _ in range(5)] for _ in range(5)]
        
        for y in range(5):
            for x in range(5):
                
                #flag 세팅 파티션이면 지나갈 수 없음
                flag = [[True if place[y][x] != "X" else False for x in range(5)] for y in range(5)]
        
                #사람이 앉아있고, 지나가지 않았을 경우 BFS 시작
                if place[y][x] == "P" and flag[y][x] == True:

                    #만약 처음 만나는 P일 경우, 해당 distance는 0으로 설정
                    if distance_board[y][x] == int(1e9):
                        distance_board[y][x] = 0
                        gap_board[y][x] = 0
                        
                    deq = deque([[x,y,distance_board[y][x]]])
                    flag[y][x] = False
                    
                    
                    while deq:
                        now = deq.popleft()
                        now_x, now_y, now_distance = now[0], now[1], now[2]
                        
                        for idx in range(4):
                            new_x = now_x + dx[idx]
                            new_y = now_y + dy[idx]
                            
                            if new_x < 0 or new_x > 4:
                                continue
                                
                            if new_y < 0 or new_y > 4:
                                continue
                                
                            if flag[new_y][new_x] == False:
                                continue
                            
                            #if문으로 빠지지 않았을 경우
                            deq.append([new_x,new_y, now_distance + 1])
                            flag[new_y][new_x] = False
                            
                            #만약 사람이 앉아있지 않으면 경로의 거리 계산
                            if place[new_y][new_x] != "P":
                                distance_board[new_y][new_x] = now_distance + 1
                            
                            #만약 사람이 앉아있으면 temp리스트에 추가
                            if place[new_y][new_x] == "P":
                                
                                #만약 새로 측정된 거리의 gap이 원래의 gap보다 작을 경우
                                if (now_distance + 1) - distance_board[y][x] < distance_board[new_y][new_x]:
                                    new_gap = (now_distance + 1) - distance_board[y][x]
                                    distance_board[new_y][new_x] = new_gap
                                    gap_board[new_y][new_x] = min(new_gap, gap_board[new_y][new_x])
                                    
                                else:
                                    new_gap = distance_board[new_y][new_x]
                                    distance_board[new_y][new_x] = new_gap
                                    gap_board[new_y][new_x] = min(new_gap, gap_board[new_y][new_x])

        #gap_board로 추출한 앉아있는 사람들 간의 작은 간격 비교
        temp = []
        for distance in gap_board:
            for d in distance:
                if d != int(1e9):
                    temp.append(d)

        #시작 할 때의 0을 제외한 1과 2가 없을 경우 성공으로써 1 추가
        if 1 not in temp and 2 not in temp:
            answer.append(1)

        #1과 2가 있으면 거리두기 실패한 것이므로 0 추가
        else:
            answer.append(0)
        
    return answer