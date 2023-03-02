def solution(babbling):
    speak = ["aya","ye","woo","ma"]
    answer= 0 
    
    for x in babbling:
        for y in speak:
            if y*2 in x:
                break
            
            x = x.replace(y," ")
        
        else:
            x= x.strip()
            
            if len(x) == 0 :
                answer += 1
                
    return answer