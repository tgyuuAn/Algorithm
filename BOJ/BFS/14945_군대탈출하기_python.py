from collections import deque

N,M = map(int,input().split())

dp_table = [[[i,int(1e9),int(1e9)] for i in map(int,input().split())] for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

deq = deque()
dp_table[0][0] = [dp_table[0][0][0],dp_table[0][0][0],int(1e9)]
deq.append([0,0])

while deq:
    now_x, now_y = deq.popleft()

    for direction in range(4):
        new_x, new_y = now_x + dx[direction], now_y + dy[direction]

        if new_x < 0 or new_x >= M:
            continue

        if new_y < 0 or new_y >= N:
            continue

        # 특수장비 사용하지 않음
        if dp_table[new_y][new_x][1] > max(dp_table[now_y][now_x][1],dp_table[new_y][new_x][0]):
            dp_table[new_y][new_x][1] = max(dp_table[now_y][now_x][1],dp_table[new_y][new_x][0])

            deq.append([new_x,new_y])

        # 이미 특수장비를 사용한 경우    
        if dp_table[new_y][new_x][2] > max(dp_table[now_y][now_x][2],dp_table[new_y][new_x][0]):
            dp_table[new_y][new_x][2] = max(dp_table[now_y][now_x][2],dp_table[new_y][new_x][0])
            
            if deq and deq[-1] == [new_x,new_y]:
                continue
            
            deq.append([new_x,new_y])

    for direction in range(4):
        new_x, new_y = now_x + dx[direction] * 2, now_y + dy[direction] * 2

        if new_x < 0 or new_x >= M:
            continue

        if new_y < 0 or new_y >= N:
            continue

        # 특수장비를 아직 사용하지 않은 경우
        # 특수장비 사용
        if dp_table[new_y][new_x][2] > max(dp_table[now_y][now_x][1],dp_table[new_y][new_x][0]):
            dp_table[new_y][new_x][2] = max(dp_table[now_y][now_x][1],dp_table[new_y][new_x][0])

            if deq and deq[-1] == [new_x,new_y]:
                continue
            
            deq.append([new_x,new_y])
    
    # for dp in dp_table:
    #       print(dp)
    # print()

print(min(dp_table[-1][-1][1:]))