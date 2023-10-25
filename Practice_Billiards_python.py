def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        temp = int(1e9)
        target_x, target_y = ball[0], ball[1]
        
        if startX != target_x:
            temp_x, temp_y = target_x, (n + (n-target_y))
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
            
            temp_x, temp_y = target_x, target_y * (-1)
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
            
        if startX == target_x:
            if startY>target_y:
                temp_x, temp_y = target_x, (n + (n-target_y))
                temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
                temp = min(temp, temp_distance)
                
            if startY<target_y:
                temp_x, temp_y = target_x, target_y * (-1)
                temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
                temp = min(temp, temp_distance)
            
        if (startY != target_y):
            temp_x, temp_y = (m + (m-target_x)), target_y
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
            
            temp_x, temp_y = target_x * (-1), target_y
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
                
        if startY == target_y:
            if startX > target_x:
                temp_x, temp_y = (m + (m-target_x)), target_y
                temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
                temp = min(temp, temp_distance)

            if startX < target_x:
                temp_x, temp_y = target_x * (-1), target_y
                temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
                temp = min(temp, temp_distance)
        
        if startX/startY != target_x/target_y:
            temp_x, temp_y = target_x * (-1), target_y * (-1)
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
        
        if (m-startX)/(n-startY) != (m-target_x)/(n-target_y):
            temp_x, temp_y = (m + (m - target_x)) , (n + (n - target_y))
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
            
        if startX/(n-startY) != target_x/(n-startY):
            temp_x, temp_y = target_x * (-1) , (n + (n - target_y))
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
        
        if (m-startX)/startY != (m-target_x)/startY:
            temp_x, temp_y = (m + (m - target_x)) , target_y * (-1)
            temp_distance = (temp_x-startX)**2 + (temp_y-startY)**2
            temp = min(temp, temp_distance)
        
        answer.append(temp)
    return answer