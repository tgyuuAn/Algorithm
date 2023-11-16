def solution(dartResult):
    answer = []
    temp = 0
    numTemp = ""
    num = False
    
    for result in dartResult:
        if result == "*":
            if len(answer) == 1:
                answer[0] *= 2
            else:
                answer[-1] *= 2
                answer[-2] *= 2

                
        elif result == "#":
            answer[-1] *= -1
                
        elif result.isalpha():
            if num == True:
                temp = int(numTemp)
                numTemp = ""
                num = False
                
            if result == "D":
                temp **=2
                
            elif result == "T":
                temp **=3
            
            answer.append(temp)
            temp = 0
        
        elif result.isdigit():
            num = True
            numTemp += result
            
    return sum(answer)