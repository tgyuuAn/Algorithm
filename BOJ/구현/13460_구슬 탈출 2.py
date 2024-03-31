n, m = map(int,input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(str,input())))

def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    while MAP[nx + dx][ny + dy] != '#' and MAP[nx][ny] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx,  ny, cnt

for r in range(n):
    for c in range(m):
        if MAP[r][c] == 'R':
            # red starting x, y
            rsx, rsy = r, c
        if MAP[r][c] == 'B':
            # blue starting x, y
            bsx, bsy = r, c
        if MAP[r][c] == 'O':
            # hole x, y
            ox, oy = r, c

# print(MAP)            

def solution():
    visited = {}
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    visited[(rsx,rsy)] = 1
    s = [[rsx,rsy,bsx,bsy,0]]

    while s:
        rx, ry, bx, by, cnt = s.pop(0)
        if cnt >= 10:
            return -1

        for dx, dy in moves:
            rrx, rry, rcnt = move(rx,ry,dx,dy)
            bbx, bby, bcnt = move(bx,by,dx,dy)

            if MAP[bbx][bby] != 'O':
                if rrx == ox and rry == oy:
                    return cnt + 1

                if rrx == bbx and rry == bby:
                    if rcnt > bcnt:
                        rrx, rry = rrx-dx, rry-dy
                    else:
                        bbx, bby = bbx-dx, bby-dy

                if (rrx,rry,bbx,bby) in visited:
                    continue
                else:
                    visited[(rrx,rry,bbx,bby)] = 1
                    s.append([rrx,rry,bbx,bby,cnt+1])

    return -1

print(solution())