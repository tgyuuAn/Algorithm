from collections import deque

def solution(ingredient):
    deq = deque(ingredient)
    temp = []
    flag = True
    answer = 0
    
    while deq:
        temp.append(deq.popleft())
        if len(temp)>=4 and temp[-4:] == [1,2,3,1]:
            temp.pop()
            temp.pop()
            temp.pop()
            temp.pop()
            answer += 1
            
    while flag:
        if len(temp)>=4 and temp[-4:] == [1,2,3,1]:
            temp.pop()
            temp.pop()
            temp.pop()
            temp.pop()
            answer += 1
        else:
            flag = False
        
    return answer