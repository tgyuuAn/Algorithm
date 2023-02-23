def solution(lottos, win_nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    dif = 0
    cor = 0
    zero = 0
    
    for x in sorted(lottos):
        
        if x in win_nums:
            cor +=1
        else:
            dif +=1
        if x == 0:
            zero += 1
        
    win = cor+min(dif,zero)
    lose = cor
    
    return [rank[win],rank[lose]]