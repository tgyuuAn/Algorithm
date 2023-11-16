from collections import deque
from math import ceil

def solution(n, stations, w):
    answer = 0
    station = deque([-w])
    station.extend(stations)
    station.append(n+w+1)
    
    for x in range(0,len(station)-1):
        gap=station[x+1]-station[x]-1-(2*w)
        answer += ceil(gap/((2*w)+1))

    return answer