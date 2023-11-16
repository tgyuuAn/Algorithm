from collections import Counter

def solution(participant, completion):
    temp = Counter(participant)
    
    for x in completion:
        temp[x] -= 1
        
        if temp[x] == 0:
            del temp[x]
    
    
    return list(temp.keys()).pop()