from collections import deque

def solution(order):
    order = deque(order)
    n = len(order)
    main = deque([x for x in range(1,n+1)])
    sub = deque()
    answer = 0
    flag = True
    
    while order and flag:
        target= order.popleft()
        flag = False
        
        while main or sub:
            if main and main[0] == target:
                main.popleft()
                answer+=1
                flag = True
                break
            
            if sub and sub[0] == target:
                sub.popleft()
                answer+=1
                flag = True
                break
                
            else:
                if main:
                    sub.insert(0,main.popleft())
                else:
                    break
    
    return answer