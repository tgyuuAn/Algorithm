def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    for word in s:
        now = ord(word)
        indexCopy = index
        while indexCopy > 0:
            now += 1
            
            if now> ord("z"):
                now = ord("a") + now - ord("z") - 1
            
            while chr(now) in skip:
                now += 1
                
                if now> ord("z"):
                    now = ord("a") + now - ord("z") - 1
                    
            indexCopy -= 1
        answer += chr(now)
    return answer