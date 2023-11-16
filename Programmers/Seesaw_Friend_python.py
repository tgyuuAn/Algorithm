from collections import Counter

def solution(weights):
    answer = 0
    cnt = Counter(weights)
    
    for num in cnt.items():
        if num[1] >=2 :
            answer += (num[1] * (num[1]-1)) / 2
    
    weights = set(weights)
    
    for weight in weights:
        if weight * 2/3 in weights :
            answer += cnt[weight] * cnt[weight * 2/3]
            
        if weight * 1/2 in weights :
            answer += cnt[weight] * cnt[weight * 1/2]
            
        if weight * 3/4 in weights :
            answer += cnt[weight] * cnt[weight * 3/4]
    
    return answer