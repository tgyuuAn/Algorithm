def solution(sequence, k):
    start , end = 0,0
    n = len(sequence)
    ans=[]
    temp = 0
    
    while True:        
        if end >= n and temp < k :
            break
            
        if temp == k:
            ans.append([start,end-1])
        
        if temp > k:
            temp -= sequence[start]
            start += 1
        else:
            if end==n:
                break
                
            temp += sequence[end]
            end += 1
    
    return sorted(ans,key=lambda x:x[1]-x[0])[0]