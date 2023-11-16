from collections import defaultdict
def solution(number, limit, power):
    answer = 0
    dic = defaultdict(int)
    for x in range(1,number+1):
        for y in range(x,number+1,x):
            dic[y]+=1
    
    for x in dic.values():
        if x<=limit:
            answer += x
        else:
            answer += power
            
    return answer