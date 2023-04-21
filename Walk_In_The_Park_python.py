
def solution(park, routes):

    EAST,WEST,SOUTH,NORTH = 0,1,2,3
    
    totalX = len(park[0])
    totalY = len(park)
    tempRoute = []

    #방향, 칸수로 되어있는 걸 tempRoute리스트에 쪼개서 나눔
    for route in routes:
        direction, count = route.split()
        count = int(count)
        tempRoute.append([direction,count])

    def check(newX,newY):
        #새로운 X가 총X길이를 넘어가거나, 새로운 Y가 총 Y길이를 넘어가거나, 0보다 작아질 경우 True 반환
        if newX >= totalX or newY >= totalY or newX < 0 or newY <0:
            return True
        
        #만약 새로운 곳에 장애물이 있을 경우 True 반환
        if park[newY][newX] == "X":
            return True
        
        return False

    #예를 들어 "E"이면 현재위치에 dx[EAST], dy[EAST]를 더함
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


    #현재위치를 x,y에 저장.
    for y in range(totalY):
        for x in range(totalX):
            if park[y][x] == "S":
                nowX, nowY = x,y
                break

    
    for route in tempRoute:

        direction, count = route[0], route[1]
        tempX, tempY = nowX, nowY
            
        for _ in range(count):
            if direction == "N":
                newX = tempX + dx[NORTH]
                newY = tempY + dy[NORTH]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY

            elif direction == "S":
                newX = tempX + dx[SOUTH]
                newY = tempY + dy[SOUTH]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY
                    
            elif direction == "W":
                newX = tempX + dx[WEST]
                newY = tempY + dy[WEST]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY
                    
            elif direction == "E":
                newX = tempX + dx[EAST]
                newY = tempY + dy[EAST]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY
                    
        else:
            nowX, nowY = newX, newY
    return nowY,nowX