from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i] == True:
            continue
            
        else:
            visited[i] = True
            queue = deque(computers[i])
            idx=0
            while queue:
                if idx>=n:
                    idx-=n
                if queue.popleft()==1 and visited[idx]==False:
                    visited[idx]=True
                    queue.extend(computers[idx])
                idx +=1
            answer +=1
    return answer