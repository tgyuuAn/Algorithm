from collections import deque

def check(nx,ny):
    if nx<= -1 or nx >= 11:
        return True
    if ny<= -1 or ny >= 11:
        return True
    return False

def solution(dirs):
    dirs = deque(dirs)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    log = []
    nowX, nowY = 5,5
    answer = 0

    while dirs:
        temp = dirs.popleft()
        if temp == "U":
            
            nx = nowX+dx[0]
            ny = nowY+dy[0]

            if check(nx,ny):
                continue
            
            if [nowX,nowY,nx,ny] not in log:
                log.append([nowX,nowY,nx,ny])
                log.append([nowX,ny,nx,nowY])
                answer += 1

            nowX, nowY = nx,ny

        elif temp == "D":
            
            nx = nowX+dx[1]
            ny = nowY+dy[1]

            if check(nx,ny):
                continue
            
            if [nowX,nowY,nx,ny] not in log:
                log.append([nowX,nowY,nx,ny])
                log.append([nowX,ny,nx,nowY])
                answer += 1

            nowX, nowY = nx,ny

        elif temp == "L":
            
            nx = nowX+dx[2]
            ny = nowY+dy[2]

            if check(nx,ny):
                continue
            
            if [nowX,nowY,nx,ny] not in log:
                log.append([nowX,nowY,nx,ny])
                log.append([nx,nowY,nowX,ny])
                answer += 1

            nowX, nowY = nx,ny

        elif temp == "R":
            
            nx = nowX+dx[3]
            ny = nowY+dy[3]

            if check(nx,ny):
                continue
            
            if [nowX,nowY,nx,ny] not in log:
                log.append([nowX,nowY,nx,ny])
                log.append([nx,nowY,nowX,ny])
                answer += 1

            nowX, nowY = nx,ny

    return answer