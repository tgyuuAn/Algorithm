def solution(survey, choices):
    dic = {"R" : 0,
          "J" : 0,
          "C" : 0,
          "A" : 0}
    
    for x,choice in zip(survey,choices):
        choice -= 4
        choice *= -1

        if "RT" in x:
            dic["R"] += choice
        if "TR" in x:
            dic["R"] -= choice
            
        if "CF" in x:
            dic["C"] += choice
        if "FC" in x:
            dic["C"] -= choice
            
        if "JM" in x:
            dic["J"] += choice
        if "MJ" in x:
            dic["J"] -= choice
            
        if "AN" in x:
            dic["A"] += choice
        if "NA" in x:
            dic["A"] -= choice
    print(dic)
    answer = ''
    
    if dic["R"] >= 0:
        answer += "R"
    else:
        answer += "T"
    
    if dic["C"] >= 0:
        answer += "C"
    else:
        answer += "F"
        
    if dic["J"] >= 0:
        answer += "J"
    else:
        answer += "M"
        
    if dic["A"] >= 0:
        answer += "A"
    else:
        answer += "N"

    return answer