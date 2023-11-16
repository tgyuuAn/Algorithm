from heapq import heappush,heappop
from collections import deque

def solution(k, score):
    temp = []
    score = deque(score)
    answer = []
    
    while score:
        heappush(temp,score.popleft())
        if len(temp)>k:
            heappop(temp)
        answer.append(temp[0])
        
    return answer