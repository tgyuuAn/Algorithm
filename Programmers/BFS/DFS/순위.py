from collections import deque

def solution(n, results):
    low = [[] for _ in range(n+1)]
    up = [[] for _ in range(n+1)]
    answer = 0

    for result in results:
        winner, loser = result
        low[winner].append(loser)
        up[loser].append(winner)
    
    for player in range(1,n+1):
        visited = [False for _ in range(n+1)]
        visited[player] = True
        deq = deque(low[player])
        
        for init in low[player]:
            visited[init] = True
        
        while deq:
            now = deq.popleft()
            
            for lower_player in low[now]:
                if visited[lower_player] == False:
                    deq.append(lower_player)
                    visited[lower_player] = True
                    
                    
        deq = deque(up[player])
        
        for init in up[player]:
            visited[init] = True
        
        while deq:
            now = deq.popleft()
            
            for upper_player in up[now]:
                if visited[upper_player] == False:
                    deq.append(upper_player)
                    visited[upper_player] = True
        
        if all(visited[1:]):
            answer+=1
            
    return answer