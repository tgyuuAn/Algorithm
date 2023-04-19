def solution(park, routes):
    totalX = len(park[0])
    totalY = len(park)
    tempRoute = []

    for route in routes:
        direction, count = route.split()
        count = int(count)
        tempRoute.append([direction,count])

    def check(newX,newY):
        if newX >= totalX or newY >= totalY or newX < 0 or newY <0:
            return True

        if park[newY][newX] == "X":
            print(newX,newY,totalX,totalY)
            return True
        
        if park[newY][newX] == "O":
            return False

    동,서,남,북 = 0,1,2,3

    for y in range(totalY):
        for x in range(totalX):
            if park[y][x] == "S":
                nowX, nowY = x,y
                break

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for route in tempRoute:

        direction, count = route[0], route[1]
        tempX, tempY = nowX, nowY
            
        for _ in range(count):
            if direction == "N":
                newX = tempX + dx[북]
                newY = tempX + dy[북]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY

            elif direction == "S":
                newX = tempX + dx[남]
                newY = tempY + dy[남]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY
                    
            elif direction == "W":
                newX = tempX + dx[서]
                newY = tempY + dy[서]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY
                    
            elif direction == "E":
                newX = tempX + dx[동]
                newY = tempY + dy[동]
                
                if check(newX,newY):
                    break
                else:
                    tempX, tempY = newX, newY
                    
        else:
            nowX, nowY = newX, newY
    return nowY,nowX