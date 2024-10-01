from collections import deque

def solution(n, t, m, timetable):
    arv_hour = 9
    arv_minute = 0
    arv_time = []
    
    for num in range(n):
        arv_time.append((arv_hour, arv_minute))
        
        arv_minute += t
        if arv_minute >= 60:
            arv_minute -= 60
            arv_hour += 1
    
    timedeq = []
    for time in timetable:
        hour = int(time[:2])
        minute = int(time[3:])
        timedeq.append((hour, minute))
    timedeq.sort()
    timedeq = deque(timedeq)
    
    last = ""
    for arv_hour, arv_minute in arv_time:
        count = 0
        while len(timedeq) > 0 and (arv_hour > timedeq[0][0] or (arv_hour == timedeq[0][0] and arv_minute >= timedeq[0][1])):
            count += 1
            last = timedeq.popleft()
            if count == m: break
            
        if count < m:
            last = (arv_hour, arv_minute+1)
    
    if last[1]-1 < 0:
        last = (last[0]-1, last[1]+59)
    else:
        last = (last[0], last[1]-1)
        
    answer = ''
    if len(str(last[0])) == 1:
        answer += f"0{last[0]}"
    else: answer += str(last[0])
    
    answer+=":"
    if len(str(last[1])) == 1:
        answer += f"0{last[1]}"
    else: answer += str(last[1])
        
    return answer