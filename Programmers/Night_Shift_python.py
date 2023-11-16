from heapq import *

def solution(n, works):
    work = [-x for x in works]
    answer = 0
    heapify(work)
    
    for x in range(n):
        temp = heappop(work)
        
        if temp == 0:
            return 0
        
        heappush(work,temp+1)
        
    for y in work:
        answer += (-y)**2
    return answer