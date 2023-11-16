from collections import deque
def solution(cacheSize, cities):
    answer = 0
    deq = deque(cities)
    temp = deque()
    while deq:
        city = deq.popleft().upper()
        if city not in temp:
            temp.append(city)
            answer +=5
        else:
            temp.remove(city)
            temp.append(city)
            answer +=1
        
        if len(temp) > cacheSize:
            temp.popleft()

    return answer