from collections import deque

col, row, height = map(int,input().split())

tomato_box = [[[-1 for _ in range(col)] for _ in range(row)] for _ in range(height)]
ripe_tomatoes = deque()
unripe_tomatoes_count = 0
days = 0

for h in range(height):
    for r in range(row):
        tomato_box[h][r] = list(map(int,input().split()))

for h in range(height):
    for r in range(row):
        for c in range(col):
            if tomato_box[h][r][c] == 0:
                unripe_tomatoes_count += 1
            
            elif tomato_box[h][r][c] == 1:
                ripe_tomatoes.append((h,r,c,0))

dc = [0,0,-1,1,0,0]
dr = [-1,1,0,0,0,0]
dh = [0,0,0,0,-1,1]

while ripe_tomatoes:

    for h in range(height):
        for r in range(row):
            print(tomato_box[h][r])

        print()
    
    h,r,c,days = ripe_tomatoes.popleft()

    for idx in range(6):
        new_h, new_r, new_c = h + dh[idx], r + dr[idx], c + dc[idx]

        if new_h < 0 or new_h >= height:
            continue

        if new_r < 0 or new_r >= row:
            continue

        if new_c < 0 or new_c >= col:
            continue

        if tomato_box[new_h][new_r][new_c] == -1:
            continue

        if tomato_box[new_h][new_r][new_c] == 0:
            tomato_box[new_h][new_r][new_c] = 1
            ripe_tomatoes.append((new_h,new_r,new_c,days+1))
            unripe_tomatoes_count -= 1

if unripe_tomatoes_count == 0: print(days)
else: print("-1")