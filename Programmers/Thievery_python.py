def solution(money):
    n = len(money)
    answer = -1
    
    money_2 = money[:]
    money_2[0] = 0
    money[-1] = 0
    for idx, value in enumerate(money):
        if idx == 0:
            continue
            
        if idx == 1:
            money[1] = max(money[0], money[1])
            continue
            
        money[idx] = max(money[idx-1], (money[idx]+money[idx-2]))
        
    for idx, value in enumerate(money_2):
        if idx == 0:
            continue
            
        if idx == 1:
            money[1] = max(money_2[0], money_2[1])
            continue
            
        money_2[idx] = max(money_2[idx-1], (money_2[idx]+money_2[idx-2]))
        
    return max(money[-1],money_2[-1])