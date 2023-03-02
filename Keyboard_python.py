def solution(keymap, targets):
    answer = []
    temp = set()
    for x in keymap:
        temp.update(set(x))
    
    print(temp)
    
    for x in targets:
        if set(x)-temp:
            answer.append(-1)
        else:
            temp2 = 0
            for y in x:
                minTemp = int(1e9)
                for z in keymap:
                    if y in z:
                        minTemp = min(minTemp,z.index(y)+1)
                temp2 += minTemp
            
            answer.append(temp2)
    return answer