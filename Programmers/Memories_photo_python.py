def solution(name, yearning, photos):
    score = dict()
    answer = []
    
    for name, yearning in zip(name,yearning):
        score[name] = yearning
        
    for photo in photos:
        temp = 0
        for x in photo:
            if x in score:
                temp += score[x]
            
        answer.append(temp)
    return answer