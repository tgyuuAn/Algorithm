from collections import Counter,defaultdict

def solution(X, Y):
    
    temp = defaultdict(int)
    tempX = Counter(X)
    tempY = Counter(Y)
    
    
    for x in tempX:
        if x in tempY:
            temp[x] = min(tempX[x],tempY[x])
    
    if len(temp) == 0:
        return "-1"
    
    if len(temp) == 1 and ("0" in temp):
        return "0"
    
    answer = ''
    for x in sorted(temp.keys(),reverse= True):
        answer += str(x)*temp[x]
    
    return answer