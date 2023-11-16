def solution(storey):
    
    answer = 0
    flag = False
    storey = str(storey)
    for y in range(len(storey)-1,-1,-1):
        x = int(str(storey)[y])
        
        if(flag == True):
            x += 1
            flag = False
            
        if(y==0):
            if x>=6:
                answer += 10-x+1
            else:
                answer += x
                
            return answer

        if(x>=6):
            answer += (10 - x)
            flag = True
            
        elif(x<=4):
            answer += x
        
        else:
            if y>=1:
                if int(storey[y-1])>=5:
                    answer += (10 - x)
                    flag = True
                else:
                    answer += x