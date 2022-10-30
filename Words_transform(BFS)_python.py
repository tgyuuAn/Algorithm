from collections import deque

def check(query, word):
    diff = 0
    for i in range(len(query)):
        if query[i] != word[i]:
            diff +=1
    return diff==1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([[begin,0]])
    while queue:
        x,cnt = queue.popleft()
        if x==target:
            return cnt
        
        for word in words:
            if x==word:
                continue
                
            if check(x,word):
                queue.append([word, cnt+1])
    return 0