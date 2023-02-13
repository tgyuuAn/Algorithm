def solution(n, s):
    
    if n>s:
        return [-1]
    
    if s//n == s/n:
        return [s/n for _ in range(n)]
    
    else:
        tempSum = (s//n)*n
        temp = [s//n for _ in range(n)]
        
        for x in range(len(temp)-1,0,-1):
            temp[x]+=1
            tempSum +=1
            
            if tempSum == s:
                return temp