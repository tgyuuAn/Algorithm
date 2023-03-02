def solution(s):
    
    answer = 0
    savePoint = -1
    dic = {"now" : 0,
           "diff" : 0}
    
    index = 0
    while True:
        now = s[index]
        
        while True:
            if index == len(s):
                break
                
            if now == s[index]:
                dic["now"] += 1
            else:
                dic["diff"] += 1
                
            if dic["now"] == dic["diff"] and dic["now"] != 0:
                answer += 1
                savePoint = index
                index += 1
                dic["now"] = 0
                dic["diff"] = 0
                break
            
            index += 1
        
        
        if index == len(s):
            break
            
    if savePoint != len(s)-1:
        answer+=1
            
    return answer